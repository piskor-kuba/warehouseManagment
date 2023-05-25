// Menu.js
import React from 'react';
import { MenuItemLink, useGetList } from 'react-admin';

const Menu = ({ onMenuClick, logout }) => {
	const { data: resources } = useGetList('resources', { perPage: -1 });
	console.log(resources);

	return (
		<div>
			{/* {resources?.map((resource) => (
				<MenuItemLink
					key={resource.name}
					to={`/${resource.name}`}
					primaryText={resource.options.label}
					onClick={onMenuClick}
				/>
			))} */}
			<MenuItemLink
				to='/Category'
				primaryText='Category'
				onClick={onMenuClick}
			/>
			<MenuItemLink to='/Clients' primaryText='Clients' onClick={onMenuClick} />
			<MenuItemLink
				to='/Employees'
				primaryText='Employees'
				onClick={onMenuClick}
			/>
			<MenuItemLink to='/Persons' primaryText='Persons' onClick={onMenuClick} />
			<MenuItemLink to='/Product' primaryText='Product' onClick={onMenuClick} />
			<MenuItemLink to='/logout' primaryText='Logout' onClick={logout} />
		</div>
	);
};

export default Menu;
