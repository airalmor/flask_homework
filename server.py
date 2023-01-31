from flask import Flask, jsonify, request
from flask.views import MethodView
from database import Session, AdvertModel
from errors import HttpExeption

app = Flask('app')


@app.errorhandler(HttpExeption)
def error_handler(error: HttpExeption):
    http_responce = jsonify({
        'status': 'error',
        'message': error.message
    })
    http_responce.status_code = error.status_code
    return http_responce


def get_advert(advert_id: int, session: Session) -> AdvertModel:
    advert = session.query(AdvertModel).get(advert_id)
    if advert is None:
        raise HttpExeption(
            status_code=404,
            message='advert not found'
        )
    return advert


class Advert(MethodView):

    def get(self, advert_id: int):
        with Session() as session:
            advert = get_advert(advert_id, session)

            return jsonify({
                'id': advert.id,
                'title': advert.advert_title,
                'text': advert.advert_text,
                'creation_time': advert.creation_time.isoformat(),
                'owner': advert.owner_name
            })

    def post(self):
        advert_data = request.json

        with Session() as session:
            new_advert = AdvertModel(**advert_data)
            session.add(new_advert)
            session.commit()
            return jsonify({'id': new_advert.id})

    def delete(self, advert_id: int):
        with Session() as session:
            advert = get_advert(advert_id, session)
            session.delete(advert)
            session.commit()
            return jsonify({'status': 'success'})


app.add_url_rule('/adverts/<int:advert_id>', view_func=Advert.as_view('adverts'), methods=['GET', 'DELETE'])
app.add_url_rule('/adverts/', view_func=Advert.as_view('create_advert'), methods=['POST'])

if __name__ == '__main__':
    app.run()
