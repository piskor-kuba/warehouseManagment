import {
	List,
	Datagrid,
	TextField,
	EditButton,
	DeleteButton,
} from 'react-admin';

export const EmployeesList = (props) => (
	<List {...props}>
		<Datagrid bulkActionButtons={false}>
			<TextField source='id' />
			<TextField source='Name' />
			<TextField source='Role' />
			<TextField source='Workplace' />
			<EditButton />
			<DeleteButton />
		</Datagrid>
	</List>
);
