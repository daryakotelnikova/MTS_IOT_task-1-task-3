FROM amancevice/pandas:latest

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 1883
EXPOSE 8000

CMD python ./iot_dashboard/main.py