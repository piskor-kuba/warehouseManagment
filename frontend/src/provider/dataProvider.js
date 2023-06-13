import {
	GET_LIST,
	GET_ONE,
	GET_MANY,
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
	console.log(type);
	switch (type) {
		case GET_LIST: {
			const query = { skip: 0, limit: 100 };
			let addressUrl = '';

			if (resource === 'category') {
				addressUrl = `${API_URL}/category/?${stringify(query)}`;
			}
			if (resource === 'clients') {
				addressUrl = `${API_URL}/client/?${stringify(query)}`;
			}
			if (resource === 'employees') {
				addressUrl = `${API_URL}/employee/?${stringify(query)}`;
			}
			if (resource === 'persons') {
				addressUrl = `${API_URL}/person/?${stringify(query)}`;
			}
			if (resource === 'product') {
				addressUrl = `${API_URL}/product/?${stringify(query)}`;
			}
			if (resource === 'workplace') {
				addressUrl = `${API_URL}/workplace/?${stringify(query)}`;
			}
			if (resource === 'role') {
				addressUrl = `${API_URL}/role/?${stringify(query)}`;
			}
			return {
				url: addressUrl,
				options: { method: 'GET' },
			};
		}
		case GET_ONE:
			let urlGet = `${API_URL}/${resource}/${params.id}`;

			if (resource === 'category') {
				urlGet = `${API_URL}/category/${params.id}`;
			}
			if (resource === 'clients') {
				urlGet = `${API_URL}/client/${params.id}`;
			}
			if (resource === 'employees') {
				urlGet = `${API_URL}/employee/${params.id}`;
			}
			if (resource === 'persons') {
				urlGet = `${API_URL}/person/${params.id}`;
			}
			if (resource === 'product') {
				urlGet = `${API_URL}/product/${params.id}`;
			}
			return {
				url: urlGet,
				options: { method: 'GET' },
			};

		case GET_MANY: {
			const query = {
				filter: JSON.stringify({ id: params.ids }),
			};
			return { url: `${API_URL}/${resource}?${stringify(query)}` };
		}

		case UPDATE:
			let addressUrlUpdate = `${API_URL}/${resource}/${params.id}`;

			let method = 'PATCH';

			if (resource === 'employees') {
				addressUrlUpdate = `${API_URL}/employee/${params.id}`;
			}
			if (resource === 'clients') {
				addressUrlUpdate = `${API_URL}/client/${params.id}`;
			}
			if (resource === 'persons') {
				addressUrlUpdate = `${API_URL}/person/${params.id}`;
			}

			return {
				url: addressUrlUpdate,
				options: { method, body: JSON.stringify(params.data) },
			};

		case CREATE:
			let addressUrlCreate = `${API_URL}/${resource}/`;

			if (resource === 'employees') {
				addressUrlCreate = `${API_URL}/employee/`;
			}
			if (resource === 'clients') {
				addressUrlCreate = `${API_URL}/client/`;
			}
			if (resource === 'persons') {
				addressUrlCreate = `${API_URL}/person/`;
			}

			return {
				url: addressUrlCreate,
				options: { method: 'POST', body: JSON.stringify(params.data) },
			};

		case DELETE:
			console.log('XXDD');
			let addressUrlDelete = `${API_URL}/${resource}/${params.id}`;

			if (resource === 'employees') {
				addressUrlDelete = `${API_URL}/employee/${params.id}`;
			}
			if (resource === 'clients') {
				addressUrlDelete = `${API_URL}/client/${params.id}`;
			}
			if (resource === 'persons') {
				addressUrlDelete = `${API_URL}/person/${params.id}`;
			}

			return {
				url: addressUrlDelete,
				options: { method: 'DELETE' },
			};

		case DELETE_MANY:
			let addressUrlDeleteMany = `${API_URL}/${resource}/${params.ids[0]}`;

			if (resource === 'employees') {
				addressUrlDeleteMany = `${API_URL}/employee/${params.ids[0]}`;
			}
			if (resource === 'clients') {
				addressUrlDeleteMany = `${API_URL}/client/${params.ids[0]}`;
			}
			if (resource === 'persons') {
				addressUrlDeleteMany = `${API_URL}/person/${params.ids[0]}`;
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

		switch (type) {
			case GET_LIST:
				return {
					data: json,
					total: json.length,
				};
			case GET_ONE:
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

	const headers = new Headers({ authorization: `Bearer ${token}` });

	const optionsWithToken = { ...options, headers };

	return fetchJson(url, optionsWithToken).then((response) =>
		convertHTTPResponseToDataProvider(response, type, resource, params)
	);
};
export default dataProvider;
