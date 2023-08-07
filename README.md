# pyHueBridge
A Python FastAPI based server to facilitate easier communication with the Phillips Hue bridge.

## Description
This is a simple server designed to make it easier for an app to communicate with a Hue Bridge.
It accomplishes the following:
 - Offers an endpoint that returns rooms with the room's corresponding light information, rather than just light IDs.   
 This enables a client application to get this information with one XHR call, rather than combining the results of two calls in the client application.
 - translates colors to RGB values rather than HSV 

## Configuration
Note: Requires the Philips Hue bridge/hub

Create a `config.py` file in the server's root directory following the example of the `config.py.sample` file.

## Development
 - start dev server: `uvicorn main:app --reload`
