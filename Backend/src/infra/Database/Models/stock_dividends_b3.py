from dataclasses import dataclass
from datetime import date
from src.infra.Database.extensions import db

class Stock_dividends_b3(db.Model):
    __tablename__ = "stock_dividends_b3"

    id = db.Column(db.Integer, primary_key=True)
    assetIssued = db.Column(db.String(45))
    cnpj = db.Column(db.String(16))
    factor = db.Column(db.Numeric(30, 13), nullable=False)
    approvedOn = db.Column(db.Date, nullable=False)
    isinCode = db.Column(db.String(45))
    label = db.Column(db.String(45))
    lastDatePrior = db.Column(db.Date, nullable=False)
    remarks = db.Column(db.String(45))