from . import db

class PropertyProfile(db.Model):

    __tablename__ = 'property_profile'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String())
    description = db.Column(db.String())
    num_bedrooms = db.Column(db.String())
    num_bathrooms=db.Column(db.String())
    price = db.Column(db.String())
    prop_type = db.Column(db.String())
    location = db.Column(db.String())
    photo = db.Column(db.String())
    
    def __init__(self, title, description, num_bedrooms, num_bathrooms, price, prop_type, location, photo):
        self.title=title
        self.description=description
        self.num_bedrooms=num_bedrooms
        self.num_bathrooms=num_bathrooms
        self.price=price
        self.prop_type=prop_type
        self.location=location
        self.photo=photo