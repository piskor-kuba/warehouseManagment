import { SimpleForm, Create, NumberInput } from 'react-admin';

export const ClientsCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<NumberInput source='id_persons' />
			<NumberInput source='amount' />
		</SimpleForm>
	</Create>
);
