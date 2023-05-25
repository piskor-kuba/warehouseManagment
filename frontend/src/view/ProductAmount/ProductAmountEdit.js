import { Edit, SimpleForm, TextInput } from 'react-admin';

export const ProductAmountEdit = (props) => (
	<Edit {...props}>
		<SimpleForm>
			<TextInput disabled source='id' />
			<TextInput source='title' />
			<TextInput multiline source='body' />
		</SimpleForm>
	</Edit>
);
