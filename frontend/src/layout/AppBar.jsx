// AppBar.js
import React from 'react';
import { AppBar as RaAppBar } from 'react-admin';
import Typography from '@mui/material/Typography';

const AppBar = (props) => (
	<RaAppBar {...props}>
		<Typography variant='h6' color='inherit' id='react-admin-title' />
	</RaAppBar>
);

export default AppBar;
