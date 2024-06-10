import asyncio

def start_database_check():
    from .consumers import database_check_loop
    print('Database check started')
    database_check_loop()