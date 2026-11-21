# sagar-develop/litertlm-kmp

⭐ 11 · Kotlin · AGPL-3.0 · 推送 2026-06-23 · [GitHub](https://github.com/sagar-develop/litertlm-kmp) · 个人维护

**给 Android 开发者的 Gemma 端侧运行引擎库及本地聊天示例应用**

围绕 Google LiteRT-LM 的 Kotlin Multiplatform 封装库，支持在设备端运行 Gemma 系列模型，提供 KV-cache 有状态多轮会话、带断点续传与 SHA-256 校验的模型下载管理、函数调用 schema 转换、设备端文本嵌入（RAG）与图像输入。面向需要在自有 App 中集成端侧 LLM 的 Android 开发者。附带示例应用 NativeLM，为基于本地文档问答与聊天的私有应用。双许可：AGPL-3.0，商业发行需商业许可。iOS 支持处于路线图阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- KV-cache 有状态会话，多轮记忆无重发历史
- 硬件分级逻辑按设备选择 Gemma 变体并拦截低配设备
- 类型化 Kotlin schema 转 OpenAPI JSON 的函数调用约束输出
- 设备端嵌入引擎支持本地 RAG 管线（PDF 提取→嵌入→HNSW 检索→带引用回答）

## 适用场景

- 在自有 Android App 中离线运行 Gemma 流式对话
- 基于用户本地 PDF/笔记构建端侧文档问答（RAG）
- 在 LLM 输出上做结构化函数调用
- 按设备硬件自动匹配可运行的模型变体

## 场景标签

`文档问答` `RAG` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L10: **A Kotlin Multiplatform wrapper around Google's LiteRT-LM for running Gemma-family models on-device.**
> L18: - A clean abstraction over the LiteRT-LM Java SDK so your app code stays platform-independent
> L69: The common module (`lib/src/commonMain`) carries the engine state machine, model-catalog typing, Ktor-backed downlo

## 星数曲线

```mermaid
xychart-beta
    title "sagar-develop/litertlm-kmp 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-21"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-08 10 → 2026-11-21 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `ee6c9cc68c97` · [字段定义](../../DATASET.md)*
