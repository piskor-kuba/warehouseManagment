import { Edit, SimpleForm, TextInput, NumberInput } from 'react-admin';

export const EmployeesEdit = (props) => (
	<Edit {...props}>
		<SimpleForm>
			<TextInput disabled source='id' />
			<NumberInput source='id_persons' />
			<NumberInput source='id_role' />
			<NumberInput source='id_workplace' />
		</SimpleForm>
	</Edit>
);
