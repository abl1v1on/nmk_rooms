from sqlalchemy import Table, Column, ForeignKey

from . import Base


rooms_equipments = Table(
    'rooms_equipments',
    Base.metadata,
    Column('room_id', ForeignKey('rooms.id'), primary_key=True),
    Column('equipment_id', ForeignKey('equipments.id'), primary_key=True)
)
