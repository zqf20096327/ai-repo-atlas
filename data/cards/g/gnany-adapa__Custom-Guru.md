# gnany-adapa/Custom-Guru

⭐ 4 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/gnany-adapa/Custom-Guru) · 个人维护

**可溯源的 AI persona 问答引擎：回答绑定已验证引文或标注为推理**

面向想要『与某人语料对话』且需审计回答来源的用户：将用户自有语料离线蒸馏为可检查的原则集（principles.json），问答时逐条验证引文确实存在于源文本，伪造或转述引文被丢弃；语料未覆盖的问题以 premise→principle→conclusion 轨迹输出并明确标注为外推假设。附带 faithfulness critic、评测框架、可选 Langfuse 追踪与 Streamlit 演示界面。通过 LLMProvider 接口切换供应商，仓库不附带任何 persona 数据，需自备语料才能返回答案。

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

- 引文逐条验证确实存在于源文本，未通过验证的引用被丢弃
- 离线管线将语料蒸馏为可检查的原则集，支撑可追踪的推理路径
- faithfulness critic 检查推理回答并标记无支撑声明
- LLMProvider 单接口切换 OpenAI/Anthropic/本地模型/代理

## 适用场景

- 基于某人讲稿或文集构建可溯源的问答机器人
- 需要区分『原话引用』与『模型推理』的审计场景
- 自托管、可更换 LLM 供应商的 persona 问答部署

## 场景标签

`聊天机器人` `RAG` `模型评测` · 领域:对话与助手

## 证据(README 行号)

> L3: **An open-source engine for *grounded, auditable* AI personas — it answers *as* a person
> L24: - **Provider-agnostic & self-hostable.** One `LLMProvider` interface; swap OpenAI / Anthropic


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `2358409c9139` · [字段定义](../../DATASET.md)*
