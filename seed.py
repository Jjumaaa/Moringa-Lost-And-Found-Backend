from app import app
from config import db
from models import User, Item, Claim, Comment, Reward, Image
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def seed():
    with app.app_context():
        print(" Clearing old data...")
    db.session.query(Image).delete()
    db.session.query(Reward).delete()
    db.session.query(Comment).delete()
    db.session.query(Claim).delete()
    db.session.query(Item).delete()
    db.session.query(User).delete()
    db.session.commit()
      
