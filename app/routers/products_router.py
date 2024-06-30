
from fastapi import APIRouter, HTTPException, Depends
from models.database import  Session, get_db
from schemas.chat_request import ChatRequest
from openai import OpenAI
from models.product import Product
from models.database import  db_dependency
from typing import List


router = APIRouter(
    prefix='/product',
    tags=['product']
)

client = OpenAI()

def read_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.post("/chat")
def chat_bot(request: ChatRequest, db: Session = Depends(get_db)):
    try:

        data = db.query(Product).all()
        if data:
            product_info = ", ".join([f"{p.name} ({p.type})" for p in data])
            system_message = f"You are an AI assistant for Makers Tech, a technology ecommerce company. Your task is to assist users through a graphical interface by providing information about the current inventory, features, and prices of available products. Your responses should be personalized and based on real-time inventory data. who knows about these products: {product_info}"
        else:
            system_message = "You are an e-commerce assistant."

        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": request.question}
            ]
        )

        response_content = completion.choices[0].message
        return {"response": response_content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))