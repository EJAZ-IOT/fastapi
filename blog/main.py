from fastapi import FastAPI, Depends, status, Response, HTTPException
from starlette.requests import Request
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, bookmarkid =request.bookmarkid)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.post('/bookmark', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Bookmark, db: Session = Depends(get_db)):
    new_bk = models.Bookmark(btitle =request.btitle, bid =request.bid)
    db.add(new_bk)
    db.commit()
    db.refresh(new_bk)
    return new_bk


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destry(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/blog/{id}', status_code=200)
def update(id,request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Blog with id {id} not found")
    
    blog.update(request.dict())
    db.commit()
    return 'updated sucessfully'



@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs =db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200, response_model = schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                           detail=f"Blog with the id {id} is not avialable")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f"Blog with the id {id} is not avialable"}
    return blog

'''To get all bookmark relatd to a blog using blog id'''

@app.get('/bookmark/{bid)', status_code=200)         
def show(bid, response: Response, db: Session = Depends(get_db)):
    bookmark = db.query(models.Bookmark).filter(models.Bookmark.bid == bid).all()
    return bookmark
 