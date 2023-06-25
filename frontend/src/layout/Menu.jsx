// Menu.js
import React from 'react';
import { MenuItemLink } from 'react-admin';

const Menu = ({ onMenuClick }) => {
	return (
		<>
			<MenuItemLink
				to='/category'
				primaryText='Category'
				onClick={onMenuClick}
			/>
			<MenuItemLink to='/clients' primaryText='Clients' onClick={onMenuClick} />
			<MenuItemLink
				to='/employee'
				primaryText='Employee'
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
		</>
	);
};

export default Menu;
