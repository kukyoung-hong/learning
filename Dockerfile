From python:3.11-slim

#로컬 컴퓨터가 아니라 컨테이너에서 app이라는 dir만든다는것임
WORKDIR /app

COPY .env.prod /app/.env.prod
# dependency 복사 및 설치
# . 이 /app이랑 같음
COPY requirements.txt .
#RUN은 container안에서 실행하는 명령어
RUN  pip install --no-cache-dir -r requirements.txt

#manage.py dir에 있는 모든 내용을 app dir에 다 복사하겠다
COPY . .

# 크론 및 슈퍼바이저 설치
# 특정 시간에 실행시켜주는 프로그램
# 슈퍼바이저 : 계속 떠있는 프로그램
# apt는 리눅스에서 기본적으로 설치하는 프로그램 
RUN apt-get update && apt-get install -y supervisor cron && apt-get clean && rm -rf /var/lib/apt/lists/*

# 여기는 아직 몰라도 됨
#크론 설정 복사 및 등록
#크론을 특정 원하는 시간에 실행시키도록
COPY ./cronjob.txt /etc/cron.d/news_cron

RUN chmod 0644 /etc/cron.d/news_cron
RUN crontab /etc/cron.d/news_cron

#supervisor 설정 복사
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#로그 폴더
RUN mkdir -p /app/logs
#여기까지

#환경변수 설정
#컨테이너 안에 장고env라는 환경변수를 만들고 그 값을 production이라고 쓰겠다.
ENV DJANGO_ENV=production

# collectstatic 명령실행 
# css파일같은 static파일들
# nginx가 static을 찾을 수 있도록 모아두는 작업이 collectstatic이다.
RUN python manage.py collectstatic --noinput

#포트노출 ( nginx 기본포트)
EXPOSE 8000
#webserver gateway interface 
#8000번 포트로 들어오는 0.0.0.0은 모든 주소를 허용하겠다 
CMD ["gunicorn","learning.wsgi:application", "--bind","0.0.0.0:8000"]