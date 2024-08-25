from main import Session,engine,User


local_session=Session(bind=engine)

user_to_update=local_session.query(User).filter(User.username == 'jack').first()

user_to_update.username = "gopal"
user_to_update.email="baniyaji@company.com"

local_session.commit()