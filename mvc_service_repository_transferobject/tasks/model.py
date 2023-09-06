from mvc_service_repository_transferobject.extensions import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(
        db.String(160), unique=False, nullable=True, default=''
    )
    status = db.Column(
        db.String(20), unique=False, nullable=False, default='TODO'
    )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, description, status, user_id):
        self.title = title
        self.description = description
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return f'<Task {self.id} | {self.user_id} | {self.title} | >'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'user_id': self.user_id,
        }

    def from_dict(self, data):
        for field in ['id', 'title', 'description', 'status', 'user_id']:
            if field in data:
                setattr(self, field, data[field])
