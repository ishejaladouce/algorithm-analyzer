from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AlgoAnalysis(Base):
    __tablename__ = "algo_analysis"

    id = Column(Integer, primary_key=True, autoincrement=True)
    algo = Column(String(100), nullable=False)
    items = Column(Integer, nullable=False)
    steps = Column(Integer, nullable=False)
    start_time = Column(BigInteger, nullable=False)
    end_time = Column(BigInteger, nullable=False)
    total_time_ms = Column(Integer, nullable=False)
    time_complexity = Column(String(50), nullable=False)
    path_to_graph = Column(String(255), nullable=True)
