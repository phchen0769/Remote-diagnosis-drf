FROM alpine:latest

LABEL MAINTAINER = "Fedorov"

# 替换apk使用的源
COPY repositories /etc/apk/repositories
COPY requirements.txt /root/requirements.txt

# 设定容器时间
RUN echo "export TZ='UTC'" > /etc/profile

# Install required packages and remove the apt packages cache when done.
# RUN apk update 
RUN apk add python3 \
	python3-dev \
	gcc \
	g++ \
	# mariadb-connector-c-dev \
	# mariadb-dev \
	linux-headers \
	pcre-dev \
	musl-dev \
	libxml2-dev \
	libxslt-dev \
	nginx \
	jpeg-dev \
	zlib-dev \
	supervisor \
	py3-pip


RUN pip3 install --no-cache-dir -r /root/requirements.txt

# 添加/root/.local/bin目录到环境变量
# ENV PATH="/root/.local/bin:${PATH}"
# 设置环境变量
ENV DJANGO_SETTINGS_MODULE=remote_diagnosis_drf.settings
ENV PYTHONPATH=/workspaces/remote_diagnosis_drf:$PYTHONPATH

# RUN  rm -r /root/.cache

# copy all the configfiles
COPY default.conf /etc/nginx/http.d/default.conf
COPY remote_diagnosis_drf.ini /etc/supervisor.d/
# xadmin针对python3.10的cache源文件修改
# COPY cache.py /usr/lib/python3.10/site-packages/django/views/decorators/cache.py

EXPOSE 8080

CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]