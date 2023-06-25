import { Edit, SimpleForm, TextInput } from 'react-admin';

export const CategoryEdit = (props) => (
	<Edit {...props}>
		<SimpleForm>
			<TextInput disabled source='id' />
			<TextInput source='name' required />
		</SimpleForm>
	</Edit>
);
