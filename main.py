from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def testing_route():
  return { "Hello" : "World!"}