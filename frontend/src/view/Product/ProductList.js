import { List, Datagrid, TextField, EditButton } from 'react-admin';

export const ProductList = (props) => (
	<List {...props}>
		<Datagrid>
			<TextField source='id' />
			<TextField source='name' />
			<TextField source='describe' />
			<TextField source='id_category' />
			<EditButton />
		</Datagrid>
	</List>
);
