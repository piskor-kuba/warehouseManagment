import { Admin, Resource } from 'react-admin';
import { authProvider } from './provider/authProvider';
import { Layout, LoginPage } from './layout';
import Posts from './view/Posts';

const App = () => {
	return (
		<Admin authProvider={authProvider} loginPage={LoginPage} layout={Layout}>
			<Resource name='posts' {...Posts} />
		</Admin>
	);
};

export default App;
