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
			return {
				url: addressUrl,
				options: { method: 'GET' },
			};
		}
		case GET_ONE:
			let urlGet = `${API_URL}/${resource}/${params.id}`;

			// if (resource === 'Category') {
			// 	console.log(resource);
			// 	urlGet = `${API_URL}/category/${params.id}`;
			// }
			// if (resource === 'Clients') {
			// 	urlGet = `${API_URL}/client/${params.id}`;
			// }
			// if (resource === 'Employee') {
			// 	urlGet = `${API_URL}/employee/${params.id}`;
			// }
			// if (resource === 'Persons') {
			// 	urlGet = `${API_URL}/person/${params.id}`;
			// }
			// if (resource === 'Product') {
			// 	urlGet = `${API_URL}/product/${params.id}`;
			// }
			return { url: urlGet };

		case GET_MANY: {
			const query = {
				filter: JSON.stringify({ id: params.ids }),
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
				addressUrlCreate = `${API_URL}/product/`;
			}
			if (resource === 'category') {
				addressUrlCreate = `${API_URL}/category/`;
			}
			return {
				url: addressUrlCreate,
				options: { method: 'POST', body: JSON.stringify(params.data) },
			};

		case DELETE:
			let addressUrlDelete = `${API_URL}/${resource}/${params.id}`;

			if (resource === 'category') {
				addressUrlDelete = `${API_URL}/category/${params.id}`;
			}

			return {
				url: addressUrlDelete,
				options: { method: 'DELETE' },
			};

		case DELETE_MANY:
			
			let addressUrlDeleteMany = `${API_URL}/${resource}?${params.id}`;
			
			if (resource === 'category') {
				addressUrlDeleteMany = `${API_URL}/category/${params.id}`;
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

		// if (json === undefined) {
		// 	localStorage.removeItem('token');
		// 	window.location.href = '#/login';
		// }

		switch (type) {
			case GET_LIST:
				return {
					data: json,
					total: json.length,
				};
			case GET_ONE:
				// 	if (json.idInvoice) json.id = json.idInvoice;
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
