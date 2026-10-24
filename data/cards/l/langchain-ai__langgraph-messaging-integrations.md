# langchain-ai/langgraph-messaging-integrations

⭐ 66 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/langchain-ai/langgraph-messaging-integrations) · 组织维护

**将 LangGraph 应用接入 Slack 的消息事件集成代码，开发者用**

由 LangChain 团队维护的集成示例工程：把 Slack 事件路由文件复制进现有 LangGraph 应用目录，通过 LangGraph 平台的自定义路由功能部署。服务端用 Slack Bolt SDK 注册 webhook 接收消息/@提及，打包为 chat messages 转发给 LangGraph 应用，应用完成后经回调 webhook 取最新回复发回 Slack。需自建 Slack 应用并配置 Bot Token 与 Signing Secret，目前仅支持 Slack，结构可适配其他消息平台。

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

- 通过 LangGraph 平台自定义路由挂载 Slack 事件端点
- Slack Bolt SDK 处理消息/@提及等事件并回调取回回复
- 支持 Manifest 导入与 From Scratch 两种 Slack 应用配置方式
- 可自定义输入输出的 messages 状态键映射

## 适用场景

- 让团队在 Slack 频道直接与 LangGraph 聊天机器人对话
- 将已有 LangGraph 应用接入日常工作通讯渠道
- 以此为模板适配其他消息平台的事件集成

## 场景标签

 · 领域:LLM 基础设施/消息平台集成

## 证据(README 行号)

> L15: The overall concept is simple: Slack routes are added directly to the API server deployed on the LangGraph platform
> L65: The integration uses the langgraph_sdk and connects to the current platform routes by setting URL to None, which co

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langgraph-messaging-integrations 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-24 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d0b090afbab9` · [字段定义](../../DATASET.md)*
