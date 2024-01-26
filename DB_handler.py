import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def login(self, id, pwd):
        pass
    
    def signin_verification(self, uid):
        users = self.db.child("users").get().val()
        for user in users:
            if uid == user:
                return False
        
        return True

    def signin(self, _id_, pwd, name, email):
        information = {
            "pwd" : pwd,
            "uname":name,
            "email":email
        }
        if self.signin_verification(_id_):
            self.db.child("users").child(_id_).set(information)
            return True
        else:
            return False
            
    

    def write_post(self, user, contents):
        pass

    def post_list(self):
        pass

    def post_detail(self, pid):
        pass

    def get_user(self, uid):
        pass

''' 댓글 기능도 추가 가능(스스로)'''