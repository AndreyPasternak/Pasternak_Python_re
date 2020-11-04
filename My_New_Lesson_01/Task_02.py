usertime = int(input('Введите секунды'))
hours = usertime // 3600
minutes = (usertime // 60) - (60*hours)
seconds = usertime - (hours*3600 + minutes*60)
print(f"ВРЕМЯ >>> {hours:02}:{minutes:02}:{seconds:02}")


