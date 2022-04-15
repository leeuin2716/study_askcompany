1. bash in 
2. pip install pipenv
3. pipenv --three                # python 3.8.10
4. pipenv shell
5. pip install -r requirements.txt
6. vscode 재실행
7. F1 버튼  >python:Select interpreter   생성된 가상환경 선택




pipenv 에러시 

1 pip uninstall virtualenv    기존 virtualenv 삭제
2 pip uninstall pipenv  생성된 pipenv 도 삭제 

후 재설치 

가상환경 비활성화 deactivate


라이브러리 requirements.txt 화

pip freeze > requirements.txt

#batch file 작성시
{
f1 >> pythonSelectInterpreter >>>  생성한 가상환경 실행

6.
{가상환경경로}/Scripts/activate.bat
ex =        C:/Users/ASC/.virtualenvs/Crawler-1-SB4-eyB_/Scripts/activate.bat


7.
{가상환경경로}/Scripts/python.exe {python 파일경로 }/coupang_crawler.py
C:\Crawler-1>C:/Users/ASC/.virtualenvs/Crawler-1-SB4-eyB_/Scripts/python.exe c:/Crawler-1/living_paradise/coupang_crawler.py

}


pycharm power_shell 권한 에러시

1. ExecutionPolicy   #현재 권한확인 -->> Unrestricted 아닐경우
2. Set-ExecutionPolicy -Scope CurrentUser
3. Unrestricted
4. ExecutionPolicy

data base---------

ex) mssql
host = '211.223.132.46'
database = 'living_paradise'
user = 'living_paradise '
password = 'asc1234pw!'
conn = pymssql.connect(
    host , user, password, database,charset='utf8'
)








코스메카
host = '211.223.132.46'
        database = 'cosmeca'
        user = 'cosmeca '
        password = 'asc1234pw!'

        conn = pymssql.connect(
            host , user, password, database,charset='utf8'
        )

무료 프록시 https://free-proxy-list.net/




  cursor.nextset()

    results1 = cursor.fetchall()