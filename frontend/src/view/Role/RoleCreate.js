import { SimpleForm, TextInput, Create } from 'react-admin';

export const RoleCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<TextInput source='name' />
		</SimpleForm>
	</Create>
);
