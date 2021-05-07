FROM python:3.6.5-stretch
COPY ./ ./
RUN pip install -r /requirements.txt
CMD ["/bin/bash", "run.sh"]
