import { useEffect, useState } from 'react';

import {
	SimpleForm,
	NumberInput,
	Create,
	AutocompleteInput,
} from 'react-admin';
import axios from 'axios';
import endpoint from '../../endpoint';

export const EmployeesCreate = (props) => {
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

	return (
		<Create {...props}>
			<SimpleForm>
				<AutocompleteInput source='id_persons' choices={persons} />
				<AutocompleteInput source='id_role' choices={role} />
				<AutocompleteInput source='id_workplace' choices={workplace} />
			</SimpleForm>
		</Create>
	);
};
