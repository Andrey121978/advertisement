import requests



response1 = requests.post("http://127.0.0.1:5000/ads",
    json = {
        'title': 'Продам квартиру',
        'description': 'Продам однокомнатную квартиру',
        'owner': 'Андрей',
    }
        )
response2 = requests.post("http://127.0.0.1:5000/ads",
    json = {
        'title': 'Продам авто',
        'description': 'Продам отечественное авто',
        'owner': 'Иван',
    }
        )
response3 = requests.post("http://127.0.0.1:5000/ads",
    json = {
        'title': 'Продам электропилу',
        'description': 'Продам торцовочную пилу',
        'owner': 'Алексей',
    }
        )
response_get = requests.get("http://127.0.0.1:5000/ads/2")


response_delete = requests.delete("http://127.0.0.1:5000/ads/2")
