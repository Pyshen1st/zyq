import pandas_datareader.data as web
import datetime
start  = datetime.datetime(1900,1,1)
end = datetime.date.today()
maotai2 = web.DataReader("600519.SS", "yahoo", start, end)
# for i in range(4, 8):
#     print list(maotai2.iloc[i,:])


import sqlite3
conn = sqlite3.connect('D:/sqlite3/maotai02.db')  #(":memory:")
c = conn.cursor()
#
#c.execute('''create table ceshi(user text, note text)''')
#
#c.execute('''insert into ceshi(user,note) values('11','21')''')
#
#c.execute('''update ceshi(user, note) set note = '22' where user = '11' ''')
#

#
#c.execute('''create table maotai122201(open, high, low, close, volume, adjclose)''')
for i in range(1, len(maotai2 + 1)):     #[1,len(maotai2) + 1, 1]
    mt = list(maotai2.iloc[i,:])
    c.execute('''insert into maotai122201 values(?,?,?,?,?,?)''', mt)

conn.commit()
c.execute('''select * from maotai21''').fetchall()
rec = c.execute('''select * from maotai21''')
print c.fetchall()
