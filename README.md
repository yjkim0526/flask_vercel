
# [ Python Flask ] 파이썬 플라스크 웹서버  Vercel 배포 하기

* 디렉토리 위치 : C:\project\flask_python\flask_vercel 

1.  가상디렉토리 생성 :
   C:\project\flask_python\flask_vercel>python -m venv myvenv

3.  가상 디렉토리 활성화
   C:\project\flask_python\flask_vercel>.\myvenv\Scripts\activate

4. pip install flask 설치 하기
   (myvenv) C:\project\flask_python\flask_vercel>pip install flask

5. app.py 작성하기

6. templates 폴더 만들고 index.html 생성하기
  
7. app.py 실행
(myvenv) C:\project\flask_python\flask_vercel>python app.py

8. http://127.0.0.1:5000 눌러서 확인하기
   
9. vercel 배포 작업 준비하기
   - 배포시에 필요한  pip list 만들기 ( pip freeze > requirements.txt )
   (myvenv) C:\project\flask_python\flask_vercel>pip freeze > requirements.txt
   
   - app.py   app.run() 로 수정 필요 (개발모드 제거)
   
   - vercel.json  만들기
     vercel.json 생성 후 아래 내용 넣기
   
     {
       "builds": [{ "src": "app.py", "use": "@vercel/python" }],
       "routes": [{ "src": "/(.*)", "dest": "app.py" }]
     }
   
   - vscode 터미널 에서  vercel  CLI 설치 ( npm i -g vercel )
   (myvenv) C:\project\flask_python\flask_vercel>npm i -g vercel
   
   - vscode 터미널 에서 vercel 에 로그인 하기  ( vercel login )
   (myvenv) C:\project\flask_python\flask_vercel>vercel login
   
   - vercel 배포 ( vercel . ) → 현재 디렉토리 배포
   (myvenv) C:\project\flask_python\flask_vercel>vercel .
   
   * Link to existing project? —> N 선택 나머지는 Y또는 엔터 

10. 배포 완료

