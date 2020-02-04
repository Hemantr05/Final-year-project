
FROM ubuntu:18.04



RUN apt-get update -y && apt-get install\
	-y --no-install-recommends python3 python3-virtualenv

#RUN python3 -m virtualenc --python=/usr/bin/python3 /opt/venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# We copy just the requiremnts first to leverage Docker cache
COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./keywordextraction/keyword_extraction2.py /keyword_extraction2.py
#WORKDIR /keywordextraction

CMD ["python3","keyword_extraction2.py"]
#CMD exec python3 ./keywordextraction/keyword_extraction.py 
