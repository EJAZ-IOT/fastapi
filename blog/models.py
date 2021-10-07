import re
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    bookmarkid = Column(Integer, ForeignKey('bookmark.bid'))

    mark = relationship("Bookmark", back_populates= "blogs")

class Bookmark(Base):
    __tablename__ = 'bookmark'
    id = Column(Integer, primary_key=True, index=True)
    bid = Column(Integer)          #bid = blog id
    btitle = Column(String)

    blogs = relationship("Blog", back_populates="mark")



    


