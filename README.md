# e-chat-backend


```
Architecture (inspired in clean architecture)
├── LICENSE                     
├── README.md                   
└── app
    ├── main.py                 # Entry point of the FastAPI application
    ├── models
    │   ├── database.py         # Database connection setup (Frameworks and Drivers)
    │   └── product.py          # Data models related to products (Entities)
    ├── routers
    │   └── products_router.py  # API routes (Interface Adapters)
    ├── schemas
    │   ├── chat_request.py     # Pydantic models for chat-related requests (Entities)
    │   └── product.py          # Pydantic models for product-related data (Entities)
    └── settings.py             # Configuration settings (Frameworks and Drivers)
```


![image](https://github.com/JosephSC0121/e-chat-backend/assets/119358195/407b040d-0084-4b3e-bd44-e35ce629e17c)
![image](https://github.com/JosephSC0121/e-chat-backend/assets/119358195/06a67b0a-9b1e-432d-b113-808593a60c0b)

