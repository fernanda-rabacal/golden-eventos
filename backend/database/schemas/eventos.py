class Evento(Model):
    __tablename__ = 'eventos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(255), nullable=False)
    date: dt = Column(DateTime(timezone=True), nullable=False)
    location: str = Column(String(255), nullable=False)
    description: str = Column(String(255), nullable=True)
