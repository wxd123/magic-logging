# src/magic_logging/core/logger.py
from typing import List, Optional
from enum import Enum
from datetime import datetime


class LogLevel(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40


class LogRecord:
    def __init__(self, level: LogLevel, message: str, name: str = None):
        self.level = level
        self.message = message
        self.name = name or "root"
        self.timestamp = datetime.now()
        self.module = None
        self.function = None
        self.line = None


class BaseHandler:
    def emit(self, record: LogRecord):
        raise NotImplementedError


class ConsoleHandler(BaseHandler):
    def emit(self, record: LogRecord):
        print(f"[{record.timestamp}] {record.level.name}: {record.message}")


class Logger:
    """日志器，支持单例模式和多个 Handler"""
    
    _default_logger: Optional['Logger'] = None
    
    def __init__(self, name: str = "root"):
        self.name = name
        self.handlers: List[BaseHandler] = []
    
    # ========== 单例管理（类方法） ==========
    
    @classmethod
    def get_logger(cls, name: Optional[str] = None) -> 'Logger':
        """
        获取全局 Logger 实例（单例模式）
        
        Args:
            name: logger 名称（预留，暂未使用）
            
        Returns:
            全局唯一的 Logger 实例
        """
        if cls._default_logger is None:
            cls._default_logger = cls()
            # 默认添加控制台输出
            cls._default_logger.add_handler(ConsoleHandler())
        return cls._default_logger
    
    @classmethod
    def setup(cls, config: dict = None):
        """
        配置日志系统（预留接口）
        
        Args:
            config: 配置字典，可指定日志级别、输出格式等
        """
        logger = cls.get_logger()
        # TODO: 根据 config 配置 logger
        return logger
    
    # ========== 实例方法 ==========
    
    def add_handler(self, handler: BaseHandler):
        """添加日志处理器"""
        self.handlers.append(handler)
        return self
    
    def _log(self, level: LogLevel, message: str):
        record = LogRecord(level, message, self.name)
        for handler in self.handlers:
            handler.emit(record)
    
    def debug(self, msg: str):
        self._log(LogLevel.DEBUG, msg)
    
    def info(self, msg: str):
        self._log(LogLevel.INFO, msg)
    
    def warning(self, msg: str):
        self._log(LogLevel.WARNING, msg)
    
    def error(self, msg: str):
        self._log(LogLevel.ERROR, msg)