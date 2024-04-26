from extensions import db

class Categorie(db.Model):
    __tablename__ = 'categorie' 
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(100), nullable=False)
    