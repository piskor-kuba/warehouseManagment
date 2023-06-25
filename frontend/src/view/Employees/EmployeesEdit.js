import { useEffect, useState } from 'react';
import { Edit, SimpleForm, AutocompleteInput } from 'react-admin';

import axios from 'axios';
import endpoint from '../../endpoint';

export const EmployeesEdit = (props) => {
	const [role, setRole] = useState([]);
	const [workplace, setWorkplace] = useState([]);
	const [persons, setPersons] = useState([]);
	useEffect(() => {
		const fetchRole = async () => {
			await axios.get(`${endpoint.baseUrl}/role/`).then((resp) => {
				setRole(resp.data);
			});
		};
		const fetchWorkplace = async () => {
			await axios.get(`${endpoint.baseUrl}/workplace/`).then((resp) => {
				setWorkplace(resp.data);
			});
		};
		const fetchPersons = async () => {
			await axios.get(`${endpoint.baseUrl}/person/`).then((resp) => {
				setPersons(resp.data);
			});
		};
		fetchRole();
		fetchWorkplace();
		fetchPersons();
	}, []);

	const transform = (data) => ({
		id_persons: data['Name'],
		id_role: data['Role'],
		id_workplace: data['Workplace'],
	});

	return (
		<Edit {...props} transform={transform}>
			<SimpleForm>
				<AutocompleteInput source='Name' choices={persons} />
				<AutocompleteInput source='Role' choices={role} />
				<AutocompleteInput source='Workplace' choices={workplace} />
			</SimpleForm>
		</Edit>
	);
};
