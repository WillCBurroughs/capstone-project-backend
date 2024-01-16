# from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
# from sqlalchemy.orm import relationship
# from app.schemas import user_roleInDB
# from models import Business, Requirement

# from app.db.base_class import Base

# class Funding_Opportunity(Base):
    
#     __tablename__ = "user_role"
    
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index = True)

#     # Define relationships


#     def to_schema(self):
#         return user_roleInDB(

#             id = self.id,
#             title = self.title

#         )