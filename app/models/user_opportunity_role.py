# from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
# from sqlalchemy.orm import relationship
# from app.schemas import user_opportunity_roleInDB
# from models import Business, Requirement

# from app.db.base_class import Base

# class user_opportunity_role(Base):
    
#     __tablename__ = "user_opportunity_role"
    
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     opp_id = Column(Integer, ForeignKey('opportunity.id'))
#     role_id = Column(Integer, ForeignKey('user_roles.id'))

#     # Define relationships


#     def to_schema(self):
#         return user_opportunity_roleInDB(

#         id = self.id,
#         user_id = self.user_id,
#         opp_id = self.opp_id,
#         role_id = self.role_id

#         )