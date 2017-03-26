# 결과값 DB에 넣을 수 있는 형태로 만든 담에 Give to M.S
# created by Kelly 2017-2-27


import pymysql

# charset 변경

cnx = pymysql.connect(user='kelly', password='kelly1994',
                              host='insighteye.cqsjnckwggck.ap-northeast-2.rds.amazonaws.com',port=3309,
                              database='QuoteEye',charset='utf8',)


print("start")


# 1. 연결: MySQL connection // mysql cmd 에서 정보 확인.
#from mystuff.WebCrawler.quote import index_tuple

# quote eyes 서버 접속

# 2. Connection 으로 부터 Cursor 생성

try:
    cursor = cnx.cursor()
    print("1")
    # 3. SQL문 실행
    cursor.execute("use QuoteEye")
    print("2")
    cursor.execute("show tables")
    print("3")

    # 4. 데이터 fetch
    data2 = cursor.fetchall()

    # 5. articlescraper column 프린트
    print("Databases are: %s" % [data2])



finally:
    
    cursor.close()

    cnx.close()

    # 5. disconnect from server

