import { SimpleForm, TextInput, NumberInput, Create } from 'react-admin';

export const ProductCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<NumberInput source='id' />
			<TextInput source='name' />
			<TextInput multiline source='describe' />
			<TextInput source='amount' />
			<NumberInput source='id_category' />
		</SimpleForm>
	</Create>
);
