# Introduction
Following on from the oirignal source - https://github.com/gabrielpreda/local-explorer-assistant, this is an extension to the concept of local travel assistant to incorporate a local tour guide element. This new agent will detail interesting facts about buildings and landmarks in the location where the user is. Output can be text or voice. The application uses ADK, Gemini, Google Search, and Google Maps APIs. The user's current GPS will be processed by an identifier agent to identify the landmarks at that location. The information is sent to the discovery agent , which uses google search to find information. The composer agent will be prompted to create a friendly, narrative script. We will then add a step to convert this text into speech using an audio generation tool.

# Architecture

Frontend: Streamlit app (streamlit_ui.py)
Backend: FastAPI service (main.py)

## Agents

* **Coordinator** agents (coordinator.py):
    * `root_agent`: for the local explorer feature.
    * `tour_guide_coordinator`: for the tour guide feature.
* Subagents:
    * **Identifier** agent (identifier.py)
    * **Discovery** agent (discovery.py)  
    * **Routing** agent (routing.py)  
    * **Composer** agent (composer.py)  

## Tools

* `google_search` (used by **Discovery** and **Identifier** agents)
* `maps_search_route` (used by **Routing** agent)

## Models

* Gemini 2.5 pro

# Features

## Local Explorer

This feature allows you to plan a personalized day trip based on your interests and available time.

## Tour Guide

This feature provides interesting facts about a landmark at your current location. It uses your GPS coordinates to identify the landmark, searches for information about it, and presents it to you in a narrative format.

# Getting started

## Clone the repo

```bash
git clone https://github.com/opowbow/local-tour-guide-assistant.git
cd local-tour-guide-assistant
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
python3 -m venv venv
source venv/bin/activate
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

The Streamlit application will open in your browser. It has two sections:

* **Local Explorer Assistant**: to plan your trip.
* **Tour Guide**: to get information about your current location.
