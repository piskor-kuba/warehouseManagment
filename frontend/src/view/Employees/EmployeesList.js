import {
	List,
	Datagrid,
	TextField,
	EditButton,
	DeleteButton,
} from 'react-admin';

export const EmployeesList = (props) => (
	<List {...props}>
		<Datagrid>
			<TextField source='id' />
			<TextField source='id_persons' />
			<TextField source='id_role' />
			<TextField source='id_workplace' />
			<EditButton />
			<DeleteButton />
		</Datagrid>
	</List>
);
