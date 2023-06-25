import {
	SimpleForm,
	TextInput,
	NumberInput,
	Create,
	number,
} from 'react-admin';

export const ProductCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<NumberInput source='id' number={number} />
			<TextInput source='name' required />
			<TextInput multiline source='describe' />
			<TextInput source='amount' required />
			<NumberInput source='id_category' number={number} required />
		</SimpleForm>
	</Create>
);
