FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Copy local code to the container image.
RUN mkdir -p /nxn/app
WORKDIR /nxn/app

# Copy and install requirements
COPY requirements.txt /nxn/app
RUN pip install --no-cache-dir -r requirements.txt

# Copy contents from your local to your docker container
COPY . /nxn/app
