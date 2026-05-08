# magic_log/db_sink.py
from magic_base.data_access.manager import DatabaseManager
from magic_base.data_access.model import MagicBaseModel
from sqlalchemy import Column, String, DateTime, Integer, Text
from datetime import datetime
import json

class LogEntry(MagicBaseModel):
    """日志条目模型（继承 base 的 ORM 基类）"""
    __tablename__ = "log_entries"
    
    level = Column(String(20), nullable=False)
    message = Column(Text, nullable=False)
    module = Column(String(100))
    function = Column(String(100))
    line = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now)
    extra = Column(Text)  # JSON 格式的额外信息

class DatabaseSink:
    """loguru 的数据库 Sink"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self._ensure_table()
    
    def _ensure_table(self):
        """确保表存在（使用 base 的数据库初始化）"""
        with self.db_manager.engine.begin() as conn:
            LogEntry.metadata.create_all(conn)
    
    def write(self, record: dict):
        """loguru 调用的写入方法"""
        with self.db_manager.get_session() as session:
            log = LogEntry(
                level=record["level"].name,
                message=record["message"],
                module=record.get("name", ""),
                function=record.get("function", ""),
                line=record.get("line", 0),
                extra=json.dumps(record.get("extra", {}))
            )
            session.add(log)
            session.commit()