# homeassistant-ai/ha-mcp

⭐ 8,124 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/homeassistant-ai/ha-mcp) · [官网](https://homeassistant-ai.github.io/ha-mcp/) · 组织维护

**让 Claude/ChatGPT 等 AI 助手通过 MCP 配置与自动化 Home Assistant**

提供 87 个工具的 MCP 服务器，将 Home Assistant 暴露给 MCP 客户端，使其能读取和控制家庭自动化实例。推荐方式是通过 Home Assistant 内置 Marketplace 安装 in-process 集成，适用于 OS/Supervised/Container/Core 全部安装类型；另有 add-on、Docker、PyPI/uvx、本地 stdio 等安装路径。远程访问经 Nabu Casa、Webhook Proxy 或 OpenAI Tunnel；stdio 传输存在已知连接问题，仅建议用于演示测试。需要管理员长期访问令牌或专用账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 87 个 MCP 工具管理 Home Assistant
- 支持集成、add-on、Docker、PyPI/uvx、stdio 多种安装方式
- 远程访问支持 Nabu Casa、Webhook Proxy、OpenAI Tunnel 与 OIDC 认证
- 自带侧边栏设置面板管理工具、功能开关与备份

## 适用场景

- 用 Claude 或 ChatGPT 对话式配置和自动化 Home Assistant
- 在 Container/Core 安装上通过 Docker/PyPI 独立运行 MCP 服务器
- 通过演示环境先试用再接入自己的 Home Assistant

## 场景标签

 · 领域:智能家居/自动化

## 证据(README 行号)

> L5:  # HA-MCP — Manage Home Assistant with AI
> L18:  Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants.
> L24: The recommended way to run ha-mcp is the **HA-MCP integration**. It installs into Home Assistant through the built-

## 星数曲线

```mermaid
xychart-beta
    title "homeassistant-ai/ha-mcp 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 4890 --> 8418
    line [5184, 5198, 5233, 5277, 5303, 5323, 5352, 5370, 5379, 5392, 5198, 5505, 6551, 7225, 7675, 7749, 7814, 7868, 7907, 7951, 7984, 8000, 8021, 8035, 8070, 8088, 8124]
```

2026-10-24 5,184 → 2026-11-26 8,124（+2,940）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `b7f29c8ba8f5` · [字段定义](../../DATASET.md)*
