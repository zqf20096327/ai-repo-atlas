# hiremav/spectre

⭐ 28 · Ruby · 推送 2025-12-15 · [GitHub](https://github.com/hiremav/spectre) · 组织维护

**Rails 应用的 AI 集成 gem：嵌入、向量搜索与对话补全**

面向 Ruby on Rails 开发者的 Ruby gem，通过 include 模块方式为 Mongoid 模型生成嵌入并存储，基于 MongoDB Atlas 执行向量搜索，提供统一接口调用多家 LLM 提供商（OpenAI、Ollama、Claude、Gemini）生成对话补全，支持 JSON Schema 结构化输出、函数调用与生成参数透传。另提供基于 .yml.erb 模板与 ERB 的动态 prompt 渲染系统。向量搜索当前仅支持 Mongoid 模型，Claude 嵌入未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mongoid 模型嵌入生成（embed!/embed_all!）与 MongoDB Atlas 向量搜索
- 统一接口对接 OpenAI、Ollama、Claude、Gemini 的对话补全
- JSON Schema 结构化输出与函数调用（tool use）
- .yml.erb + ERB 的动态 prompt 模板渲染

## 适用场景

- 在 Rails 应用中为模型生成嵌入并做向量检索
- 构建 RAG 问答或聊天机器人功能
- 跨多个 LLM 提供商切换对话补全后端
- 用模板管理可复用的动态提示词

## 场景标签

`RAG` `模型网关` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Spectre** is a Ruby gem that makes it easy to AI-enable your Ruby on Rails application. Currently, Spectre focuses
> L13: |Vector Searching|MongoDB Atlas|

## 星数曲线

```mermaid
xychart-beta
    title "hiremav/spectre 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6acd6a92e8bc` · [字段定义](../../DATASET.md)*
