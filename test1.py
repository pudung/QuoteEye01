# Python version in the development environment 2.7.11
# created by Kelly 2017-2-27


from mystuff.WebCrawler.quote import article_text3


def findvalue(STRING, aSub, aStart, bSub):
    '''STRING,aSub,aStart,bSub'''

    # aStart(위치) 부터 aSub 문자 Searching.
    indexA = STRING.index(aSub, aStart) + len(aSub)

    # 위에서 aStart부터 찾았으니까 그 이후인 indexA부터 bSub 문자 Searching.
    indexB = STRING.index(bSub, indexA)

    # STRING 에서 aSub에 입력한 문자열과 bSub에 입력한 문자열의 중간 문자열 리턴
    returnvalue = (indexA, indexB + len(bSub), STRING[indexA:indexB].strip())

    # indexA = s, indexB = indexB+len(bSub) = e, v = quote

    return returnvalue

# 문자열 인자

def findnickname(text):

    whitelist = ['유승민', '유 의원', '그는']
# nick name이 white list에 없을 경우가 -1

    for nickname in whitelist:
        if text.find(nickname) > -1:
            return nickname

    # nickname unfound
    return None



#def findnickname(nickIndexA, nickIndexBWithLength):
    # 위에 있는 indexA를 따로 저장해야 할듯? 위의 메소드에서는
    # # 앞
    # nickname_aSub = nickIndexA - 20
    # # 뒤
    # nickname_bSub = nickIndexBWithLength + 10


STRING = article_text3


#STRING = '더불어민주당 김재인 ' \
#        '전 대표는 25일 "평창동계올림픽이 북한의 참여로 평화의 상징이 된다면 올림픽 성공에도 도움이 되고 꽉 막힌 남북관계를 풀어내는 계기가 될 것"이라고 말했다.'

outIndexA, outIndexBWithlength, quoteString = findvalue(STRING, '"', 0, '"')

HeadText = STRING[outIndexA-15:outIndexA]


# 기사 첫줄만 HeadText 가 됨.

print(HeadText)
print(findnickname(HeadText))
