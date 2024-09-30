import os
from dotenv import load_dotenv

from openai import OpenAI, AzureOpenAI
load_dotenv()

class OpenAIClient:
    def __init__(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        self.azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT") 
        self.azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")  
        self.azure_api_version = os.environ.get("AZURE_OPENAI_API_VERSION") 

    def chat_complete_openai(self, prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 300, system_prompt: str = "You are a helpful assistant.", temperature: float = 0.5) -> str:
        response = await openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}], 
            max_tokens=max_tokens,
            temperature=temperature  
        )
        return response.choices[0].message.content.strip()

    def chat_complete_azure(self, prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 300, system_prompt: str = "You are a helpful assistant.", temperature: float = 0.5) -> str:
        response = await AzureOpenAI.ChatCompletion.create(  
            model=model,
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],  prompt
            max_tokens=max_tokens,
            api_base=self.azure_endpoint,  
            api_key=self.azure_api_key,
            temperature=temperature  
        )
        return response.choices[0].message.content.strip()