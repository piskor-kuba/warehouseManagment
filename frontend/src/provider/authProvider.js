import endpoint from '../endpoint';

export const authProvider = {
	login: ({ username, password }) => {
		const request = new Request(endpoint.baseUrl, {
			method: 'POST',
			body: JSON.stringify({ username, password }),
			headers: new Headers({ 'Content-Type': 'application/json' }),
		});
		return fetch(request)
			.then((response) => {
				if (response.status < 200 || response.status >= 300) {
					throw new Error(response.statusText);
				}
				return response.json();
			})
			.then(({ token }) => {
				localStorage.setItem('token', token);
			});
	},
	logout: () => {
		localStorage.removeItem('token');
		return Promise.resolve();
	},
	checkError: () => Promise.resolve(),
	checkAuth: () => {
		return localStorage.getItem('token') ? Promise.resolve() : Promise.reject();
	},
	getPermissions: () => Promise.resolve(),
};
