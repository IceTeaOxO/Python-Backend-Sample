from app.models import User
from app import db

# Function to Get Users
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'createAt':user.created_at} for user in users]
    return user_list

# Function to Create User
def create_user(user_data):
    new_user = User(username=user_data['username'], email=user_data['email'])
    db.session.add(new_user)
    db.session.commit()
    return {'id': new_user.id, 'username': new_user.username}
