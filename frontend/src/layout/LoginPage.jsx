import * as React from 'react';
import { useLogin, useNotify, Notification } from 'react-admin';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { styled } from '@mui/material/styles';
import { cloudy } from '../assets/bgImage/cloudySVG';

const LoginPage = () => {
	const [username, setUsername] = React.useState('');
	const [password, setPassword] = React.useState('');
	const login = useLogin();
	const notify = useNotify();

	const handleSubmit = (e) => {
		e.preventDefault();
		login({ username, password }).catch(() =>
			notify('Invalid username or password')
		);
	};

	return (
		<Root>
			<BackgroundSVG />
			<Notification />
			<FormContainer onSubmit={handleSubmit}>
				<LoginForm>
					<LoginFormTitle>Sign In</LoginFormTitle>
					<LoginInput
						label='Username'
						variant='outlined'
						size='small'
						margin='normal'
						required
						value={username}
						onChange={(e) => setUsername(e.target.value)}
					/>
					<LoginInput
						label='Password'
						variant='outlined'
						size='small'
						margin='normal'
						type='password'
						required
						value={password}
						onChange={(e) => setPassword(e.target.value)}
					/>
					<LoginButton variant='contained' color='primary' type='submit'>
						Sign In
					</LoginButton>
				</LoginForm>
			</FormContainer>
		</Root>
	);
};
const BackgroundSVG = styled('div')({
	position: 'absolute',
	top: 0,
	left: 0,
	width: '100%',
	height: '100%',
	backgroundRepeat: 'no-repeat',
	backgroundPosition: 'center',
	backgroundSize: 'cover',
	backgroundImage: `url("${cloudy}")`,
});

const Root = styled('div')({
	display: 'flex',
	justifyContent: 'center',
	alignItems: 'center',
	minHeight: '100vh',
});

const FormContainer = styled('div')({
	display: 'flex',
	justifyContent: 'center',
});

const LoginForm = styled('form')({
	display: 'flex',
	flexDirection: 'column',
	alignItems: 'center',
	padding: '32px',
	border: '1px solid rgba(0, 0, 0, 0.1)',
	borderRadius: '8px',
	backgroundColor: '#fff',
	boxShadow: '0px 8px 16px rgba(0, 0, 0, 0.1)',
	zIndex: 1,
	minWidth: '20vw',
});

const LoginFormTitle = styled('h1')({
	margin: 0,
	marginBottom: '32px',
});

const LoginInput = styled(TextField)({
	width: '100%',
});

const LoginButton = styled(Button)({
	width: '100%',
	marginTop: '32px',
});

export default LoginPage;
