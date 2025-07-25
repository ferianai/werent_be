from instance.database import db
from shared import crono


class Products(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    condition = db.Column(db.String(50), nullable=False)  # e.g., new, used

    image_url = db.Column(db.String(255), nullable=True)  # URL to product image
    created_at = db.Column(db.DateTime, default=crono.now)
    updated_at = db.Column(db.DateTime, default=crono.now, onupdate=crono.now)

    def __repr__(self):
        return f"<Product {self.name} - ${self.price}>"
