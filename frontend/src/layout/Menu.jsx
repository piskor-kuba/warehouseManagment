// Menu.js
import React from 'react';
import { MenuItemLink } from 'react-admin';

const Menu = ({ onMenuClick }) => {
	return (
		<div>
			{/* <MenuItemLink
				to='/dashboard'
				primaryText='Dashboard'
				onClick={onMenuClick}
			/> */}
			<MenuItemLink
				to='/category'
				primaryText='Category'
				onClick={onMenuClick}
			/>
			<MenuItemLink to='/clients' primaryText='Clients' onClick={onMenuClick} />
			<MenuItemLink
				to='/employees'
				primaryText='Employees'
				onClick={onMenuClick}
			/>
			<MenuItemLink to='/persons' primaryText='Persons' onClick={onMenuClick} />
			<MenuItemLink to='/product' primaryText='Product' onClick={onMenuClick} />
			<MenuItemLink
				to='/workplace'
				primaryText='Workplace'
				onClick={onMenuClick}
			/>
			<MenuItemLink to='/role' primaryText='Role' onClick={onMenuClick} />
		</div>
	);
};

export default Menu;
