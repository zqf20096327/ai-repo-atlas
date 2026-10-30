# pooyaphoenix/CortexKG

⭐ 20 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/pooyaphoenix/CortexKG) · 个人维护 · 中文 README

**把对话转为知识图谱的 LLM 长期记忆工具，用户自主掌控**

基于 Streamlit 的对话应用：在与 LLM 交流过程中抽取实体与关系，存入带时间戳的知识图谱，供后续对话注入上下文，形成持久、可移植的 AI 记忆。提供 3D/2D 图谱浏览、时间回溯、记忆控制中心（搜索、编辑、确认、删除）、JSON 导入导出，可选同步 Neo4j。支持 Ollama、OpenAI、Gemini 及 OpenAI 兼容端点，含 OpenRouter、vLLM、LM Studio 等；可 Docker 或源码运行，本地存储优先。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话中抽取实体与关系存入带时间戳的知识图谱
- 3D 图谱浏览、时间回溯 scrubber 与按日学习时间线
- 记忆控制中心：搜索、编辑、确认、拒绝、删除记忆
- JSON 导入导出与可选 Neo4j 同步

## 适用场景

- 让 LLM 跨对话记住我的知识与个人背景
- 可视化浏览和审计 AI 记住了什么、何时学的
- 把个人 AI 记忆在不同模型和提供商间迁移携带

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L33: Instead of repeatedly telling the model who you are, what you know, what you've learned, and how everything is conn
> L46: 5. Future conversations can inject this graph back into the LLM as context.
> L71: - 💬 **Multi-Provider LLM Support** — Ollama, OpenAI, Gemini, and OpenAI-compatible APIs.

## 星数曲线

```mermaid
xychart-beta
    title "pooyaphoenix/CortexKG 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-30 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `2b63e5a6cb9c` · [字段定义](../../DATASET.md)*
