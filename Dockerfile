FROM igormcsouza/flask:latest

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

RUN pip install git+https://github.com/igormcsouza/movie-review-plus-package.git

WORKDIR /movie-review-plus-backend

COPY backend/ /movie-review-plus-backend

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 app:app
