# src/magic_logging/__init__.py
"""
magic-logging: 统一日志系统
"""

from .core.logger import Logger, ConsoleHandler, LogLevel

# 导出核心函数（转发到类方法）
get_logger = Logger.get_logger
setup_logging = Logger.setup

__all__ = [
    "get_logger",
    "setup_logging",
    "Logger",
    "ConsoleHandler",
    "LogLevel",
]