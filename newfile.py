import asyncio
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession


def visit_website(url):
    try:
        with FuturesSession(max_workers=10) as session:
            future = session.get(url, verify=False)
            # Просто открываем сайт, без обработки ответа
            pass
    except Exception as e:
        print(f"Error visiting {url}: {e}")

async def main(num_task, url):
    while True:
        with ThreadPoolExecutor(max_workers=num_tasks) as executor:
            tasks = [executor.submit(visit_website, url) for _ in range(num_tasks)]
            await asyncio.gather(*[asyncio.wrap_future(task) for task in tasks])

if __name__ == "__main__":
    asyncio.run(main(num_tasks = int(input("Enter the number of tasks to create: ")),url=input(">>"))
     
