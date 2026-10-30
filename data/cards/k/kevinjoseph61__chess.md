# kevinjoseph61/chess

⭐ 23 · Python · 推送 2026-05-30 · [GitHub](https://github.com/kevinjoseph61/chess) · [官网](https://chess-gang.onrender.com/) · 个人维护

**实时多人国际象棋平台，含浏览器内 AI 引擎与 LLM 教练**

基于 Django 5.2 + Daphne (ASGI) + Channels + Redis 的实时国际象棋 Web 平台：WebSocket 同步多人对局、公开/私人房间、自动重连。AI 部分：AlphaZero 风格引擎（神经网络 + MCTS，ONNX Runtime Web 在浏览器 Web Worker 内运行，三档难度）、每步评估（Brilliant 到 Blunder 分类 + Stockfish.js 深度 12 局面评估 + 评估条）、调用 Groq 的 Llama 3.3 70B 输出自然语言教练提示。单人模式无需 Redis；多人模式需 Redis 与 Groq API key。附 PyTorch 训练管线文档与 Render 部署分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AlphaZero 风格引擎在浏览器 Web Worker 内运行（ONNX INT8 量化 10.9 MB）
- 每步分类评估（★到??）+ Stockfish.js 深度 12 局面评估
- LLM 教练经 Groq API（Llama 3.3 70B）逐步输出自然语言提示
- WebSocket 实时多人对局（Django Channels + Redis）

## 适用场景

- 与浏览器内 AI 引擎下棋并按三档难度对弈
- 对局中逐步获得教练提示与局面评估
- 创建公开或私人房间进行实时多人对局

## 场景标签

 · 领域:游戏/Web 应用

## 证据(README 行号)

> L15: - **AlphaZero-style engine** — Neural network + MCTS running entirely in-browser via ONNX Runtime Web
> L22: - **Live LLM coaching** — Natural language tips after each move using Llama 3.3 70B (Groq free tier)

## 星数曲线

```mermaid
xychart-beta
    title "kevinjoseph61/chess 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `23c6cd394a44` · [字段定义](../../DATASET.md)*
