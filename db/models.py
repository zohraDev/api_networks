from sqlalchemy import (Boolean,
                        Column,
                        ForeignKey,INT, FLOAT, Text)


from db.database import Base


class Operators(Base):
    __tablename__ = "operators"
    code = Column(INT, primary_key=True, nullable=False)
    name = Column(Text)


class NetWorkOffers(Base):
    __tablename__ = "networkoffers"
    id = Column(INT, primary_key=True, autoincrement=True, nullable=False)
    code = Column(INT, ForeignKey('operators.code', ondelete="CASCADE"), nullable=False)
    long = Column(FLOAT)
    lat = Column(FLOAT)
    g2_offer = Column(Boolean)
    g3_offer = Column(Boolean)
    g4_offer = Column(Boolean)
    # operator = relationship("Operators", back_populates="owner")
