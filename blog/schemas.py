from pydantic import BaseModel


   
class Bookmark(BaseModel):
    bid: int
    btitle: str
    

class ShowBookmark(BaseModel):
    btitle: str
    class Config():
        orm_mode = True
     




class Blog(BaseModel):
    title: str
    body: str
    bookmarkid: int
    
class ShowBlog(BaseModel):
    title: str
    body: str
    mark: ShowBookmark
    class Config():
        orm_mode = True


   