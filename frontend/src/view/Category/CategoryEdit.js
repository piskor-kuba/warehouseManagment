import { Edit, SimpleForm, TextInput } from 'react-admin';

export const CategoryEdit = (props) => (
	<Edit {...props}>
		<SimpleForm>
			<TextInput disabled source='id' />
			<TextInput source='title' />
			<TextInput multiline source='body' />
		</SimpleForm>
	</Edit>
);
