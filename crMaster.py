from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship, Session, aliased
from datetime import datetime, timedelta, date
import enum
import sys
import os
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()
engine = create_engine(f"mysql+mysqlconnector://{os.environ['USER_NAME']}:{os.environ['PASSWORD']}@{os.environ['PI']}/{os.environ['MAIN_DB']}" )


class crCards(Base):
    __tablename__ = "cr_cards"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    current_level = Column(Integer)
    star_level = Column(Integer)
    count = Column(Integer)

class crCard_Icon(Base):
    __tablename__ = 'cr_card_icons'
    id = Column(Integer, ForeignKey("cr_cards.id"))
    icon_url = Column(String(255))
    size = Column(String(255))

class crDeck(Base):
    __tablename__ = 'cr_deck_map'
