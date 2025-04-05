# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose the port Render expects
EXPOSE 8000

# Start app using Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
