import { List, Datagrid, TextField, EditButton } from 'react-admin';

export const PersonsList = (props) => (
	<List {...props}>
		<Datagrid>
			<TextField source='id' />
			<TextField source='title' />
			<EditButton />
		</Datagrid>
	</List>
);
