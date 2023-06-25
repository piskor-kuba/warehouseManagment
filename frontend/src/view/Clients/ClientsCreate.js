import { useEffect, useState } from 'react';
import {
	SimpleForm,
	Create,
	NumberInput,
	number,
	AutocompleteInput,
} from 'react-admin';
import axios from 'axios';
import endpoint from '../../endpoint';

export const ClientsCreate = (props) => {
	const [persons, setPersons] = useState([]);
	useEffect(() => {
		const fetchPersons = async () => {
			await axios.get(`${endpoint.baseUrl}/person/`).then((resp) => {
				setPersons(resp.data);
			});
		};
		fetchPersons();
	}, []);

	return (
		<Create {...props}>
			<SimpleForm>
				<AutocompleteInput source='id_persons' choices={persons} />
				<NumberInput source='amount' validate={number} />
			</SimpleForm>
		</Create>
	);
};
