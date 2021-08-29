from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import EmailType
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(EmailType)
    city = Column(String(20))

    def __init__(self, email=None, name=None, city=None):
        self.name = name
        self.email = email
        self.city = city

    def __str__(self):
        return f"{self.name} having email {self.email}"

    def to_tuple(self):
        return self.email, self.name, self.city