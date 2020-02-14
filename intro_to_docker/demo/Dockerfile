# Start from a base image. In this case, we are using a docker image with python 3 installed
FROM python:3

# Copy any directories from local storage to the docker image
ADD . /demo

# Change working directory. If ran in -it mode, we would begin in /demo
WORKDIR /demo

# Run any commands necessary for setup. This is usually for installation or setup
RUN pip install -q -r requirements.txt

# Expose port to be accessed
EXPOSE 5000

# Last line of a dockerfile. Runs command. Usually used to run a daemon or webserver
CMD ["python", "app.py"]
