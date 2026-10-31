# Dot-Fun/fathom-mcp

⭐ 14 · Python · MIT · 推送 2026-03-20 · [GitHub](https://github.com/Dot-Fun/fathom-mcp) · 组织维护

**访问 Fathom AI 会议数据的 MCP 服务器**

基于 FastMCP 的 Model Context Protocol 服务器，封装 Fathom AI API，向 MCP 客户端（如 Claude Desktop、Codex）提供 7 个工具：列出会议（含转录/摘要/行动项/CRM 匹配的可选包含）、获取摘要、获取带说话人与时间戳的转录、列出团队与成员、创建/删除 webhook；另暴露 API 信息与限速两个资源。认证依赖用户级 FATHOM_API_KEY，全局限速 60 次/60 秒。以 Python 源码形式提供，支持 stdio 与 HTTP 两种传输方式，已用真实 Fathom API 数据测试。

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

- 7 个工具覆盖会议/转录/摘要/团队/webhook 操作
- list_meetings 支持按参与者、日期、团队过滤并可包含转录与摘要
- 支持 stdio 与 HTTP 两种运行方式
- 提供 Claude Desktop 与 Codex 的接入配置示例

## 适用场景

- 在 Claude Desktop 或 Codex 中通过对话查询我的会议记录与摘要
- 为团队会议事件配置 webhook 通知
- 让 AI 客户端检索特定参与者的会议与行动项

## 场景标签

 · 领域:办公自动化/AI 工具接入

## 证据(README 行号)

> L7: A Model Context Protocol (MCP) server for interacting with the Fathom AI API. This server provides tools for accessi
> L84: ### Integrating with Claude Desktop

## 星数曲线

```mermaid
xychart-beta
    title "Dot-Fun/fathom-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b03369b474c6` · [字段定义](../../DATASET.md)*
