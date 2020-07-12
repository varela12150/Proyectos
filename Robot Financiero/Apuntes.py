import pandas as pd
import calendar
festivos = list(calendar.day_name)
print(festivos)


s = pd.date_range(start="2020-02-27", end="2020-4-06" )
df = pd.DataFrame(s, columns=['Fecha'])
 




        