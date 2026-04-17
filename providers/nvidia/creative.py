import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_CREATIVE")
)


def creative_llm(creative_prompt):
  completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role":"user","content":creative_prompt}],
    temperature=1,
    top_p=1,
    max_tokens=5000,
    stream=False
  )
  return completion.choices[0].message.content