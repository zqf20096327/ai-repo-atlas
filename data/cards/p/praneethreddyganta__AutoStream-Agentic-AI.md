# praneethreddyganta/AutoStream-Agentic-AI

⭐ 13 · Python · 推送 2026-10-19 · [GitHub](https://github.com/praneethreddyganta/AutoStream-Agentic-AI) · [官网](https://autostream-agentic-ai.streamlit.app/) · 个人维护

**面向 SaaS 销售线索收集的对话式 Agent 应用（LangGraph+RAG）**

为虚构 SaaS 公司 AutoStream 构建的对话式销售与客服 Agent：用 LangGraph 状态机编排多轮槽位填充式线索收集（姓名/邮箱/平台），经 FAISS 本地向量库 + RAG 回答定价与政策问题，槽位填满后调用 mock CRM 写入线索。LLM 采用三层回退：Gemini 3.5 Flash-Lite 主模型、Groq GPT-OSS 20B 备用、双限流时返回礼貌提示。提供 CLI 与 Streamlit 两种界面，可部署到 Streamlit Community Cloud，需自备 Gemini 与 Groq API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 状态机驱动的多轮槽位填充线索收集流程
- FAISS + Gemini Embedding 2 的本地 RAG 语义检索
- Gemini 主模型 + Groq GPT-OSS 20B 回退的多 LLM 三层架构
- 提供 Streamlit 仪表盘界面与云端部署指引

## 适用场景

- 搭建自动收集销售线索的对话机器人
- 演示基于 LangGraph 的 Agentic 对话工作流
- 参考多 LLM 回退与限流降级实现模式

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L9: The agent utilizes **LangGraph** state machines to orchestrate multi-turn slot-filling lead capture workflows, retri
> L20: Once the agent detects high user intent (e.g., a desire to upgrade or purchase a subscription), it transitions into
> L41: - **Gemini 3.5 Flash-Lite Integration**: Powered by Google Gemini 3.5 Flash-Lite for ultra-fast, cost-effective int

## 星数曲线

```mermaid
xychart-beta
    title "praneethreddyganta/AutoStream-Agentic-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0a885a2e3970` · [字段定义](../../DATASET.md)*
