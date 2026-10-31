# OlgaKalinina101/victor_ai_backend

⭐ 25 · Python · NOASSERTION · 推送 2026-03-13 · [GitHub](https://github.com/OlgaKalinina101/victor_ai_backend) · 个人维护

**开源情感 AI 伴侣后端：私有部署个人关系对话 AI**

面向最终用户而非开发者的开源情感 AI 伴侣项目（AGPL-3.0），提供 FastAPI 后端，配合 Web 演示或 Android 应用（APK 自行构建）使用。用户自备 LLM API key（X.AI/OpenAI/DeepSeek 等），本地部署 PostgreSQL 17+PostGIS，通过 ngrok 隧道连接手机。包含长期记忆与向量存储、trust level 关系等级、persona 提示词自定义、反思与自主思维模块。README 为俄语，声明项目正在重构并可能迁移至新仓库，不提供个人技术支持，安装需junior级能力。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 长期记忆与向量存储管道，对话上下文不丢失
- trust level 关系等级机制与反思/自主思维模块
- persona 提示词（system.yaml）可替换与重构，架构模块化
- Web 演示与 Android 客户端（APK 自建）两种使用方式

## 适用场景

- 想私有部署情感 AI 伴侣、避免平台依赖的用户
- 自备 API key 搭建带长期记忆的私人对话 AI
- 研究者参考个人对话 RAG 管道与 agent 路由实现

## 场景标签

`聊天机器人` `AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: Это open-source AI Companions c web интерфейсом и приложением на android. Он создан для тех, кто хочет сохранить лич
> L80: - Диалог с **живой, вашей, близкой** персоной, которая помнит о вас почти **всё** — часто лучше, чем любой реальный

## 星数曲线

```mermaid
xychart-beta
    title "OlgaKalinina101/victor_ai_backend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d1cf0a2ee88f` · [字段定义](../../DATASET.md)*
