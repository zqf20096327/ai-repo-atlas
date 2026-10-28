# wananing/Smart-Health-Assistant

⭐ 37 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/wananing/Smart-Health-Assistant) · 个人维护 · 中文 README

**开源大健康 AI 助手全栈参考实现：多智能体问诊+实时语音**

基于 LangGraph + FastAPI + React 的 AI 健康助手全栈参考实现，对标蚂蚁阿福等产品形态。包含 Router 调度的多专科智能体（预问诊、医保、健康问答、药管家与报告解读）、开放麦可打断的实时语音问诊（级联流式 ASR→LangGraph→流式 TTS，出声前过急症规则检查）、BM25+密集向量混合检索 RAG、可插拔技能系统与 OpenTelemetry/DeepEval 评测。支持多模型配置（ARK/OpenAI/DeepSeek/通义/智谱及 OpenAI-compatible）。限制：语音真机回声消除未验证、仅覆盖 AI 诊室、语音仅实测火山引擎；医保数据为模拟接口。

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

- 开放麦可打断的实时语音问诊，级联架构保证每句话出声前过急症规则与安全检查
- LangGraph 多智能体：Router 意图分类、swarm 式 Command 转接、interrupt() 追问恢复
- RAG 混合检索（BM25+密集向量+RRF），嵌入模型与向量库（Chroma/FAISS/Qdrant/pgvector）可切换
- 可插拔 Agent Skills 系统（6 项内置技能，零配置自发现）与 OpenTelemetry/DeepEval 链路评估

## 适用场景

- 搭建医疗健康领域的多智能体问诊对话应用
- 实现像打电话一样的开放麦可打断语音问诊
- 在医保、用药、报告解读等场景做卡片化服务分发
- 学习 LangGraph 子图、转接与语音级联架构的落地模式

## 场景标签

`AI 助手` `语音 Agent` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L7: 基于 **LangGraph + FastAPI + React** 的完整 AI 多智能体全栈参考实现。不只是一个聊天机器人，而是深度融合了**流式工具调用**、**结构化 UI 卡片**与**实时语音通话**的智能分发引擎。
> L9: - 🎙️ **新增实时语音问诊（Realtime Voice Agent）**：像打电话一样问诊——开放麦连续对话、助手说话时随时开口打断，屏幕同步显示实时字幕、症状要点和分诊卡片。流式 ASR + LangGraph + 流式 T
> L12: - 支持 **多模型配置**：聊天模型可切换 ARK、OpenAI、DeepSeek、通义千问、智谱或任意 OpenAI-compatible 服务；图片模型可独立配置

## 星数曲线

```mermaid
xychart-beta
    title "wananing/Smart-Health-Assistant 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24", "2026-10-26", "2026-10-28"]
    y-axis "stars" 32 --> 38
    line [33, 34, 35, 37, 37]
```

2026-10-18 33 → 2026-10-28 37（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6a126a104b1f` · [字段定义](../../DATASET.md)*
