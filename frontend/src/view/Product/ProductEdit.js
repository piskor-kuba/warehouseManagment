import { useEffect, useState } from 'react';
import {
	Edit,
	SimpleForm,
	TextInput,
	AutocompleteInput,
	maxLength,
} from 'react-admin';
import axios from 'axios';
import endpoint from '../../endpoint';

export const ProductEdit = (props) => {
	const [category, setCategory] = useState([]);
	useEffect(() => {
		const fetchCategory = async () => {
			await axios.get(`${endpoint.baseUrl}/category/`).then((resp) => {
				setCategory(resp.data);
			});
		};
		fetchCategory();
	}, []);

	const transform = (data) => ({
		name: data['product_name'],
		describe: data['describe'],
		id_category: data['category'],
	});

	return (
		<Edit {...props} transform={transform}>
			<SimpleForm>
				<TextInput source='product_name' validate={maxLength(20)} />
				<TextInput multiline source='describe' validate={maxLength(50)} />
				<AutocompleteInput source='category' choices={category} />
			</SimpleForm>
		</Edit>
	);
};
