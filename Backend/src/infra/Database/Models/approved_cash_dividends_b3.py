from dataclasses import dataclass
from datetime import date
from src.infra.Database.extensions import db

class Approved_cash_dividends_b3(db.Model):
    __tablename__ = "approved_cash_dividends_b3"

    id = db.Column(db.Integer, primary_key=True)

    assetIssued = db.Column(db.String(45))
    paymentDate = db.Column(db.Date)
    rate = db.Column(db.Numeric(20, 10), nullable=False)
    relatedTo = db.Column(db.String(45))
    isinCode = db.Column(db.String(45))
    approvedOn = db.Column(db.Date)
    label = db.Column(db.String(45))
    lastDatePrior = db.Column(db.Date, nullable=False)
    remarks = db.Column(db.String(45))