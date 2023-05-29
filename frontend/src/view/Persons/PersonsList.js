import { List, Datagrid, TextField, EditButton } from 'react-admin';

export const PersonsList = (props) => {
	return (
		<List {...props}>
			<Datagrid>
				<TextField source='id' />
				<TextField source='name' />
				<TextField source='surname' />
				<TextField source='phone' />
				<TextField source='address' />
				<EditButton />
			</Datagrid>
		</List>
	);
};
