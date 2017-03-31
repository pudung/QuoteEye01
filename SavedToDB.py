# 결과값 DB에 넣을 수 있는 형태로 만든 담에 Give to M.S
# created by Kelly 2017-2-27

import pymysql

from mystuff.WebCrawler import quote3

# charset 변경

cnx = pymysql.connect(user='kelly', password='kelly1994',
                              host='insighteye.cqsjnckwggck.ap-northeast-2.rds.amazonaws.com',port=3309,
                              database='QuoteEye',charset='utf8',)


quote = quote3.quote

#print("quote:",quote)

try:
    cursor = cnx.cursor()

    cursor.execute("use QuoteEye")

    cursor.execute("show tables")


# Sidx, Eidx 시작 인덱스, 끝인덱스 가져오기

    cursor.execute("SELECT Art_ID, URL FROM Article")

    row = cursor.fetchone()

    print(row[0],row[1])


    sql = """INSERT INTO Quote(Quote, Sidx, Eidx, Art_ID, Nm_ID, Ms_ID) VALUES (%s, %s, %s, %s,%s, %s)"""

    print(sql, %(Quote, Sidx, Eidx, Art_ID, Nm_ID, Ms_ID))


    cursor.execute(sql,(quote,1,2,row[0],"null","null"))

    cnx.commit()



finally:
    
    cursor.close()

    cnx.close()

    # 5. disconnect from server

