
class UserConfigs():
    def __init__(self):
        self.__user = 'NINOMAL'
        self.__password = 'ADMIN'
        self.__dns = 'localhost:1521/XEPDB1'

    def getUser(self):
        return self.__user
    
    def getPassword(self):
        return self.__password
    
    def getDns(self):
        return self.__dns