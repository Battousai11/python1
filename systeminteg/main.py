from fastapi import FastAPI 
import uvicorn 
app = FastAPI()

@app.get("/hello/{name}")
async def main(name:str):
        return {"message": f"Hello {name}"}


@app.get("/addition/{num1}/{num2}")
async def main(num1:int, num2:int):
        answer = num1 + num2
        return {"message": f"Answer = {answer}"}

@app.get("/subtraction/{num1}/{num2}")
async def main(num1:int, num2:int):
        answer = num1 - num2
        return {"message": f"Answer = {answer}"}

@app.get("/division/{num1}/{num2}")
async def main(num1:int, num2:int):
        answer = num1 / num2
        return {"message": f"Answer = {answer}"}

@app.get("/multiplication/{num1}/{num2}")
async def main(num1:int, num2:int):
        answer = num1 * num2
        return {"message": f"Answer = {answer}"}