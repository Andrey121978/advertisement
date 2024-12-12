from flask import Flask, jsonify, request
from datetime import date
app = Flask(__name__)


ads = []
next_id = 1


@app.route('/ads', methods=['POST'])
def create_ad():
    global next_id
    data = request.json

    ad = {
        'id': next_id,
        'title': data['title'],
        'description': data['description'],
        'created_at': str(date.today()),
        'owner': data['owner'],
    }
    ads.append(ad)
    next_id += 1
    return jsonify(ad), 201


@app.route('/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    marker_find = 0
    for ad in ads:
        if ad['id'] == ad_id:
            marker_find = 1

            return jsonify(ad)

    if marker_find == 0:
        return jsonify({'message': 'Объявление не найдено'}), 404




@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    global ads
    marker_find = 0
    for ad in ads:
        if ad['id'] == ad_id:
            marker_find = 1
            ads.remove(ad)
    if marker_find == 1:
        return jsonify({'message': 'Объявление удалено'}), 200
    else:
        return jsonify({'message': 'Объявление не найдено'}), 404




if __name__ == '__main__':
    app.run()