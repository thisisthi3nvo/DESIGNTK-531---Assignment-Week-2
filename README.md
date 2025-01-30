# DESIGNTK-531---Assignment-Week-2
This project demonstrates the integration of MQTT (Message Queuing Telemetry Transport) with OpenAI's Language Model (LLM) for real-time sensor data analysis.

## Project Description
The system consists of three main components:
An MQTT publisher that simulates sensor data
An MQTT subscriber that receives the data and processes it using OpenAI's LLM
A standalone LLM test script for independent validation

## Setup and Installation
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies:
- pip install paho-mqtt openai
4. Set up your OpenAI API key:
- Create an account on OpenAI's platform if you haven't already.
- Obtain your API key from the OpenAI dashboard.
- Replace the placeholder API key in sub2.py and LLMtest.py with your actual key.

## Usage
MQTT Publisher (pub.py)
Run the publisher to simulate sensor data:
python pub.py
This script will continuously publish random temperature and humidity data to the MQTT broker.

MQTT Subscriber with LLM Integration (sub2.py)
Start the subscriber to receive sensor data and analyze it using the LLM:
python sub2.py
The subscriber will connect to the MQTT broker, receive messages, and send them to OpenAI's API for analysis.

Standalone LLM Test (LLMtest.py)
To test the LLM interaction independently:
python LLMtest.py
This script sends a fixed prompt to OpenAI's API and prints the response, allowing you to verify the LLM functionality without MQTT integration.

## Example Output
When running sub2.py, you might see output similar to:

Received message on topic pythontest/sensors/mysensor: {"hello": "hello class!!!!!!!", "temperature": 23.7, "humidity": 49.0, "timestamp": "2025-01-29T22:58:47.362177"}
LLM Analysis: The sensor data shows a temperature of 23.7°C and a humidity level of 49.0%. This indicates a comfortable room temperature with moderate humidity. The timestamp suggests this reading was taken on January 29, 2025, at 22:58:47 UTC.
When running LLMtest.py, you should see an explanation of MQTT printed to the console.
