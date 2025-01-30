import paho.mqtt.client as mqtt
import time
from openai import OpenAI

# Initialize OpenAI client
openai_client = OpenAI(api_key="aSYRDifAVYczMcKTQNbBs17kWrtjVOCrHp8OtZTnZbJpxLGKC-IDaOQUKX4QM4ApH68YoTb0T3BlbkFJSal0T2ZTUUBZWAjd1QUeflI_AcKvmFQ4xXr-jof7cKCD_gMTnnxbEGA6jfVr7VNZVsJ-9cC3YA")

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    
    try:
        # Generate a prompt based on the received message
        prompt = f"Generate an analysis of this sensor data: {msg.payload.decode()}"
        
        # Send the prompt to OpenAI
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant analyzing sensor data."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Print the LLM's response
        print("LLM Analysis:", response.choices[0].message.content)
    except Exception as e:
        print(f"Error in LLM processing: {str(e)}")
