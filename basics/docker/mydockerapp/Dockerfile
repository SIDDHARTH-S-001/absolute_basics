# Start from the official ubuntu base image.
FROM ubuntu:24.04

# Set the working directory inside the container.
WORKDIR /app

# Copy current directory contents into the container.
COPY . .

# Install the necessary packages.
RUN apt update && apt install -y curl

# Define the default command to run when the container starts.
CMD ["echo", "Hello from Docker Container !!!"]