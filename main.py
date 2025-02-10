from dotenv import load_dotenv
from mira_sdk import MiraClient, Flow
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

flow = Flow(source="flow.yaml")

input_dict = {"topic": "India vs Australia 2023 ODI World Cup Final", "style": "Indian"}

response = client.flow.test(flow,input_dict)

print(response)