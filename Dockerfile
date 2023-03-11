FROM python:3.10

WORKDIR /api

COPY ./app/requirements.txt /api/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/app/requirements.txt

COPY ./app /api/app

WORKDIR /api/app/bin

RUN echo 'export PATH=/api/app/bin:$PATH' >> "$HOME/.bashrc"

CMD ./entrypoint
