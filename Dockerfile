FROM ubuntu:latest

RUN apt update && apt install -y glpk-utils python3 python3-pip coinor-cbc
RUN pip install pandas

COPY clews_ethiopia_model /clews_ethiopia_model/

