import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_SCENE")
)

def scene_llm(s_prompt):
  completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role":"user","content":s_prompt}],
    temperature=0.1,
    top_p=1,
    max_tokens=5000,
    stream=False
  )
  return completion.choices[0].message.content