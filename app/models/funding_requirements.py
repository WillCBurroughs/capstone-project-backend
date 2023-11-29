from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.schemas import funding_requirementsInDB
from models import Business, Requirement

from app.db.base_class import Base

class Funding_Requirements(Base):
    
    __tablename__ = "funding_requirement"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index = True)
    data = Column(String, index = True)



    # Define relationships


    def to_schema(self):
        return funding_requirementsInDB(

        id = self.id,
        title = self.title,
        data = self.data

        )