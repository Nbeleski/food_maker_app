from datetime import datetime

from main import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200))
    permissions = db.Column(db.Integer, default=1)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %s>' % self.username

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'last_login')
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)