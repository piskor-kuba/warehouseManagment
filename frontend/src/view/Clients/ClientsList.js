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
			<Datagrid>
				<TextField source='id' />
				<TextField source='id_persons' />
				<TextField source='amount' />
				<EditButton />
				<DeleteButton />
			</Datagrid>
		</List>
	);
};
