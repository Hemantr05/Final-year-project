FROM ubuntu:18.04



RUN apt-get update -y && apt-get install\
	-y --no-install-recommends python3 python3-virtualenv

RUN python3 -m virtualenc --python=/usr/bin/python3 /opt/venv

# We copy just the requiremnts first to leverage Docker cache
COPY ./requirement.txt .

#WORKDIR /keywordextraction

RUN . /opt/venv/bin/activate && pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD . /opt/venv/bin/activate && exec python3 Keyword_extraction2.py
 
