# Use the official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# 1. Copy ONLY requirements.txt first (this caches the pip install step)
COPY requirements.txt /app/

# 2. Install dependencies from the file
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of the application code
COPY . /app/

# Make port 5000 available
EXPOSE 5000

# Run the app using gunicorn (Production server)
# Note: "app:app" means "file app.py, object app"
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]