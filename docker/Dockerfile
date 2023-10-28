# Dockerfile

# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Update the package list and install necessary dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone your project repository and navigate to the /py directory
RUN git clone https://github.com/glweber/python_dash.git .

# Install the Python dependencies from requirements.txt in the project root
RUN pip install -r /app/requirements.txt

# Expose port 8501 (Streamlit default port)
EXPOSE 8501

# Healthcheck to ensure Streamlit is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Set the entry point to run your Streamlit app with the appropriate file and port
ENTRYPOINT ["streamlit", "run", "/app/py/dash.py", "--server.port=8501", "--server.address=0.0.0.0"]
