from pydantic import BaseModel



   
class Bookmark(BaseModel):
    bid: int
    btitle: str


class Blog(BaseModel):
    title: str
    body: str
    
    


   