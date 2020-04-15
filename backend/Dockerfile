FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Copy local code to the container image.
RUN mkdir -p /nxn/
WORKDIR /nxn/

# Copy and install requirements
COPY requirements.txt /nxn/
RUN pip install --no-cache-dir -r requirements.txt

# Copy contents from your local to your docker container
COPY . /nxn/

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
