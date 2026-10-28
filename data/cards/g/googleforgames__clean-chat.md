# googleforgames/clean-chat

⭐ 55 · Python · Apache-2.0 · 推送 2026-07-28 · [GitHub](https://github.com/googleforgames/clean-chat) · 组织维护

**游戏内毒性行为检测框架：训练部署语音/文本毒性模型**

Google for Games 开源的游戏毒性语音与文本检测框架，供多人在线游戏的开发与运营方使用。以游戏服务器第三方服务/sidecar 形式部署，不直接与客户端通信。由 API 后端、Cloud Functions、基于 Apache Beam 的 Scoring Engine（可更换 ML 模型加启发式规则设定业务阈值）与 ML Model Pipeline 组成，预置 BERT 与 Cohere 等基础模型供训练或微调，部署依赖 Terraform、Docker 与 Google Cloud SDK，运行在 GCP（Cloud Run、Dataflow、Vertex AI、Kubeflow）之上。

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

- 语音与文本聊天的毒性检测评分，输出给游戏审核服务
- Apache Beam Scoring Engine：可更换 ML 模型 + 启发式规则阈值
- 预置 BERT、Cohere 基础模型，支持针对游戏语料微调
- 提供 TFX/Kubeflow 与 Vertex AI 两种训练部署管道

## 适用场景

- 多人在线游戏接入语音/文本聊天毒性检测
- 针对本游戏玩家用语微调毒性识别模型
- 将毒性评分结果接入游戏审核或客服系统

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L28: Clean Chat is an open source solution to eliminate or mitigate toxic behavior in online multiplayer video games, wi
> L32: Clean Chat is not a specific model for detecting toxicity. It is a framework where users can train and deploy their
> L145: Clean Chat comes pre-packaged with a framework to train, test, and deploy toxicity detection models. Currently, th

## 星数曲线

```mermaid
xychart-beta
    title "googleforgames/clean-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `21a446a8792e` · [字段定义](../../DATASET.md)*
