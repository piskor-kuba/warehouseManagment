import { Edit, SimpleForm, TextInput } from 'react-admin';

export const ProductEdit = (props) => (
	<Edit {...props}>
		<SimpleForm>
			<TextInput disabled source='id' />
			<TextInput source='name' />
			<TextInput multiline source='describe' />
			<TextInput source='id_category' />
		</SimpleForm>
	</Edit>
);
