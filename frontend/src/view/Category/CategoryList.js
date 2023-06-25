import {
	List,
	Datagrid,
	TextField,
	EditButton,
	DeleteButton,
} from 'react-admin';

export const CategoryList = (props) => (
	<List {...props}>
		<Datagrid bulkActionButtons={false}>
			<TextField source='id' />
			<TextField source='name' />
			<EditButton />
			<DeleteButton />
		</Datagrid>
	</List>
);
