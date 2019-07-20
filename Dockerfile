FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /home/docker/
ADD ./requirements.txt /home/docker/requirements.txt
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip3 install --no-cache-dir -r /home/docker/requirements.txt
ADD . /home/docker/
WORKDIR /home/docker/src/
CMD ["gunicorn", "manage:app", "-c", "./gunicorn.conf.py"]
