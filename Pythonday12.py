
### 국비과정 과제 -> 각종 문법과 sqlite db 연결을 통한 간단한 프로그램 제작



import sqlite3

class Survey:
# 데이터베이스 연결
    def __init__(self):
        self.conn = sqlite3.connect('survey1.db')
        self.cursor = self.conn.cursor()

        # 테이블 생성
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS survey1
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    n1 TEXT,
                    n2 TEXT,
                    n3 TEXT,
                    n4 TEXT,
                    n0 TEXT,
                    food1 TEXT,
                    food2 TEXT,
                    food3 TEXT
                    )''')
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def ep(self):
        print("좋아하는 음식 종류 설문조사")
        (input("1. 설문 참여하기는 1번을 누르세요"))
        n1 =(input("1. 한식: "))
        n2 =(input("2. 중식: "))
        n3 =(input("3. 일식: "))
        n4 =(input("4. 양식: "))
        n0 =(input("0. 기타-> 직접입력: "))
        print(f"투표결과 한식{n1}표 , 중식{n2}표 ,일식{n3}표 , 양식{n4}표 ,기타:{n0}")
            
        print("양자택일 ^_^ 전자면 1번 후자면 2번을 입력하시오")
        food1 = (input("짜장 vs 짬뽕 "))
        if food1 == 1:
            print("짜장을 선택하셨습니다")
        else:
            print("당신은 매운 음식을 좋아하는군요")

        food2 = (input("떡볶이 vs 순대 "))
        if food2 == 1:
            print("스트레스 해소는 떡볶이죠")
        else:
            print("맵지않은 음식이 좋습니다")
        food3 = int(input("산 vs 바다 "))
        if food3 == 1:
            print("산은 공기가 좋습니다")
        else:
            print("시원한 바닷바람 맞으러 가시죠")
            # 데이터 입력
        self.cursor.execute("INSERT INTO survey1 (n1, n2, n3, n4, n0, food1, food2, food3) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (n1, n2, n3, n4, n0, food1, food2, food3))
        self.conn.commit()

if __name__ == "__main__":
    surve = Survey()
    surve.ep()

conn = sqlite3.connect('survey1.db')
c = conn.cursor()
c.execute("SELECT * FROM survey1")
rows = c.fetchall()
print(rows)