# Introduction
Following on from the oirignal source - https://github.com/gabrielpreda/local-explorer-assistant, this is an extension to the concept of local travle assistamt to incorporate a local tour guide. The agent will details interesting facts about building in the location where the user is. Output can be text or voice. The application uses ADK, Gemini, Google Search, and Google Maps APIs. The user's current GPS will be processed by an identifier agent to identify the landmarks at that location. The information is sent to the discovery agent , which uses google search to find information. The composer agent will be prompted to create a friendly, narrative script. We will then add a step to convert this text into speech using an audio generation tool.

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




