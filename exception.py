class User:
    def decorate(method):
        def wrapper(self):
            if method == self.get_account_balance:
                try:
                    method(self)
                except Exception as e:
                    print("No username defined!")
            else:
                try:
                    method(self)
                except Exception as e:
                    print('No password to change')
        return wrapper

    @decorate
    def get_account_balance(self):
        print('get account balance')

    @decorate
    def change_password(self):
        print('change password')

u = User()
u.change_password()