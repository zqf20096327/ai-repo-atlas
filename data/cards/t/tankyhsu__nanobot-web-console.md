# tankyhsu/nanobot-web-console

⭐ 13 · HTML · 推送 2026-04-05 · [GitHub](https://github.com/tankyhsu/nanobot-web-console) · 个人维护 · 中文 README

**为 nanobot AI 助手框架提供 Web 控制台与 HTTP API 服务器**

nanobot 是一个轻量级个人 AI 助手框架，本项目中为其补充 FastAPI API 服务器与单文件 Web 控制台。Web 端提供实时流式聊天（WebSocket，含 thinking/tool_call 事件）、会话历史浏览、六页签设置面板（模型、渠道、Provider API key、cron 任务、提示词编辑、工具/技能/记忆查看）；可选安装 openviking 启用知识库的文件浏览、上传与语义搜索。API 端含 OpenAI 兼容的 /v1/chat/completions 等接口。面向已安装配置 nanobot 的用户，兼容 nanobot 0.1.4+，需 Python 3.11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件 Web 控制台 + FastAPI API 服务器，WebSocket 流式聊天并自动重连
- OpenAI 兼容的 /v1/chat/completions 端点与 WS 流式协议
- 六页签设置面板：模型/渠道/Provider 密钥/cron 任务/SOUL.md 等提示词/记忆查看
- 可选 openviking 知识库：viking:// 文件浏览、上传与语义搜索

## 适用场景

- 给我的 nanobot 助手装一个网页端对话界面和 API
- 在浏览器里查看会话历史与工具调用详情
- 通过 OpenAI 兼容接口把 nanobot 接入其他应用
- 管理知识库文件并按语义检索

## 场景标签

`聊天机器人` `语义搜索` · 领域:对话与助手

## 证据(README 行号)

> L5: A web console + API server for nanobot — an ultra-lightweight personal AI assistant framework.
> L7: nanobot provides a powerful agent core (tools, skills, memory, channels) but no HTTP API or web UI. This project add

## 星数曲线

```mermaid
xychart-beta
    title "tankyhsu/nanobot-web-console 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2b55979599a0` · [字段定义](../../DATASET.md)*
