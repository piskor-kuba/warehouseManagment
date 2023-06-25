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
			if (resource === 'employee') {
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
			if (resource === 'employee') {
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

			if (resource === 'employee') {
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

			if (resource === 'employee') {
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
			let addressUrlDelete = `${API_URL}/${resource}/${params.id}`;

			if (resource === 'employee') {
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

			if (resource === 'employee') {
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
				if (resource === 'clients') {
					const ClientsData = json.map((obj) => {
						const { Clinet_id, ...rest } = obj;
						return { id: Clinet_id, ...rest };
					});
					return {
						data: ClientsData,
						total: ClientsData.length,
					};
				} else if (resource === 'product') {
					const ProductData = json.map((obj) => {
						const { product_id, ...rest } = obj;
						return { id: product_id, ...rest };
					});
					return {
						data: ProductData,
						total: ProductData.length,
					};
				} else if (resource === 'employee') {
					const EmployeeData = json.map((obj) => {
						const { Employee_id, ...rest } = obj;
						return { id: Employee_id, ...rest };
					});
					return {
						data: EmployeeData,
						total: EmployeeData.length,
					};
				} else {
					return {
						data: json,
						total: json.length,
					};
				}

			case GET_ONE:
				if (resource === 'product') {
					const { product_id, ...rest } = json;
					const ProductData = { id: product_id, ...rest };
					return {
						data: ProductData,
					};
				} else if (resource === 'clients') {
					const { Clinet_id, ...rest } = json;
					const ClientsData = { id: Clinet_id, ...rest };
					return {
						data: ClientsData,
					};
				} else if (resource === 'employee') {
					const { Employee_id, ...rest } = json;
					const EmployeeData = { id: Employee_id, ...rest };
					return {
						data: EmployeeData,
					};
				} else {
					return {
						data: json,
					};
				}

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
