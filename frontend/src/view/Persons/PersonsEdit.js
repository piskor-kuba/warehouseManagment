import { Edit, SimpleForm, TextInput } from 'react-admin';

export const PersonsEdit = (props) => (
	<Edit {...props}>
		<SimpleForm>
			<TextInput source='id' />
			<TextInput source='name' />
			<TextInput source='surname' />
			<TextInput source='phone' />
			<TextInput source='address' />
		</SimpleForm>
	</Edit>
);
