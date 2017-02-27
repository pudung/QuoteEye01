# 결과값 DB에 넣을 수 있는 형태로 만든 담에 Give to M.S
# created by Kelly 2017-2-27


import pymysql

# 1. 연결: MySQL connection // mysql cmd 에서 정보 확인.
from mystuff.WebCrawler.quote import index_tuple

conn = pymysql.connect(user="root", passwd="kelly1994", charset='utf8')

# 2. Connection 으로 부터 Cursor 생성

try:
    cursor = conn.cursor()

    # 3. SQL문 실행
    cursor.execute("use articlescraper")
    cursor.execute("show tables")


    # 4. 데이터 fetch
    data2 = cursor.fetchall()

    # 5. articlescraper column 프린트
    print("Databases are: %s" % [data2])

    #data = cursor.fetchone()
    #print("Database version is : %s" % data)


finally:
    cursor.close()
    conn.close()

    # 5. disconnect from server


# 마지막 인용문의 튜플만 출력됨.
print(index_tuple)