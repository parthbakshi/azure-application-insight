FROM python:3.13-bookworm
LABEL authors="parthbakshi"
WORKDIR /app
COPY requirements.txt .

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN python
RUN pip install -r requirements.txt
COPY main.py .
EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]