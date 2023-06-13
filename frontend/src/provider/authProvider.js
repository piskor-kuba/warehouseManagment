import axios from 'axios';
import endpoint from '../endpoint';

export const authProvider = {
	login: async ({ otp, username, password }) => {
		const headers = {
			accept: 'application/json',
			'Content-Type': 'application/x-www-form-urlencoded',
		};
		const data = new URLSearchParams();
		data.append('grant_type', '');
		data.append('username', username);
		data.append('password', password);
		data.append('scope', '');
		data.append('client_id', '');
		data.append('client_secret', otp);

		try {
			const response = await axios.post(
				endpoint.baseUrl + '/users/token',
				data,
				{ headers }
			);
			localStorage.setItem('token', response.data.access_token);
			return Promise.resolve();
		} catch (error) {
			return Promise.reject();
		}
	},
	logout: () => {
		localStorage.removeItem('token');
		return Promise.resolve();
	},
	checkError: ({ status }) => {
		if (status === 401 || status === 403) {
			localStorage.removeItem('token');
			return Promise.reject();
		}
		return Promise.resolve();
	},
	checkAuth: () => {
		return localStorage.getItem('token') ? Promise.resolve() : Promise.reject();
	},
	getPermissions: () => Promise.resolve(),
};
