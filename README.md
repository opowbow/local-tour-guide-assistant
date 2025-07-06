# Introduction
The application uses ADK, Gemini, Google Search, and Google Maps APIs to power a local explorer assistant, which make recommendation for a short city visit. The user enters in a minimalistic Streamlit user interface few informations (the city visited, preferences, the time budget (between 1 and 12 hours), and things to avoid. The information is sent to the backend (built with FastAPI) and broadcasted to the coordinator agent for processing and preparing the response. This coordinator agent is using a number of sub-agents (AgentTools), each specialized in one specific task.

# Architecture

Frontend: Streamlit app (streamlit_ui.py)
Backend: FastAPI service (main.py)
Agents: 
* **Coordinator** agent (coordinator.py)
* Subagents:
    * **Discovery** agent (discovery.py)  
    * **Routing** agent (routing.py)  
    * **Composer** agent (composer.py)  
Tools:
* `google_search` (used by **Discovery** agent)
* `maps_search_route` (used by **Routing** agent)
Models:
* Gemini 2.5 pro

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




