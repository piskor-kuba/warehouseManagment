import { SimpleForm, TextInput, Create } from 'react-admin';

export const CategoryCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<TextInput source='name' required />
		</SimpleForm>
	</Create>
);
