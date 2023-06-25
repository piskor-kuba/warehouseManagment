import {
	List,
	Datagrid,
	TextField,
	EditButton,
	DeleteButton,
} from 'react-admin';

export const RoleList = (props) => (
	<List {...props}>
		<Datagrid bulkActionButtons={false}>
			<TextField source='id' />
			<TextField source='name' />
			<EditButton />
			<DeleteButton />
		</Datagrid>
	</List>
);
