"""
날짜 : 2023/01/13
이름 : 진윤희
내용 : 파이썬 사용자 관리 프로그래밍 실습
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234', 
                        db='java1db', 
                        charset='utf8')
"""cur = conn.cursor()"""



while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0
    try:
        answer = int(input('선택 : '))
    except Exception as e:
        print('다시 입력하세요. ', e)
        continue
    


    if answer == 0:
        break



    elif answer == 1:
            """
            # 내 코드
            print('아이디, 비밀번호, 이름, 휴대폰번호, 나이를 하나씩 입력하세요.')
            a = input()
            b = input()
            c = input()
            d = input()
            e = input()

            

            # SQL 실행
            sql = "insert into `user1` values ('"+a+"', '"+b+"', '"+c+"', '"+d+"', '"+e+"');"
            cur.execute(sql)
            conn.commit()

            # 데이터베이스 종료
            print('Insert 완료...')
            continue
            """

            # 선생님 코드
            data = list(input('아이디, 비번, 이름, 휴대폰, 나이 순으로 입력 : ').split())
            cur = conn.cursor()
            sql = "insert into `user1` values ('%s', '%s', '%s', '%s', '%s')"
            cur.execute(sql % (data[0], data[1], data[2], data[3], data[4]))
            conn.commit()

            print('계정등록 완료.')
            continue


    elif answer == 2:
            """
             # 내 코드
            sql = "select * from `user1`"
            cur.execute(sql)
            conn.commit()

            # 데이터 출력
            for row in cur.fetchall():
                print('----------------------')
                print('아이디 : ', row[0])
                print('비밀번호 : ', row[1])
                print('이름 : ', row[2])
                print('휴대폰 : ', row[3])
                print('나이 : ', row[4])

            print('----------------------')
            print('전체조회 완료...')
            continue
            """

             # 선생님 코드
            cur = conn.cursor()
            cur.execute("select * from `user1`")
            conn.commit()

            print('|아이디|비밀번호|이름|휴대폰|나이|')
            for row in cur.fetchall():
                print('----------------------')
                print('|%s|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3], row[4]))
            print('전체조회 완료...')
            continue


    elif answer == 3:
            """
            # 내 코드
            print('검색하실 계정의 아이디를 입력하세요.')
            a = input()
            sql = "select * from `user1` where `uid`='"+a+"';"
            cur.execute(sql)
            conn.commit()

            # 데이터 출력
            for row in cur.fetchall():
                print('검색하신 계정의 정보는 다음과 같습니다.')
                print('----------------------')
                print('아이디 : ', row[0])
                print('비밀번호 : ', row[1])
                print('이름 : ', row[2])
                print('휴대폰 : ', row[3])
                print('나이 : ', row[4])
                print('----------------------')
            continue
            """

            # 선생님 코드
            name = input('이름검색 : ')
            cur = conn.cursor()
            cur.execute("select * from `user1` where `name`='{}'".format(name))
            conn.commit()

            print('|아이디|비밀번호|이름|휴대폰|나이|')
            for row in cur.fetchall():
                print('----------------------')
                print('|%s|%s|%s|%s|%s|' % (row[0], row[1], row[2], row[3], row[4]))
            print('검색 완료...')
            continue



    elif answer == 4:
                """
                # 내 코드
                print('삭제하실 계정의 아이디와 비밀번호를 입력하세요.')
                a = input()
                b = input()
                sql = "delete from `user1` where `uid`='"+a+"'and `pass`='"+b+"';"
                cur.execute(sql)
                conn.commit()
                print('해당 계정을 삭제하였습니다.')
                """

                # 선생님 코드
                name = input('삭제할 이름 : ')
                cur = conn.cursor()
                cur.execute("delete from `user1` where `name`='{}'".format(name))
                conn.commit()

                print('삭제완료...')
                continue
    else:
        print('0 ~ 4 중에 입력하세요')



# 데이터베이스 종료
conn.close()
print('프로그램 종료...')   