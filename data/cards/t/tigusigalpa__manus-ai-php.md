# tigusigalpa/manus-ai-php

⭐ 24 · PHP · MIT · 推送 2026-10-09 · [GitHub](https://github.com/tigusigalpa/manus-ai-php) · 个人维护

**Manus AI API v2 的 PHP/Laravel 客户端 SDK**

面向 PHP 8.2+ 开发者的 Manus API v2 独立客户端库，覆盖创建与管理 agent 任务、消息轮询、附件三步上传（预签名 URL）、webhook 注册与签名验证，以及项目/技能/Agent/用量/网站等 v2 端点。支持 API key 与 OAuth Bearer 两种认证，提供可选的 Laravel 集成：自动发现的服务提供者、Facade 与 Artisan 命令。限制：API 行为与可用配置由 Manus 侧控制；listFiles 已废弃并抛出 ValidationException。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Manus API v2 任务、文件、webhook、项目、用量等端点
- Laravel 自动发现 + Facade + Artisan 命令（manus-ai:test/task 等）
- API key 与 OAuth Bearer 双认证，TaskAttachment 多来源附件助手
- 测试套件使用 mock HTTP 响应，不调用 Manus

## 适用场景

- 在 PHP/Laravel 应用中接入 Manus API 创建与管理 agent 任务
- 通过 webhook 接收任务生命周期通知并做签名验证
- 上传附件并把 file_id 关联到任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: An independent PHP 8.2+ client for Manus API v2, with optional Laravel integration. It creates and manages agent ta
> L153: ## Laravel

## 星数曲线

```mermaid
xychart-beta
    title "tigusigalpa/manus-ai-php 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fd76c720085e` · [字段定义](../../DATASET.md)*
