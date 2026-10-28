# markolofsen/django-cfg

⭐ 24 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/markolofsen/django-cfg) · [官网](https://djangocfg.com) · 个人维护

**类型安全的 Django 配置框架，附带 AI 与企业应用组件**

基于 Pydantic v2 模型替换 Django settings.py 的框架：启动时校验配置、提供 IDE 补全，并集成实时 WebSockets（Centrifugo）、gRPC 双向流、从 DRF OpenAPI schema 生成 TypeScript/Python/Go 客户端、Stripe 支付引擎及 8 个企业应用。AI 部分：供 AI 助手访问文档的 MCP server、Pydantic AI 集成、ChromaDB 向量库与 RAG 支持。通过 curl 安装脚本或 pip 安装，附 Docker Compose 与 Traefik 配置，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pydantic v2 类型安全配置替换 settings.py，启动时校验
- 从 DRF OpenAPI schema 生成 TypeScript/Python/Go 类型化 API 客户端
- MCP server 供 AI 助手访问文档，含 ChromaDB 向量库与 RAG 支持
- 集成 Centrifugo 实时 WebSockets、gRPC 流、Stripe 支付与 8 个企业应用

## 适用场景

- 用类型安全配置管理 Django 项目，减少配置错误
- 自动生成前后端类型化 API 客户端
- 搭建含实时通信、支付与 AI 助手文档访问的 Django 应用

## 场景标签

`代码生成` `RAG` · 领域:编码与开发

## 证据(README 行号)

> L19: **Django-CFG** is a next-generation Django framework that replaces `settings.py` with **type-safe Pydantic v2 model
> L29: - ✅ **AI-native docs** - First Django framework with MCP server for AI assistants
> L155: - MCP server for AI assistants

## 星数曲线

```mermaid
xychart-beta
    title "markolofsen/django-cfg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1325f4311b51` · [字段定义](../../DATASET.md)*
