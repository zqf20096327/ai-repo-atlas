# Md-Emon-Hasan/MediGenius

⭐ 52 · Jupyter Notebook · MIT · 推送 2026-08-05 · [GitHub](https://github.com/Md-Emon-Hasan/MediGenius) · [官网](https://medigenius.onrender.com) · 个人维护

**面向普通人的多智能体医疗信息问答助手，带确定性安全层**

基于 LangGraph StateGraph + Groq LLM（经 LiteLLM 网关分层重试）构建的多智能体医疗信息助手，FastAPI 后端 + React 前端。每次请求前后运行确定性安全层：危机语言检测返回固定求助热线、儿科/孕期剂量与药物相互作用问题硬拒绝并转介药师、剔除检索来源之外的剂量数字、生成后由验证子代理核查临床声明，高风险回答进入临床医生复核队列。检索侧并行组合医学 PDF RAG（ChromaDB + HuggingFace 嵌入）、Wikipedia 与 Tavily。明确声明不提供剂量建议与诊断，需 GROQ 与 TAVILY API key，Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 调用前后的确定性安全层（危机检测、拒答主题、剂量接地、诊断验证）
- RAG/Wikipedia/Tavily 并行检索 + 直接 LLM 兜底，ExecutorAgent 综合
- RxNav (NIH) 药名识别，药物相互作用问题转介药师
- 临床医生复核队列与审计日志（仅元数据，SQLite）

## 适用场景

- 用通俗语言了解症状、药物与健康问题
- 识别危机语言并转接求助热线
- 就诊前把症状描述结构化整理给医生看

## 场景标签

`多智能体` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L20: **MediGenius** helps people understand symptoms, medications, and health questions in plain language — and just as
> L25: Under the hood, **MediGenius** is a multi-agent medical information assistant orchestrated as a **LangGraph
> L92: * **Deterministic safety layer** — crisis/emergency detection, refused-topic hard-stops, dosage grounding, and an u

## 星数曲线

```mermaid
xychart-beta
    title "Md-Emon-Hasan/MediGenius 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-28 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fccd1925aecc` · [字段定义](../../DATASET.md)*
