# Alpine is a very small/lightweight Linux distribution
# We are starting from an alpine image with Python 3 installed
FROM python:3.11.5

# The WORKDIR command both creates a directory in the container 
# and sets that directory to be the current directory for all further commands
WORKDIR /code

# We install Flask in the container using Pip
RUN pip install flask
RUN pip install flask_socketio
RUN pip install shortuuid

# We want port 5000 (the default Flask port) to be used outside the container
EXPOSE 5001

# We copy everything in the current directory on our machine 
# ... into the working directory in the container 
# (In particular, this includes api.py)
COPY . .

# When the container starts running,
#    This is the final command that we want to be executed
#
# CMD is almost always used to start a program that
#    runs indefinitely and listens over the network for requests
CMD ["python3", "app.py"]

# Instead of running the Flask app through Python
# .. We could also set some environment variables
#    and run the app using the flask command
#
# ENV FLASK_APP=api.py
# ENV FLASK_RUN_HOST=0.0.0.0
# CMD ["flask", "run"]
 
