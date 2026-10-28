# microsoft/Agents-for-python

⭐ 216 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/microsoft/Agents-for-python) · 组织维护

**微软官方 Python SDK：构建多渠道企业 agent 应用**

Microsoft 365 Agent SDK 的 Python 组件仓库，提供构建面向 M365、Teams、Copilot Studio、Webchat 等平台的全栈多渠道 agent 所需的开发模块，并支持 Facebook Messenger、Slack、Twilio 等第三方集成。以约 10 个 PyPI 包形式分发，覆盖 Activity 协议类型、aiohttp/FastAPI/Teams 托管、瀑布对话系统、Azure Blob/CosmosDB 存储扩展、MSAL 与 Entra ID 认证等，多个包明确标注替代旧版 botbuilder 系列。要求 Python 3.10 及以上，推荐 3.11+。

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

- 多渠道托管包：aiohttp、FastAPI、MS Teams
- 瀑布对话与多轮会话管理系统（dialogs 包）
- Azure Blob 与 CosmosDB 存储扩展、MSAL/Entra ID 认证包
- 多个包明确替代 botbuilder-core 等旧 Bot Framework 组件

## 适用场景

- 为 Teams 或 Webchat 构建企业对话 agent
- 将 Bot Framework Python 项目迁移到新 SDK
- 以 FastAPI/aiohttp 为宿主托管 agent 服务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: The Microsoft 365 Agent SDK simplifies building full stack, multichannel, trusted agents for platforms including M36
> L8: The M365 Agent SDK is a comprehensive framework for building enterprise-grade agents, enabling developers to integra

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Agents-for-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 215 --> 217
    line [216, 216]
```

2026-10-18 216 → 2026-10-28 216（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a1cb006446a2` · [字段定义](../../DATASET.md)*
