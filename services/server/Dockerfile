FROM python:3.6
COPY requirements.txt /tmp
ADD server.py /
RUN pip install -r /tmp/requirements.txt
EXPOSE 5000
EXPOSE 8888
CMD ["python3", "server.py"]

