# Ramakm/AI-Chatbot

⭐ 26 · Python · MIT · 推送 2025-12-23 · [GitHub](https://github.com/Ramakm/AI-Chatbot) · 个人维护

**基于 FastAPI 的意图识别聊天机器人 Web 应用**

面向终端用户的对话式聊天机器人：预训练神经网络（chatbot_model.h5，TensorFlow/Keras/NLTK）识别用户消息意图，返回预设回答并提供置信度与姓名个性化。后端为 FastAPI 异步 API（/api/chat、/health），前端为响应式 HTML/CSS/Bootstrap 页面。支持 Docker 构建运行及 Heroku/Render/Railway/AWS 部署；回答内容来自 intents.json，可通过 train.py 用自定义意图重训模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预训练神经网络意图识别，返回置信度评分
- FastAPI 异步后端，含 /health 健康检查端点
- 提供 Docker 镜像构建与 Heroku/Render/Railway/AWS 部署途径
- 修改 intents.json 并运行 train.py 可重训模型

## 适用场景

- 部署一个可自定义意图与回答的网站客服聊天机器人
- 学习 FastAPI 与 Keras 意图识别模型的集成示例
- 通过 Docker 或云平台快速部署对话服务

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A beautifully designed, production-ready AI chatbot powered by **FastAPI**, featuring a modern responsive UI with re
> L141: The chatbot uses a pre-trained neural network that:
> L144: - Returns contextually appropriate responses

## 星数曲线

```mermaid
xychart-beta
    title "Ramakm/AI-Chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c85abc436e72` · [字段定义](../../DATASET.md)*
