import { useEffect, useState } from 'react';
import { Edit, SimpleForm, TextInput, AutocompleteInput } from 'react-admin';
import axios from 'axios';
import endpoint from '../../endpoint';

export const ClientsEdit = (props) => {
	const [persons, setPersons] = useState([]);
	useEffect(() => {
		const fetchPersons = async () => {
			await axios.get(`${endpoint.baseUrl}/person/`).then((resp) => {
				setPersons(resp.data);
			});
		};
		fetchPersons();
	}, []);

	const transform = (data) => ({
		id_persons: data['Name'],
		amount: data['Amount'],
	});
	return (
		<Edit {...props} transform={transform}>
			<SimpleForm>
				<AutocompleteInput source='Name' choices={persons} />
				<TextInput source='Amount' />
			</SimpleForm>
		</Edit>
	);
};
