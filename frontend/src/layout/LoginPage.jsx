import * as React from 'react';
import { useLogin, useNotify, Notification } from 'react-admin';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { styled } from '@mui/material/styles';
import { cloudy } from '../assets/bgImage/cloudySVG';
import OtpInput from 'react-otp-input';

import axios from 'axios';
import endpoint from '../endpoint';

const validateEmail = (email) => {
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	return emailRegex.test(email);
};

const LoginPage = () => {
	const [username, setUsername] = React.useState('');
	const [password, setPassword] = React.useState('');
	const [id, setId] = React.useState(null);
	const [otp, setOtp] = React.useState('');
	const [codeOpen, setCodeOpen] = React.useState(false);
	const [disabled, setDisabled] = React.useState(false);
	const [registerFlag, setRegisterFlag] = React.useState(false);

	const login = useLogin();
	const notify = useNotify();

	const handleSubmit = (e) => {
		try {
			e.preventDefault();
			setDisabled(true);

			if (!validateEmail(username)) {
				throw new Error('Invalid email address.');
			}

			registerFlag
				? axios
						.post(endpoint.baseUrl + '/users/create', {
							login: username,
							password: password,
							id_employee: parseInt(id),
						})
						.then(() => {
							setUsername('');
							setPassword('');
							setId(null);
							setRegisterFlag(false);
							notify('Created new user.');
						})
						.catch(() => {
							setDisabled(false);
							setUsername('');
							setPassword('');
							setId(null);
							notify('Invalid username or password.');
						})
				: axios
						.post(endpoint.baseUrl + '/users/OTP_code', {
							username: username,
							password: password,
						})
						.then(() => {
							setCodeOpen(true);
						})
						.catch(() => {
							setDisabled(false);
							notify('Invalid username or password.');
						});
		} catch (e) {
			setOtp('');
			setCodeOpen(false);
			notify(
				e.response?.data
					? e.response.data.context.msg
					: e.response
					? `Error: ${e.response.status} ${e.response.statusText}`
					: e.message,
				{ type: 'error' },
				false
			);
		} finally {
			setDisabled(false);
		}
	};

	React.useEffect(() => {
		if (otp.length === 6) {
			login({ otp, username, password })
				.then(() => {
					notify('Hello my friend :)');
				})
				.catch(() => {
					notify('Invalid code');
				});
		}
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, [otp]);

	const handleRegisterClick = () => {
		setRegisterFlag(true);
	};

	const handleBack = () => {
		setRegisterFlag(false);
	};

	return (
		<Root>
			<BackgroundSVG />
			<Notification />
			<FormContainer onSubmit={handleSubmit}>
				<LoginForm>
					<LoginFormTitle>
						{registerFlag ? 'Register' : 'Sign In'}
					</LoginFormTitle>
					<LoginInput
						label='Username'
						variant='outlined'
						size='small'
						margin='normal'
						required
						value={username}
						disabled={disabled}
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
						disabled={disabled}
						onChange={(e) => setPassword(e.target.value)}
					/>
					{registerFlag && (
						<LoginInput
							label='ID'
							variant='outlined'
							size='small'
							margin='normal'
							type='number'
							required
							value={id}
							disabled={disabled}
							onChange={(e) => setId(e.target.value)}
						/>
					)}
					{codeOpen ? (
						<>
							<div>Client code:</div>
							<OtpInput
								value={otp}
								onChange={setOtp}
								numInputs={6}
								renderSeparator={<span>&nbsp;&nbsp;</span>}
								renderInput={(props) => (
									<input {...props} style={{ width: 20, height: 30 }} />
								)}
							/>
						</>
					) : null}
					<LoginButton
						variant='contained'
						color='primary'
						type='submit'
						disabled={disabled}>
						{registerFlag ? 'Register' : 'Sign In'}
					</LoginButton>
					{!codeOpen && !registerFlag && (
						<RegisterButton
							variant='text'
							color='primary'
							disabled={disabled}
							onClick={handleRegisterClick}>
							Register
						</RegisterButton>
					)}
					{registerFlag && (
						<BackButton
							variant='text'
							color='primary'
							disabled={disabled}
							onClick={handleBack}>
							Back
						</BackButton>
					)}
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

const RegisterButton = styled(Button)({
	width: '100%',
	marginTop: '16px',
});

const BackButton = styled(Button)({
	width: '100%',
	marginTop: '16px',
});

export default LoginPage;
