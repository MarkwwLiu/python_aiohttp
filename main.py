import aiohttp
import asyncio


test_url = 'https://www.bitopro.com/ns/home'

def do_requests(session):
    return session.get(test_url)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(0, 10):
            tasks.append(do_requests(session))

        results = await asyncio.gather(*tasks)
        for r in results:
            print('{0} =>'.format(test_url), r.status)

if __name__ == '__main__':
    asyncio.run(main())
