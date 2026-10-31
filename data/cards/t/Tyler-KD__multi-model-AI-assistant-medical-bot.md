# Tyler-KD/multi-model-AI-assistant-medical-bot

⭐ 21 · Python · Apache-2.0 · 推送 2026-03-08 · [GitHub](https://github.com/Tyler-KD/multi-model-AI-assistant-medical-bot) · 个人维护

**面向医疗诊断与研究的多 Agent AI 医疗助手聊天系统**

基于 FastAPI 与 LangGraph 的多 Agent 医疗聊天机器人：集成 RAG（Docling 解析、Qdrant 混合检索、Cross-Encoder 重排）、医学影像分析（胸部 X 光分类、皮肤病变分割、脑肿瘤检测标注 TBD）、实时网络检索与语音交互（Eleven Labs API），并含输入输出护栏与人类专家在环验证。面向医疗专业人员与学习者，以 Docker 或 Python 环境部署，默认配置使用 Azure OpenAI（gpt-4o），换用其他 LLM 需修改代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Agent 编排：诊断、检索、推理代理间基于置信度交接
- RAG 管线：Docling 解析、LLM 语义分块、Qdrant BM25+稠密混合检索、Cross-Encoder 重排
- PyTorch 医学影像代理（X 光分类、皮肤病变分割）
- 输入/输出护栏与人类专家在环验证

## 适用场景

- 上传医学影像获取 AI 诊断参考结果
- 基于自建医学文献库做检索增强问答
- 通过语音与医疗助手交互并获取带来源链接的回答

## 场景标签

`多智能体` `聊天机器人` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L8: The **Multi-Agent Medical Assistant** is an **AI-powered chatbot** designed to assist with **medical diagnosis, rese
> L39: - 🤖 **Multi-Agent Architecture** : Specialized agents working in harmony to handle diagnosis, information retrieval
> L53: - 🏥 **Medical Imaging Analysis**

## 星数曲线

```mermaid
xychart-beta
    title "Tyler-KD/multi-model-AI-assistant-medical-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bef17bb6973e` · [字段定义](../../DATASET.md)*
