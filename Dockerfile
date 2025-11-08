# ✅ Use a stable Python version (latest can break some libs)
FROM python:3.12-slim

# ✅ Prevent interactive apt warnings
ENV DEBIAN_FRONTEND=noninteractive

# ✅ Set working directory inside the container
WORKDIR /app

# ✅ Copy dependency list first (for efficient caching)
COPY requirements.txt .

# ✅ Install system dependencies
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg curl unzip bash \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ✅ Install Deno (optional)
RUN curl -fsSL https://deno.land/install.sh | sh \
    && ln -s /root/.deno/bin/deno /usr/local/bin/deno

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -U -r requirements.txt

# ✅ Copy all app files into the container
COPY . .

# ✅ Optional: define environment variables (replace with real values)
# ENV API_ID=123456
# ENV API_HASH=abcdef1234567890abcdef1234567890
# ENV BOT_TOKEN=1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ

# ✅ Default command to start your bot
CMD ["bash", "start"]
