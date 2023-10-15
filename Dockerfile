
FROM datamechanics/spark:3.2.1-latest as spark
ENV PYSPARK_MAJOR_PYTHON_VERSION=3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SPARK_OPTS="--conf spark.driver.extraJavaOptions=""-Divy.cache.dir=/tmp -Divy.home=/tmp"" " 
WORKDIR /app
COPY requirements.txt .
RUN conda install --yes --file requirements.txt 
COPY main.py .
COPY data/ /data/


# VM is wining about adduser not beeing installed. ... skipping security setting for now
USER root
RUN adduser -u 5678 --disabled-password --gecos "" appuser 
RUN  chown -R appuser /app && chown -R appuser /data
USER appuser
CMD ["python", "main.py"]