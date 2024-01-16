# from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
# from sqlalchemy.orm import relationship
# from app.schemas import funding_opportunityInDB
# from models import Business, Requirement

# from app.db.base_class import Base

# class Funding_Opportunity(Base):
    
#     __tablename__ = "funding_opportunity"
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     requirement_id = Column(Integer, ForeignKey('funding_requirements.id'))
#     data = Column(String, index = True)

#     # Define relationships

#     def to_schema(self):
#         return funding_opportunityInDB(

#         id = self.id,
#         user_id = self.user_id,
#         requirement_id = self.requirement_id,
        
#         data = self.data

#         )