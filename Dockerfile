FROM python:3.11
WORKDIR /adarsh
COPY . .
RUN pip install -r requirements.txt
CMD ["python","app.py"]