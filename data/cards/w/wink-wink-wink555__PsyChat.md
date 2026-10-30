# wink-wink-wink555/PsyChat

⭐ 35 · Python · MIT · 推送 2026-03-17 · [GitHub](https://github.com/wink-wink-wink555/PsyChat) · 个人维护 · 中文 README

**基于 Agentic RAG 的心理咨询对话助手，运用 REBT 方法**

PsyChat 是面向终端用户的心理咨询 AI 对话应用：知识库基于 PsyDTCorpus 数据集构建，按 12 个心理学主题分类并分块存入 ChromaDB。多阶段 Agent 工作流包括 RAG 判断与主题分类、ReAct 查询改写（最多 3 轮）、多查询词向量检索、回溯完整咨询对话的上下文扩展、咨询师话术分析（带主题级缓存）与四层结构化提示词生成。LLM 使用 DeepSeek Chat，Embedding 与 TTS 使用阿里云百炼服务。提供 Web 界面与 CLI 两种模式，免责声明指出回复不构成专业医疗建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct 查询优化：轻检索锚点→分析匹配度→改写或直接检索
- 上下文扩展从 chunk 回溯完整咨询对话原文
- 咨询师话术分析（共情/提问/节奏/语言）带主题级缓存
- 基于 PsyDTCorpus 的 12 主题知识库与阿里云百炼 TTS 语音播放

## 适用场景

- 通过对话获得基于 REBT 理论的心理支持与情绪疏导
- 学习 RAG 多阶段 Agent 工作流在咨询场景的实现
- 研究范例引导的话术风格迁移方法

## 场景标签

`AI 助手` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L3:  基于 Agentic RAG 的智能心理咨询伴侣
> L15: **PsyChat** 是一个基于检索增强生成（RAG）技术的心理咨询 AI 助手。其核心目标是最大程度地**蒸馏真实心理咨询师的说话方式**——不只是复用知识库中的内容，而是主动分析、学习专业咨询师在共情、提问、引导节奏上的共性

## 星数曲线

```mermaid
xychart-beta
    title "wink-wink-wink555/PsyChat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `292c66cefeb8` · [字段定义](../../DATASET.md)*
