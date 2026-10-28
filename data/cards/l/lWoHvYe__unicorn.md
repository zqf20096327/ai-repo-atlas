# lWoHvYe/unicorn

⭐ 47 · Java · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/lWoHvYe/unicorn) · [官网](https://lwohvye.github.io/unicorn/) · 个人维护 · 中文 README

**基于 Java 25/Spring Boot 4 的前后端分离脚手架，含 Spring AI 示例模块**

在 eladmin 项目基础上扩展的后端脚手架，采用 Java 25（Core 模块支持 17-21/24/25）、Spring Boot 4、JPA、Spring Security、Redis、RabbitMQ、Vue。功能覆盖用户/角色/菜单/字典管理、定时任务、代码生成器、多数据源读写分离（ShardingSphere）、OAuth2 示例等，各模块基本可插拔。unicorn-ai 模块集成 Spring AI 2.0 示例（Chat/RAG/MCP），含流式对话、向量检索、MCP Server/Client。运行需 Java 25、MySQL、Redis、RabbitMQ 等环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 各模块按功能拆分、基本可插拔，可按需只引入部分模块
- unicorn-ai 集成 Spring AI 2.0 示例（Chat/RAG/MCP）
- ShardingSphere 多数据源读写分离 + Redisson 缓存读写分离
- 支持 Virtual Threads（Runtime >= 21 时启用）

## 适用场景

- 作为 To B 管理系统后端脚手架快速搭建项目
- 参考 Spring AI 2.0 的 Chat/RAG/MCP 集成示例
- 搭建带 OAuth2 授权/资源服务器的 To C 业务后端

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L49: 一个基于最新的Java 25(17, 21) 版本、 Spring Boot 4.x、 Jpa、 Spring Security、Redis、RabbitMQ、Vue的前后端分离的脚手架。
> L74: - 集成 Spring AI 2.0 示例（Chat/RAG/MCP）：流式对话、对话记忆、结构化输出、工具调用、ETL/向量检索、MCP Server/Client。
> L116: - `unicorn-ai` Spring AI 2.0 示例集合：Chat（流式/记忆/结构化输出/工具/Agent）、RAG（ETL/向量检索/Query Rewrite）、MCP Server/Client，详见 unic


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d2b77b472589` · [字段定义](../../DATASET.md)*
