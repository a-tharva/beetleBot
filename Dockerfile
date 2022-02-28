FROM python:3

# Create directory
WORKDIR /bot

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# Copy all files from current to image
COPY . .

# Start
CMD ["python", "main.py"]
