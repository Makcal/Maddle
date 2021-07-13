import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

password = '12345'  # input('Enter password: ')
TEMPLATE = 'pscp -P 5022 -pw {password}{r} {source} maxim@home.pasha1st.ru:' \
           '/home/maxim/VK_Wallet'
LIBRARIES = ('paperscrollsdk', 'Bytecoin.py', 'coronacoin.py', 'vkcoin',
             'vkpoint_api', 'pymysql', 'vk', 'Catcoin.py', 'Worldcoin.py')
PROJECT = ('Coins', 'Connections.py', 'Server.py', 'Account.txt',
           'my_utils.py', 'calc_rates.py')

def transfer(elem):
    print(f'Transfering {elem}...\n')
    os.system(TEMPLATE.format(
        password=password,
        r='' if '.' in elem else ' -r',
        source=fr'.\{elem}',
    ))
    print()


loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(max_workers=5)

os.chdir(r'D:\Mine\PyProjects\Maddle')
elems = [loop.run_in_executor(executor, transfer, elem) for elem in PROJECT]
elems = asyncio.gather(*elems, loop=loop)
loop.run_until_complete(elems)

executor = ThreadPoolExecutor(max_workers=5)

os.chdir(r'C:\Users\Max\AppData\Local\Programs\Python\Python37'
         r'\Lib\site-packages')
libs = [loop.run_in_executor(executor, transfer, lib) for lib in LIBRARIES]
libs = asyncio.gather(*libs, loop=loop)
loop.run_until_complete(libs)

print('\nDone...')
