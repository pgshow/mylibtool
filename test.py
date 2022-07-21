import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="China is trying to ease panic over two of the biggest issues threatening social stability in the country—mortgage boycotts and frozen bank accounts.\n\nOn Sunday, the China Banking and Insurance Regulatory Commission urged banks to increase loan support for real estate developers so they can complete unfinished projects, as thousands of disgruntled homebuyers are staging a mortgage boycott across the country.\n\nWrite a title for this article",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)