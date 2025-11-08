# Use a stable Python version (latest might break some libs)
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list first (for efficient caching)
COPY requirements.txt .

# Install system dependencies
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg curl unzip bash \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Deno (optional but kept for your setup)
RUN curl -fsSL https://deno.land/install.sh | sh \
    && ln -s /root/.deno/bin/deno /usr/local/bin/deno

# Install Python dependencies
RUN pip3 install -U pip && pip3 install -U -r requirements.txt

# Copy all app files into the container
COPY . .

# Run your startup script
CMD ["bash", "start"]
