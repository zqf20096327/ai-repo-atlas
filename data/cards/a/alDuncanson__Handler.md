# alDuncanson/Handler

⭐ 46 · Python · GPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/alDuncanson/Handler) · [官网](https://handler.alduncanson.com) · 个人维护

**终端里的 A2A 协议客户端，供工程师构建测试 agentic 系统**

面向软件工程师的 A2A 协议开源客户端：提供交互式 TUI、可脚本化的 CLI（结构化输出）以及 MCP 服务器，使其他 agent 可直接对接 A2A 服务。支持流式回复收发文本/文件/结构化数据、任务管理与推送通知配置，传输层默认 JSON-RPC 与 HTTP+JSON（gRPC 需 extra），认证覆盖 bearer、API key、mTLS、OAuth2 等，凭据仅保存在配置来源。通过 PyPI 包安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 交互式 TUI + 可脚本化 CLI + MCP 服务器三种使用形态
- 流式收发文本、文件与结构化数据，支持任务管理与推送通知配置
- 支持 bearer/API key/mTLS/OAuth2/OIDC 等多种认证，凭据不落第三方主机
- 文档以 agent skill 形式提供，并可经 MCP 服务器查询

## 适用场景

- 在终端中与 A2A 服务器对话并查看 agent card
- 脚本化测试与运维 agentic 系统，获取结构化输出
- 让其他 agent 通过 MCP 集成 A2A 服务

## 场景标签

 · 领域:AI agent 基础设施/协议客户端

## 证据(README 行号)

> L10: Handler is an open-source A2A protocol
> L13: MCP server that lets other agents integrate with A2A services directly. Handler

## 星数曲线

```mermaid
xychart-beta
    title "alDuncanson/Handler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f471b6555fa4` · [字段定义](../../DATASET.md)*
