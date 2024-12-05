from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, func
from .pg import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True) #0
    username = Column(String(50), unique=True, nullable=False) #1
    password_hash = Column(String(255), nullable=False) #2
    created_at = Column(DateTime, default=func.now()) #3


class Survey(Base):
    __tablename__ = 'surveys'
    id = Column(Integer, primary_key=True) #0
    title = Column(String(255), nullable=False) #1
    description = Column(Text) #2
    created_by = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=True) #3
    created_at = Column(DateTime, default=func.now()) #4
    is_active = Column(Boolean, default=True) #5
    is_single_choice = Column(Boolean, default=False) #6
    user = relationship('User', backref='surveys') #7
    #vote = relationship('Vote', backref='surveys', cascade="all,delete")



class Option(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True) #0
    survey_id = Column(Integer, ForeignKey('surveys.id', ondelete="CASCADE"), nullable=False) #1
    option_text = Column(String(255), nullable=False) #2


class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True) #0
    survey_id = Column(Integer, ForeignKey('surveys.id', ondelete="CASCADE"), nullable=False) #1
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=True) #2
    voter_ip = Column(String(50), nullable=True) #3
    created_at = Column(DateTime, default=func.now()) #4


class VoteOption(Base):
    __tablename__ = 'vote_options'
    id = Column(Integer, primary_key=True) #0
    vote_id = Column(Integer, ForeignKey('votes.id', ondelete="CASCADE"), nullable=False) #1
    option_id = Column(Integer, ForeignKey('options.id', ondelete="CASCADE"), nullable=False) #2
