// Menu.js
import React from 'react';
import { MenuItemLink, useGetList } from 'react-admin';

const Menu = ({ onMenuClick, logout }) => {
	const { data: resources } = useGetList('resources', { perPage: -1 });

	return (
		<div>
			{resources?.map((resource) => (
				<MenuItemLink
					key={resource.name}
					to={`/${resource.name}`}
					primaryText={resource.options.label}
					onClick={onMenuClick}
				/>
			))}
			<MenuItemLink
				to='/custom-route'
				primaryText='Custom Route'
				onClick={onMenuClick}
			/>
			<MenuItemLink to='/logout' primaryText='Logout' onClick={logout} />
		</div>
	);
};

export default Menu;
