import { Edit, SimpleForm, TextInput } from 'react-admin';

export const RoleEdit = (props) => (
	<Edit {...props}>
		<SimpleForm>
			<TextInput disabled source='id' />
			<TextInput source='name' />
		</SimpleForm>
	</Edit>
);
