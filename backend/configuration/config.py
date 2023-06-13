import yaml

class Config:
    def __init__(self):
        try:

            with open('configuration/config.yaml','r') as yml: #configuration/config.yaml
                self.__configuration = yaml.safe_load(yml)
        except FileNotFoundError as e:
            print(f"Problem with config file [ERROR NUMBER: {e.errno}]")
    @property
    def config(self):
        return self.__configuration

class Authorization(Config):
    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        raise AttributeError

    @property
    def key(self):
        return self.config['configuration']['authorization']['secretKey']

    @property
    def algorithm(self):
        return self.config['configuration']['authorization']['algorithm']

    @property
    def emailRegex(self):
        return self.config['configuration']['authorization']['emailRegex']

class F2a(Config):
    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        raise AttributeError

    @property
    def key(self):
        return self.config['configuration']['f2a']['secretKey']

    @property
    def password(self):
        return self.config['configuration']['f2a']['password']

    @property
    def email(self):
        return self.config['configuration']['f2a']['email']

    @property
    def emailBody(self):
        return self.config['configuration']['f2a']['emailBody']

    @property
    def emailSubject(self):
        return self.config['configuration']['f2a']['emailSubject']

    @property
    def smtpServer(self):
        return self.config['configuration']['f2a']['smtpServer']

class AuthorizationBlocker(Config):
    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        raise AttributeError

    @property
    def attempts(self):
        return self.config['configuration']['authorizationBlocker']['attempts']

    @property
    def time(self):
        return self.config['configuration']['authorizationBlocker']['time']

class Database(Config):
    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        raise AttributeError

    @property
    def url(self):
        return str(self.config['configuration']['database']['url'])

class Server(Config):
    def __init__(self):
        super().__init__()

    def __getattr__(self, item):
        raise AttributeError

    @property
    def host(self):
        return self.config['configuration']['server']['host']

    @property
    def port(self):
        return self.config['configuration']['server']['port']
