import { Admin, Resource } from 'react-admin';
import { authProvider } from './provider/authProvider';
import dataProvider from './provider/dataProvider';
import axios from 'axios';

import { Layout, LoginPage } from './layout';
import { Dashboard } from './view/Dashboard';
import Category from './view/Category';
import Clients from './view/Clients';
import Employees from './view/Employees';
import Persons from './view/Persons';
import Product from './view/Product';
import ProductAmount from './view/ProductAmount';
import Role from './view/Role';
import Workplace from './view/Workplace';

axios.interceptors.response.use(
	(response) => response,
	(error) => {
		if (error.response.status === 401) {
			localStorage.removeItem('token');
			window.location.href = '#/login';
		}
		return Promise.reject(error);
	}
);

axios.interceptors.request.use(
	(config) => {
		const token = localStorage.getItem(`token`) || null;
		if (token)
			config.headers = {
				...config.headers,
				authorization: `Bearer ${token}`,
			};
		return config;
	},
	(error) => {
		Promise.reject(error);
	}
);

const App = () => {
	return (
		<Admin
			dataProvider={dataProvider}
			loginPage={LoginPage}
			layout={Layout}
			authProvider={authProvider}
			dashboard={Dashboard}>
			<Resource name='category' {...Category} />
			<Resource name='clients' {...Clients} />
			<Resource name='employees' {...Employees} />
			<Resource name='persons' {...Persons} />
			<Resource name='product' {...Product} />
			{/* <Resource name='ProductAmount' {...ProductAmount} /> */}
			<Resource name='Role' {...Role} />
			<Resource name='Workplace' {...Workplace} />
		</Admin>
	);
};

export default App;
