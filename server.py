from aiohttp import web
from datetime import date

ads = []
next_id = 1


async def create_ad(request):
    global next_id
    data = await request.json()

    ad = {
        'id': next_id,
        'title': data['title'],
        'description': data['description'],
        'created_at': str(date.today()),
        'owner': data['owner'],
    }
    ads.append(ad)
    next_id += 1
    return web.json_response(ad, status=201)


async def get_ad(request):
    ad_id = int(request.match_info['ad_id'])
    for ad in ads:
        if ad['id'] == ad_id:
            return web.json_response(ad)

    return web.json_response({'message': 'Объявление не найдено'}, status=404)


async def delete_ad(request):
    global ads
    ad_id = int(request.match_info['ad_id'])
    for ad in ads:
        if ad['id'] == ad_id:
            ads.remove(ad)
            return web.json_response({'message': 'Объявление удалено'}, status=200)

    return web.json_response({'message': 'Объявление не найдено'}, status=404)


app = web.Application()
app.router.add_post('/ads', create_ad)
app.router.add_get('/ads/{ad_id}', get_ad)
app.router.add_delete('/ads/{ad_id}', delete_ad)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)