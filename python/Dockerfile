FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Copy local code to the container image.
WORKDIR /app
COPY . ./

# Install production dependencies.
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "nxn_game.main:app", "--host", "0.0.0.0", "--port", "80"]
