
from src.infra.Database.extensions import db

class Subscriptions_b3(db.Model):
    __tablename__ = "subscriptions_b3"

    id = db.Column(db.Integer, primary_key=True)
    approvedOn = db.Column(db.Date, nullable=False)
    assetIssued = db.Column(db.String(45))
    isinCode = db.Column(db.String(45))
    lastDatePrior = db.Column(db.Date, nullable=False)
    percentage = db.Column(db.Numeric(30, 13), nullable=False)

    priceUnit = db.Column(db.Numeric(30, 13), nullable=False)
    remarks = db.Column(db.String(45))
    subscriptionDate = db.Column(db.Date, nullable=False)
    tradingPeriod = db.Column(db.String(45))
