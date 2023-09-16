FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8502
HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health
ENTRYPOINT ["streamlit", "run", "src/labelling_app.py", "--server.port=8502", "--server.address=0.0.0.0"]
