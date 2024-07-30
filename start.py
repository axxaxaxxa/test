import asyncio
from new_file import main
num_tasks= int(input("Enter the number of tasks to create: "))
url=input(">>")
print(1)
asyncio.run(main(num_tasks=num_tasks,url=url))
print(2)
asyncio.run(main(num_tasks=num_tasks,url=url))
print(3)
asyncio.run(main(num_tasks=num_tasks,url=url))
