# ntk148v/alertmanager-mcp-server

⭐ 25 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/ntk148v/alertmanager-mcp-server) · 个人维护

**让 AI 助手查询和管理 Prometheus Alertmanager 的 MCP 服务器**

面向 Prometheus Alertmanager 的 Model Context Protocol (MCP) 服务器，供 Claude Desktop 等 AI 助手通过自然语言查询告警、静默、接收器与告警组，并支持创建/更新/删除静默、创建告警。遵循 Alertmanager API v2，支持 Basic auth 环境变量认证与多租户（Mimir/Cortex，tenant 启动时固定、忽略请求头传入值以防客户端任意选择租户）。工具层内置分页以避免 LLM 上下文溢出。传输支持 stdio/http/sse，http/sse 模式可设置 Bearer API key。需 Python 3.12+ 与可访问的 Alertmanager 实例，提供 Smithery 一键安装、源码运行与 Docker 预构建镜像三种途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 暴露遵循 Alertmanager API v2 的查询与管理工具（告警/静默/接收器/告警组）
- 分页机制限制单次返回条目数，避免 LLM 上下文溢出
- stdio/http/sse 三种传输模式，http/sse 支持 Bearer API key 认证
- 多租户支持且 tenant 启动时固定，忽略请求头传入值

## 适用场景

- 在 Claude Desktop 中用自然语言查看当前告警与详情
- 通过对话为告警创建限时静默
- 在大量告警环境下分页浏览，避免上下文耗尽

## 场景标签

 · 领域:DevOps/可观测性

## 证据(README 行号)

> L14: Prometheus Alertmanager MCP is a Model Context Protocol (MCP) server for Prometheus Alertmanager. It enables AI ass
> L18: - [x] Query Alertmanager status, alerts, silences, receivers, and alert groups

## 星数曲线

```mermaid
xychart-beta
    title "ntk148v/alertmanager-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bd63fece9eab` · [字段定义](../../DATASET.md)*
