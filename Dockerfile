FROM ubuntu:latest

RUN apt update
RUN apt install -y glpk-utils python3 python3-pip
RUN pip install pandas

COPY clews_ethiopia_model /clews_ethiopia_model/

