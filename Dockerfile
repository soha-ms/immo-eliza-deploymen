# Starts from the python 3.10 official docker image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy application's code into the container at /app
COPY api/ /app/


# Run the app
# Set host to 0.0.0.0 to make it run on the container's network
CMD uvicorn app:app --host 0.0.0.0