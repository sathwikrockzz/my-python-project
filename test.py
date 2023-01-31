import sqlite3 as sl
con = sl.connect("my-app.db")
cur = con.cursor()
ans = cur.execute("select * from signup")
for i in ans.fetchall():
    print(i)
bmi = cur.execute("select * from bmi")
for i in bmi.fetchall():
    print(i)
con.close()

