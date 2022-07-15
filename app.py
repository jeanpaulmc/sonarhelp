from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy import sql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:melendez2016@localhost:5432/examenparcial'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Publisher(db.Model):
    __tablename__ = 'publisher'
    id_a = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(80), nullable=False)
    topic = db.Column(db.String(80), nullable=False)
    estatus = db.Column(db.Boolean, nullable=False)


class Subscriber(db.Model):
    __tablename__ = 'subscriber'
    id_a = db.Column(db.Integer, primary_key=True)
    mirar_mensaje = db.Column(db.String(80), nullable=False)
    mirar_topic = db.Column(db.String(10), nullable=False)


db.create_all()


@app.route('/publisher', methods=['POST'])
def authenticate_data():
    error = False
    response = {}
    try:

        comando = request.get_json()[type]
        id_a = request.get_json()['id_a']
        mensaje = request.get_json()['mensaje']
        topic = request.get_json()['topic']
        estatus = request.get_json()['estatus']
        db.session.query(Publisher).filter(Publisher.id_a == id_a).filter(
            Publisher.mensaje == mensaje).filter(Publisher.topic == topic).filter(Publisher.estatus == estatus)
        response['type'] = comando

    except FileNotFoundError:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        response['error_message'] = "no existe el usuario"
    response['error'] = error
    return jsonify(response)


@app.route('/subscriber', methods=['GET'])
def response_data():
    error = False
    response = {}
    try:

        comando2 = request.get_json()[type]
        id_a = request.get_json()['id_a']
        mirar_mensaje = request.get_json()['mirar_mensaje']
        mirar_topic = request.get_json()['mirar_topic']
        db.session.query(Publisher).filter(Subscriber.id_a == id_a).filter(
            Subscriber.mirar_mensaje == mirar_mensaje).filter(Subscriber.mirar_topic == mirar_topic)
        response['type'] = comando2

    except FileNotFoundError:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        response['error_message'] = "no existe el usuario"
    response['error'] = error
    return jsonify(response)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5003, debug=True)
else:
    print('using global variables from FLASK')
