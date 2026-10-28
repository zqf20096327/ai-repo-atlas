# Tanzania-AI-Community/twiga

⭐ 54 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Tanzania-AI-Community/twiga) · [官网](https://ai.or.tz/) · 组织维护

**面向坦桑尼亚教师的 WhatsApp 教育 AI 聊天机器人**

由 Tanzania AI Community 构建的 WhatsApp 聊天机器人，面向坦桑尼亚教师，通过 RAG 将 LLM 能力与坦桑尼亚教育研究院（TIE）的课程与教材知识结合，用于自然语言对话、生成试题、撰写教案、检索教材信息等教育应用。曾获 Meta Llama Impact Grant Innovation Award 2024。后端含 FastAPI 服务，暴露 /metrics 指标端点，可通过 docker compose 启动 Prometheus + Grafana 监控栈。README 未给出完整安装运行步骤，细节位于 docs/ 目录。

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

- RAG 结合 TIE 课程与教材知识回答教师提问
- 应用场景含试题生成、教案撰写、教材信息检索
- FastAPI 服务暴露 Prometheus 指标端点（LLM 调用、限流等计数器）
- Grafana 自动预置 FastAPI/LLM/Redis 三个监控面板

## 适用场景

- 教师通过 WhatsApp 提问并获取基于教材的回答
- 生成试题与撰写教案
- 检索坦桑尼亚教材中的信息

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L11: Twiga is a WhatsApp chatbot designed specifically for Tanzanian teachers, and is being built by the Tanzania AI Com
> L13: This project was awarded the Meta Llama Impact Grant Innovation Award 2024 for its use of Llama open source LLMs fo

## 星数曲线

```mermaid
xychart-beta
    title "Tanzania-AI-Community/twiga 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-28 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `73717f11bbf5` · [字段定义](../../DATASET.md)*
