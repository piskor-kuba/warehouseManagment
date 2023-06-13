import { SimpleForm, NumberInput, Create } from 'react-admin';

export const EmployeesCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<NumberInput source='id_persons' />
			<NumberInput source='id_role' />
			<NumberInput source='id_workplace' />
		</SimpleForm>
	</Create>
);
