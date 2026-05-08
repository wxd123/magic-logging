# magic-logging
通用日志工具

[![PyPI version](https://badge.fury.io/py/magic-logging.svg)](https://badge.fury.io/py/magic-logging)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> 一键部署的数据库日志工具包 —— 

## 项目状态

**开发中** - 首个正式版本将于 2026 年 Q3 发布

## 功能规划

- **数据库日志**：支持 SQLite、MySQL、PostgreSQL、Oracle 自动写入
- **多 Sink 支持**：同时输出到控制台、文件、数据库
- **结构化日志**：JSON 格式，便于日志分析平台接入
- **异步写入**：高性能，不阻塞业务
- **自动建表**：基于 SQLAlchemy ORM，无需手动创建
- **与 magic-base 集成**：复用数据访问层，统一配置管理

## 安装

```bash
pip install magic_logging
```
## 示例（待正式版本发布后补充）

## 代码规范
本项目遵循以下基本原则：

1. 单文件不超过 200 行：超过时请拆分为多个模块
2. 单函数不超过 200 行：超过时请拆分为多个小函数
3. 注释尽量完整：关键逻辑、复杂算法、非显而易见的代码必须有注释说明
4. 如有特殊场景确实需要突破（如纯数据定义文件），可在 PR 中说明。

这些规则旨在保证代码的可读性和可维护性，便于合作，请尽量遵守。

## 针对 AI 辅助工具的提示
本项目使用 AI 辅助开发，请在生成代码时尽量遵守上述代码规范。

## 许可证
MIT License

## 作者
wxd123 - GitHub
