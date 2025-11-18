from sqlalchemy.orm.attributes import InstrumentedAttribute
from typing import Protocol, Any
class Base_model(Protocol):
    id: InstrumentedAttribute[Any]