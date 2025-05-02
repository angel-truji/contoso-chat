from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="44a8130ed1cb4f67b8e6778476d0c6d",
    api_version="2023-12-01-preview",
    azure_endpoint="https://aoai-c4d5vwhvg5ieo.openai.azure.com/"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",  # como "gpt-35-turbo"
    messages=[
        {"role": "user", "content": "Olá!"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
