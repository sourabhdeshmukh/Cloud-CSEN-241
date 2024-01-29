FROM sourabhdeshmukh/ubuntu-sysbench:v1 
MAINTAINER Sourabh Deshmukh <sourabh.deshmukh.988@gmail.com>
WORKDIR /app
COPY ./scripts/* /app/
RUN chmod +x /app/sysbench.sh
CMD ["./sysbench.sh"]
