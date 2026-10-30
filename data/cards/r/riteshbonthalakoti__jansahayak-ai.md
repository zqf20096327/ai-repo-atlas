# riteshbonthalakoti/jansahayak-ai

⭐ 25 · JavaScript · MIT · 推送 2026-06-13 · [GitHub](https://github.com/riteshbonthalakoti/jansahayak-ai) · [官网](https://janshayak-ai.vercel.app) · 组织维护

**帮印度公民用语音/聊天发现并申请政府福利的多语言 AI 助手**

面向印度公民（尤其农村地区）的政府福利导航助手：通过 WhatsApp（Meta Cloud API）或 React Web PWA，以 12 种印度语言（Bhashini STT/TTS）进行语音和文字对话，帮助用户发现、核验并申请福利计划。核心机制为 LangGraph 编排的 OBSERVE→REASON→ACT→VERIFY 自主 agent 循环，支持多 LLM 故障转移链、资格自动核验、ChromaDB 向量检索知识库。后端 Python 3.11 + FastAPI，前端部署于 Vercel，后端部署于 Hugging Face Spaces。为黑客松项目，团队两人。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Bhashini 支持的 12 种印度语言语音（STT/TTS）
- LangGraph 编排的 OBSERVE→REASON→ACT→VERIFY 自主 agent 循环
- WhatsApp Cloud API 集成，无需下载应用
- 多 LLM 提供商故障转移链，避免单一供应商锁定

## 适用场景

- 用母语通过 WhatsApp 查询可申请的政府福利计划
- 自动核验年龄、收入、职业等资格条件
- 获取福利申请所需的文件清单与通俗化说明

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: > **JanSahayak AI — India's autonomous welfare navigator. Multilingual AI that helps every citizen discover, verify,
> L30: - **🤖 Agentic Loop** — OBSERVE → REASON → ACT → VERIFY cycle via LangGraph orchestration
> L41: |**Voice (STT/TTS)**|Bhashini API — 12 Indian languages|

## 星数曲线

```mermaid
xychart-beta
    title "riteshbonthalakoti/jansahayak-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e49e01669cd2` · [字段定义](../../DATASET.md)*
