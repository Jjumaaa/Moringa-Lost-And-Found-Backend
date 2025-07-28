from app import app
from config import db
from models import User, Item, Claim, Comment, Reward, Image
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()