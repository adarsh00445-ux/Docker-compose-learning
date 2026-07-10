FROM python:3.11
WORKDIR /adarsh
COPY requirements.txt .
RUN pip install -r requrement.txt
COPY . .
CMD ["python","app.py"]