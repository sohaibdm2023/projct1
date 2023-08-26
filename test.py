class User :
    id=0
    def __init__(self,name,passw):
        self.name=name
        self.pasw=passw
        self.id= User.id
        User.id+=1
    @staticmethod
    def user_info():
        print(f"id method {User.id}")
user1=User("sohaib",2020)
User.user_info()
print(user1.id,":",user1.name)
user2=User("yhya",1999)
User.user_info()
print(user2.id,":",user2.name)
user3=User("dada :",1000)
User.user_info()
print(user3.id,user3.name)
user1.user_info()
print('Hello World')