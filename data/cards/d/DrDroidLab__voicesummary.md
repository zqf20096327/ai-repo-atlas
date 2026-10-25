# DrDroidLab/voicesummary

⭐ 36 · Python · MIT · 推送 2025-11-03 · [GitHub](https://github.com/DrDroidLab/voicesummary) · 组织维护

**语音 Agent 通话转录的开源 AI 数据库与分析平台**

面向呼叫中心、语音机器人开发者与 AI 研究者的转录存储与分析平台：基于 FastAPI、React/Next.js 与 PostgreSQL，支持通过 REST API 或 Bolna 集成接入通话数据，AWS S3 存储音频。提供 AI 数据抽取管道（客户信息、通话原因、分类、情感、标注）、音频分析（停顿检测、对话健康评分）与多 Agent 场景对比测试。AI 分析依赖 OpenAI API key，无 key 时仅保留音频分析与基础处理。通过 setup.sh 一键部署。

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

- AI 数据抽取管道：客户信息提取、通话分类、情感分析与业务标注（可经 agent_prompts.yaml 自定义提示词）
- 音频分析：停顿检测、语音分段、对话健康评分（无需 OpenAI key）
- 双通道数据接入：REST API 直连与 Bolna 平台集成，S3 音频存储
- 多 Agent 场景对比测试与执行 API

## 适用场景

- 为语音 Agent 通话建立数据库并生成抽取、分类与情感分析结果
- 评估语音 Agent 的通话质量与脚本遵循情况
- 对比多个语音 Agent 在同一场景下的表现
- 对通话音频做停顿与对话健康度分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Open Source AI Database for Voice Agent Transcripts**
> L20: Voice Summary is an **open-source AI database** specifically designed for **voice agent transcripts** and **call an

## 星数曲线

```mermaid
xychart-beta
    title "DrDroidLab/voicesummary 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `67a29c4a1122` · [字段定义](../../DATASET.md)*
