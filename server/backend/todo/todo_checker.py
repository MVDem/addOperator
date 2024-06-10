import asyncio
import threading
from datetime import datetime, timedelta
from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer
from todo.models import Todo
from todo import consumers



async def test():
    while True:
        now = datetime.now()
        reminder_time = now + timedelta(minutes=5)
        reminder_time = reminder_time.replace(second=0, microsecond=0)
        todos = await sync_to_async(list)(Todo.objects.all())
        todos_onsend = [todo for todo in todos if todo.deadline.replace(second=0, microsecond=0).timestamp() == reminder_time.timestamp()]
        print(now, reminder_time)
        print(todos_onsend)

        for todo_onsend in todos_onsend:
            channel_layer = get_channel_layer()
            await channel_layer.group_send(
                'todo_notifications',
                {
                    'type': 'todo_notification',  
                    'message': f'Задача "{todo_onsend.body}" нужно выполнить сейчас!'   
                }
            )
            sent_notifications.add(todo_onsend.id)
        await asyncio.sleep(50)


def start_task_check_loop():
    def start_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    new_loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_loop, args=(new_loop,))
    t.start()

    asyncio.run_coroutine_threadsafe(test(), new_loop)