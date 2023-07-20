name: My GitHub Action

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Python script
      run: python main.py

    - name: Check file existence
      run: |
        [ -f image_url.txt ] && echo "File exists" || echo "File does not exist"

    - name: Commit and push if changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add image_url.txt
        git commit -m "Add changes" || echo "No changes to commit"
        git push
