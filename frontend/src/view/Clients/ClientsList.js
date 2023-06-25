import {
	List,
	Datagrid,
	TextField,
	EditButton,
	DeleteButton,
} from 'react-admin';

export const ClientsList = (props) => {
	return (
		<List {...props}>
			<Datagrid bulkActionButtons={false}>
				<TextField source='id' />
				<TextField source='Name' />
				<TextField source='Amount' />
				<EditButton />
				<DeleteButton />
			</Datagrid>
		</List>
	);
};
