# Pull this image from dockerhub.com which will be the starting point for the image we are building
FROM python:3.8-slim-buster
# Just a meta data about who maintains this Dockerfile
MAINTAINER nabinkhadka14@gmail.com
# Update the existing image and install gcc and libpg-dev which are required for our postgresql in the image we are building
RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/* \
# Lets create a directory where we will work in this image we are building
RUN mkdir /api-server
# Switch to that working directory
WORKDIR /api-server
# Copy all files from your laptop to the working directory in this image we are building
COPY . /api-server
# Install python libraries we need in the image we are building
RUN pip install flask psycopg2 PyJwt