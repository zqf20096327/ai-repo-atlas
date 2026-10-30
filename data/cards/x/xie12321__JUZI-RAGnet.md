# xie12321/JUZI-RAGnet

⭐ 19 · Python · Apache-2.0 · 推送 2026-05-23 · [GitHub](https://github.com/xie12321/JUZI-RAGnet) · 个人维护 · 中文 README

**LLM 认知增强层：自省循环+分层知识库提升小模型表现**

位于语言模型与应用程序之间的即插即用认知增强层，以 OpenAI 兼容 API 形式提供独立服务，供任意客户端调用。核心机制包括思考→经验检索→错误检查的自省循环、按推理库/经验库/记忆库划分的分层知识库（支持导入 Obsidian 等 md 文件）、混合检索与知识图谱拓展、Pydantic 结构化输出与规划验证。本地模型目前仅支持 ollama，也可选云端模型。提供 Windows 图形界面安装包（.exe），README 自称 demo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自省循环：思考→经验检索→错误检查→输出
- 推理库/经验库/记忆库三层知识库，支持导入已有 md 文件
- OpenAI 兼容 API 供 OpenClaw 等客户端调用（README 标注还未测试）
- 本地模型接入目前仅支持 ollama，另支持云端模型

## 适用场景

- 给小参数本地模型叠加知识库与自省机制以处理复杂任务
- 通过 OpenAI 兼容 API 给 OpenClaw 等 Agent 客户端提供增强后端
- 用个人笔记（如 Obsidian）构建专属知识库影响模型输出

## 场景标签

`RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: **JUZI-RAGnet** 是一个即插即用的**认知增强层**，它位于“语言模型”与“应用程序”之间，通过工程化的**自省循环**、**分层记忆系统**和**按需检索**，显著提升语言模型在复杂任务中的表现。它可以作为独立服务
> L27: |**🌐 OpenAI 兼容 API**|无缝接入 OpenClaw、Hermes Agent 等任何支持该标准的客户端。（还未测试）|

## 星数曲线

```mermaid
xychart-beta
    title "xie12321/JUZI-RAGnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `46ab3caf0c75` · [字段定义](../../DATASET.md)*
