import { SimpleForm, TextInput, Create } from 'react-admin';

export const EmployeesCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<TextInput source='title' />
			<TextInput multiline source='body' />
		</SimpleForm>
	</Create>
);
