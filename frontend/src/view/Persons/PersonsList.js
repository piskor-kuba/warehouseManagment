import {
	List,
	Datagrid,
	TextField,
	EditButton,
	DeleteButton,
} from 'react-admin';

export const PersonsList = (props) => {
	return (
		<List {...props}>
			<Datagrid bulkActionButtons={false}>
				<TextField source='id' />
				<TextField source='name' />
				<TextField source='surname' />
				<TextField source='phone' />
				<TextField source='address' />
				<EditButton />
				<DeleteButton />
			</Datagrid>
		</List>
	);
};
