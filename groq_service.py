from groq import Groq

client = Groq()

def execute(prompt):
  completion = client.chat.completions.create(
    #   model="aura-asteria-en",
      model="llama2-70b-4096",
      messages=[
          {
              "role": "user",
              "content": prompt
          },
      ],
      temperature=0.5,
      max_tokens=1024,
      top_p=1,
      stream=True,
      stop=None,
  )

  response = ''
  for chunk in completion:
      response += chunk.choices[0].delta.content or ""
  
  return response

if __name__ == "__main__":
  print(execute("Tell a joke"))