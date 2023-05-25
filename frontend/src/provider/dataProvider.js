import {
	GET_LIST,
	GET_ONE,
	GET_MANY,
	GET_MANY_REFERENCE,
	CREATE,
	UPDATE,
	DELETE,
	DELETE_MANY,
	fetchUtils,
} from 'react-admin';
import { stringify } from 'query-string';
import endpoint from '../endpoint';

const API_URL = endpoint.baseUrl;

const convertDataProviderRequestToHTTP = async (type, resource, params) => {
	switch (type) {
		case GET_LIST: {
			const { page, perPage } = params.pagination;
			const { field, order } = params.sort;
			const query = {
				pageNumber: page - 1,
				pageSize: perPage === 1000 ? 10000 : perPage,
				filterHelper: params.filter,
				filteringEnabled:
					Object.keys(params.filter).length === 0 &&
					params.filter.constructor === Object
						? false
						: true,
				sortableFieldName: field,
				order: order,
			};
			let addressUrl = '';
			let urlParams = {};

			if (resource === 'product') {
				addressUrl = `${API_URL}/product`;
				urlParams = { method: 'POST', body: JSON.stringify(query) };
			}
			return {
				url: addressUrl,
				options: urlParams,
			};
		}
		case GET_ONE:
			let urlGet = `${API_URL}/${resource}/${params.id}`;

			if (resource === 'product') {
				urlGet = `${API_URL}/product/${params.id}`;
			}
			return { url: urlGet };
		case GET_MANY: {
			const query = {
				filter: JSON.stringify({ id: params.ids }),
			};
			return { url: `${API_URL}/${resource}?${stringify(query)}` };
		}
		case GET_MANY_REFERENCE: {
			const { page, perPage } = params.pagination;
			const { field, order } = params.sort;
			const query = {
				sort: JSON.stringify([field, order]),
				range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
				filter: JSON.stringify({
					...params.filter,
					[params.target]: params.id,
				}),
			};
			return { url: `${API_URL}/${resource}?${stringify(query)}` };
		}
		case UPDATE:
			let addressUrlUpdate = `${API_URL}/${resource}/${params.id}`;

			let method = 'POST';

			switch (resource) {
				case 'product':
					method = 'PUT';
					break;
				default:
					method = 'POST';
			}

			if (resource === 'product') {
				addressUrlUpdate = `${API_URL}/${resource}/product`;
			}
			return {
				url: addressUrlUpdate,
				options: { method, body: JSON.stringify(params.data) },
			};

		case CREATE:
			let addressUrlCreate = `${API_URL}/${resource}`;

			if (resource === 'product') {
				addressUrlCreate = `${API_URL}/product`;
			}
			return {
				url: addressUrlCreate,
				options: { method: 'POST', body: JSON.stringify(params.data) },
			};
		case DELETE:
			let addressUrlDelete = `${API_URL}/${resource}/${params.id}`;

			if (resource === 'product') {
				addressUrlDelete = `${API_URL}/product/${params.id}`;
			}

			return {
				url: addressUrlDelete,
				options: { method: 'DELETE' },
			};

		case DELETE_MANY:
			const query = {
				filter: JSON.stringify({ id: params.ids }),
			};

			let addressUrlDeleteMany = `${API_URL}/${resource}?${stringify(query)}`;

			if (resource === 'product') {
				addressUrlDeleteMany = `${API_URL}/product/?${stringify(query)}`;
			}

			return {
				url: addressUrlDeleteMany,
				options: { method: 'DELETE' },
			};

		default:
			throw new Error(`Unsupported fetch action type ${type}`);
	}
};

const convertHTTPResponseToDataProvider = (
	response,
	type,
	resource,
	params
) => {
	try {
		let { json, headers } = response;

		if (json === undefined) {
			localStorage.removeItem('mwlToken');
			window.location.href = '#/login';
		}
		switch (type) {
			case GET_LIST:
				return {
					data: json.items.map((x) => x),
					total: json.totalCount,
				};
			case GET_ONE:
				if (json.idInvoice) json.id = json.idInvoice;
				return {
					data: json,
				};
			case CREATE:
				return { data: { ...params.data, id: json.id } };
			default:
				return { data: json };
		}
	} catch (e) {
		console.log(e);
	}
};

const dataProvider = async (type, resource, params) => {
	const { fetchJson } = fetchUtils;
	const data = await convertDataProviderRequestToHTTP(type, resource, params);
	const { url, options } = data;

	const token = localStorage.getItem('token');

	const headers = new Headers({ authorization: token });

	const optionsWithToken = { ...options, headers };

	return fetchJson(url, optionsWithToken).then((response) =>
		convertHTTPResponseToDataProvider(response, type, resource, params)
	);
};
export default dataProvider;
