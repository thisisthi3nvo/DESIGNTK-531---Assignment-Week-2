from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="aSYRDifAVYczMcKTQNbBs17kWrtjVOCrHp8OtZTnZbJpxLGKC-IDaOQUKX4QM4ApH68YoTb0T3BlbkFJSal0T2ZTUUBZWAjd1QUeflI_AcKvmFQ4xXr-jof7cKCD_gMTnnxbEGA6jfVr7VNZVsJ-9cC3YA")

# Send a fixed test prompt
prompt = "Explain MQTT"

# Send the prompt to OpenAI
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Print the LLM's response
print("LLM Response:", response.choices[0].message.content)
