FROM python:3.10
WORKDIR /skillsync
ENV PYTHONPATH="${PYTHONPATH}:/skillsync/src/main/python"
COPY . /skillsync/
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "src/main/python/main.py"]
