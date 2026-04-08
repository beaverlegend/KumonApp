# Use CentOS Stream 9 as the base image
FROM quay.io/centos/centos:stream9

# Install Python and pip (standard in CentOS 9)
RUN dnf install -y python3 python3-pip && dnf clean all

# Set the working directory inside the container
WORKDIR /app

# Copy your requirements file first to leverage caching
COPY requirements.txt .

# Install your dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your project code
COPY . .

# Expose the port Flask runs on (usually 5000)
EXPOSE 5000

# Command to run your app
# Using 0.0.0.0 allows connections from outside the container
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"] 