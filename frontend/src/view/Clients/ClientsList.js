import { List, Datagrid, TextField, EditButton } from 'react-admin';

export const ClientsList = (props) => {
	return (
		<List {...props}>
			<Datagrid>
				<TextField source='id' />
				<TextField source='id_persons' />
				<TextField source='amount' />
				<EditButton />
			</Datagrid>
		</List>
	);
};
