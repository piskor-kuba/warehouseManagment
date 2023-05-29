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

		axios
			.post(endpoint.baseUrl + '/users/token', data, { headers })
			.then(({ data }) => {
				localStorage.setItem('token', data.access_token);
				// window.location.href = '#/dashboard';
				return Promise.resolve();
			})
			.catch(() => {});
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
