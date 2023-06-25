import {
	List,
	Datagrid,
	TextField,
	EditButton,
	DeleteButton,
} from 'react-admin';

export const ProductList = (props) => (
	<List {...props}>
		<Datagrid bulkActionButtons={false}>
			<TextField source='id' />
			<TextField source='product_name' />
			<TextField source='category' />
			<TextField source='describe' />
			<EditButton />
			<DeleteButton />
		</Datagrid>
	</List>
);
