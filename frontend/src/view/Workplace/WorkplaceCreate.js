import { SimpleForm, TextInput, Create } from 'react-admin';

export const WorkplaceCreate = (props) => (
	<Create {...props}>
		<SimpleForm>
			<TextInput multiline source='name' label='Name of workplace' />
		</SimpleForm>
	</Create>
);
