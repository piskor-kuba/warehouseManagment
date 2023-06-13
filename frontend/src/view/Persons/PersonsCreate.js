import { SimpleForm, TextInput, Create } from 'react-admin';

export const PersonsCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<TextInput source='name' />
			<TextInput source='surname' />
			<TextInput source='phone' />
			<TextInput source='address' />
		</SimpleForm>
	</Create>
);
