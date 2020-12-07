FROM python:3.9.0
ENV USER_NAME="Ruju"
COPY hello.py .
CMD ["python","hello.py"]
