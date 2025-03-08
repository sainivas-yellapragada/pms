#!/bin/bash

echo "🔹 Creating a virtual environment..."
python3 -m venv venv  
source venv/bin/activate  

echo "🔹 Upgrading pip..."
pip install --upgrade pip  

echo "🔹 Installing dependencies..."
pip install -r requirements.txt  

echo "🔹 Checking installed packages..."
pip freeze  

echo "🔹 Collecting static files..."
python3 manage.py collectstatic --noinput  