
FROM python:3.8-slim-buster

# Update the package lists and upgrade existing packages
RUN apt update && apt upgrade -y

# Install git to be able to clone repositories
RUN apt install git -y

# Copy the requirements.txt file to the root directory
COPY requirements.txt /requirements.txt

# Change the working directory to root
WORKDIR /

# Upgrade pip and install the required Python packages
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

# Create a directory for the converterbot application
RUN mkdir /converterbot

# Change the working directory to /converterbot
WORKDIR /converterbot

# Copy the start.sh script to the /converterbot directory
COPY start.sh /converterbot/start.sh

# Expose port 8080
EXPOSE 808

# Set the absolute path of the start.sh script as the command to run when the container starts
CMD ["/bin/bash", "/converterbot/start.sh"]
