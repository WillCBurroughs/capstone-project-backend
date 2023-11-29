# from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
# from sqlalchemy.orm import relationship
# from app.schemas import funding_opp_requirementsInDB
# from models import Business, Requirement

# from app.db.base_class import Base

# class Funding_Opp_Requirements(Base):
    
#     __tablename__ = "funding_opp_requirement"
    
#     id = Column(Integer, primary_key=True, index=True)
#     fund_id = Column(Integer, ForeignKey('fund.id'))
#     requirement_id = Column(String, ForeignKey('funding_requirements.id'))
    
#     # Used to define data to be parsed for testing if qualified 
#     data = Column(String, index = True)

#     # Define relationships


#     def to_schema(self):
#         return funding_opp_requirementsInDB(

#         id = self.id,
#         fund_id = self.fund_id,
#         requirement_id = self.requirement_id,
        
#         data = self.data

#         )