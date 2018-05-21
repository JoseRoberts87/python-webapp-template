from sqlalchemy import Column, Integer, String
from model.base import Base

class Locations(Base):

    __table__ = 'arde_locations'

    location_id = Column(String(45))
    name = Column(String(45))
    type = Column(String(45))
    level = Column(Integer)
    status = Column(String(45))

    def __repr__(self):
        return "<Locations(location_id='%s', name='%s', " \
               "type='%s', level='%s', status='%s')>" % (
            self.location_id, self.name,
            self.type, self.level, self.status)