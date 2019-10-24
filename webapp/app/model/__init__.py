

def init_model(sqlDAO):
    from .UserModel import User
    sqlDAO.create_all()
