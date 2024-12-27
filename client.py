
import aiohttp
import asyncio

async def main():
    async with (aiohttp.ClientSession() as session):
        response1 = await session.post("http://127.0.0.1:8080/ads", json={
        'title': 'Продам квартиру',
        'description': 'Продам однокомнатную квартиру',
        'owner': 'Андрей',
    })
        response2 = await session.post("http://127.0.0.1:8080/ads", json={
            'title': 'Продам авто',
            'description': 'Продам отечественное авто',
            'owner': 'Иван',
        })

        response3 = await session.post("http://127.0.0.1:8080/ads", json={
            'title': 'Продам электропилу',
            'description': 'Продам торцовочную пилу',
            'owner': 'Алексей',
        })


        response_get = await session.get("http://127.0.0.1:8080/ads/2")
        print(response_get)


        response_delete = await session.delete("http://127.0.0.1:8080/ads/2")
        print(response_delete)

# Запуск основной асинхронной функции
if __name__ == '__main__':
    asyncio.run(main())