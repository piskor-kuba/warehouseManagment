import { Edit, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const ClientsEdit = (props) => (
	<Edit {...props}>
		<SimpleForm>
			<NumberInput disabled source='id' />
			<NumberInput source='id_persons' />
			<TextInput source='amount' />
		</SimpleForm>
	</Edit>
);
