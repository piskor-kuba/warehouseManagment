// Layout.js
import React from 'react';
import { Layout as RaLayout, Sidebar } from 'react-admin';
import Menu from './Menu';
import AppBar from './AppBar';

const Layout = (props) => (
	<RaLayout
		{...props}
		appBar={AppBar}
		sidebar={Sidebar}
		menu={Menu}
	/>
);

export default Layout;
