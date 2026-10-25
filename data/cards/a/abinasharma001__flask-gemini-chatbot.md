# abinasharma001/flask-gemini-chatbot

⭐ 36 · HTML · 推送 2026-01-17 · [GitHub](https://github.com/abinasharma001/flask-gemini-chatbot) · [官网](https://mr-a-your-ai-chatbot.onrender.com) · 个人维护

**基于 Flask 与 Gemini API 的网页聊天机器人**

用 Flask 构建的 Web 聊天应用：前端以 HTML/CSS/JavaScript 实现聊天界面，后端通过 google.generativeai 调用 Google Gemini API 生成回复，提供 GET /、POST /chat、POST /clear 三个端点。API key 通过 .env 环境变量管理，支持会话上下文保持与模型参数（temperature、top_p 等）配置。面向学习 AI API 集成或构建自定义聊天机器人的开发者，克隆源码、pip 安装依赖并配置 API key 后运行 app.py 启动，本机 5000 端口访问。限制：依赖外部 Gemini API（有速率限制 60 请求/分钟），需自备 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Flask 后端封装 Gemini API，提供 /chat、/clear 等端点
- 环境变量管理 API key，会话保持对话上下文
- 模型参数（temperature/top_p/top_k/max_output_tokens）可在 app.py 中配置

## 适用场景

- 学习如何将 Gemini API 集成到 Flask 应用
- 快速搭建一个可自定义界面的网页聊天机器人
- 作为个人作品集展示 AI 应用开发

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L37: - **AI Model**: Google Gemini API
> L142: - **Description**: Sends a message to the Gemini API and returns the response

## 星数曲线

```mermaid
xychart-beta
    title "abinasharma001/flask-gemini-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `64322890fc8e` · [字段定义](../../DATASET.md)*
