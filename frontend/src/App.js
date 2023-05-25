import { Admin, Resource } from 'react-admin';
import { authProvider } from './provider/authProvider';
import dataProvider from './provider/dataProvider';
import { Layout, LoginPage } from './layout';
import Category from './view/Category';
import Clients from './view/Clients';
import Employees from './view/Employees';
import Persons from './view/Employees';
import Product from './view/Product';
import ProductAmount from './view/ProductAmount';
import Role from './view/Role';
import Workplace from './view/Workplace';

const App = () => {
	return (
		<Admin dataProvider={dataProvider} loginPage={LoginPage} layout={Layout} authProvider={authProvider}>
			<Resource name='Category' {...Category} />
			<Resource name='Clients' {...Clients} />
			<Resource name='Employees' {...Employees} />
			<Resource name='Persons' {...Persons} />
			<Resource name='Product' {...Product} />
			<Resource name='ProductAmount' {...ProductAmount} />
			<Resource name='Role' {...Role} />
			<Resource name='Workplace' {...Workplace} />
		</Admin>
	);
};

export default App;
