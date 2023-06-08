import time
from datetime import datetime


timedate = datetime.now().strftime('%d-%m-%Y %H:%M:%S')


# timedate=(timedate.day, timedate.month, timedate.year)
# print(f"Сегодня {timedate.day}-{timedate.month}-{timedate.year}")
print(timedate)



print( '''Привет! Это твоя записная книжка. Давай расскажу что я умею.
Мы можем создать новую запись, найти её, изменить или удалить,
а также показать все записи.''')
