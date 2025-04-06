import hashlib

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()
        print(self.name, 'user created')
    @staticmethod
    def log_in(self, email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()
        
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if stored_password == hashed_password:
            print('Valid User')
            # print('Password Found', stored_password)
        else:
            print('Invalid User')   
                    

tanvir = User('Tanvir Ahammed', 'tanvir@gmail.com', 'manisman')
tanvir.log_in('tanvir@gmail.com', 'manisman')