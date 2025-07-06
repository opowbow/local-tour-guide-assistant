# Introduction

# Architecture

# Getting started

## Clone the repo

```bash
git clone https://github.com/gabrielpreda/local-explorer-assistant.git  
cd local-explorer-assistant
```

## Create an .env file

The file should contain the following:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=YOUR_PROJECT
GOOGLE_CLOUD_LOCATION=YOUR_REGION
GOOGLE_MAPS_API_KEY=YOUR_GOOGLE_MAPS_API_KEY
```

## Install dependencies

Run:
```bash
pip install -r requirements.txt
```

## Start the backend

Run:
```bash
uvicorn main:app --reload
```

## Start the frontend

Run:
```bash
streamlit run streamlit_ui.py
```




