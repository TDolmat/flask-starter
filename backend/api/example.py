from flask import Blueprint, request, jsonify
from core.config import CONFIG
from core.models import User, db
from http import HTTPStatus

bp = Blueprint('/', __name__, url_prefix='')

@bp.route('/', methods=('GET', 'POST'))
def example():
    return jsonify({
        'message': 'Hello, World!',
    })


@bp.route('/config', methods=('GET', 'POST'))
def config():
    return jsonify({
        'config': CONFIG._asdict()
    }, HTTPStatus.OK)


"""
[FOR TESTING POST REQUEST]

curl -X POST \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john.doe@example.com"}' \
http://localhost:5001/users
"""
@bp.route('/users', methods=('GET', 'POST'))
def users():
    if request.method == 'GET': 
        users = User.query.all()
        return [
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
            }
            for user in users
        ], HTTPStatus.OK

    elif request.method == 'POST':
        data = request.get_json()        
        user = User(name=data['name'], email=data['email'])

        db.session.add(user)
        db.session.commit()
        
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
        }, HTTPStatus.CREATED

