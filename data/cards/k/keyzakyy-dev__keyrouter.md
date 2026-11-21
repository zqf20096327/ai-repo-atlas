# keyzakyy-dev/keyrouter

⭐ 6 · JavaScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/keyzakyy-dev/keyrouter) · [官网](https://router.keyzakyy.com) · 个人维护 · 中文 README

**自托管 AI 路由网关：一个端点接入 40+ 提供商**

自托管的 AI 请求路由器，位于用户的编码工具与 40+ 提供商（100+ 模型）之间，提供统一本地端点，同时兼容 OpenAI 与 Claude API 格式，并做格式互译。机制包括：压缩工具输出以减少输入 token 的 RTK、订阅→低价→免费三级自动降级、订阅配额跟踪、多账号负载分摊、OAuth 自动刷新，以及为 Claude Code 等 9 种工具一键写入配置的 connect 命令。数据（密钥、日志、用量）全部存本地 SQLite。运行需 Node.js ≥22.23，支持 npm/Docker/源码三种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一端点同时兼容 OpenAI 与 Claude API，支持格式互译（含 Gemini/Kiro/Vertex/Cursor）
- RTK 工具输出压缩与三级 fallback 路由（订阅→低价→免费）
- 订阅配额跟踪、多账号负载分摊、OAuth 自动刷新
- keyrouter connect 一键为 10 种 CLI 编码工具写入配置，原文件备份为 *.bak-keyrouter

## 适用场景

- 为多个已付费的 AI 订阅提供统一的本地 API 端点
- 在请求中途自动从订阅配额降级到低价或免费提供商
- 管理多个提供商账号与 API key，避免逐工具配置
- 在本地或自建 VPS 上自托管路由并跟踪 token 用量与成本

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L20: |**What it is**|A self-hosted router that sits between your AI coding tools and 40+ providers (100+ models)|
> L22: |**Endpoint**|`http://localhost:20131/v1` — speaks OpenAI **and** Claude API|
> L150: |**Format translation**|OpenAI ↔ Claude ↔ Gemini ↔ Kiro ↔ Vertex ↔ Cursor|One endpoint into any CLI tool|

## 星数曲线

```mermaid
xychart-beta
    title "keyzakyy-dev/keyrouter 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-21"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-08 5 → 2026-11-21 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `213988da23f3` · [字段定义](../../DATASET.md)*
