import {
	SimpleForm,
	TextInput,
	Create,
} from 'react-admin';

export const PostCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<TextInput source='title' />
			<TextInput multiline source='body' />
		</SimpleForm>
	</Create>
);
