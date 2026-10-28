# Hoopoes/FastStart

⭐ 34 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Hoopoes/FastStart) · 个人维护

**FastAPI 后端微服务模板库，多分支提供扩展**

面向后端开发者的 FastAPI 起步模板：以 main 分支提供精简脚手架，含 JWT/OAuth2 认证、pydantic DTO、版本化路由、异步 pytest 测试与日志配置；base 分支补充 OpenAPI 文档、错误处理与中间件，sqlalchemy 分支集成 Async SQLAlchemy，log-viewer 分支内置浏览器日志查看器。使用 uv 管理依赖，git clone 指定分支后 uv sync 安装、uv run 启动。附带 AGENTS.md 供 AI 编码代理参考项目约定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- main/base/sqlalchemy/log-viewer 四个分支按需选用
- 内置 JWT/OAuth2 认证流程与演示用户
- Async SQLAlchemy 异步数据库分支
- 异步 pytest 测试套件覆盖认证与用户 CRUD

## 适用场景

- 快速搭建带认证的 FastAPI 后端微服务
- 在模板基础上扩展异步数据库与日志查看功能
- 为 AI 编码代理提供项目结构约定（AGENTS.md）

## 场景标签

 · 领域:Web 后端开发

## 证据(README 行号)

> L12: **FastStart** is a modular and flexible starting point for building backend microservices with FastAPI. This reposi
> L98:  - **AGENTS.md**: Guide for AI coding agents — setup, structure, and conventions.

## 星数曲线

```mermaid
xychart-beta
    title "Hoopoes/FastStart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `63c0711eb6bd` · [字段定义](../../DATASET.md)*
