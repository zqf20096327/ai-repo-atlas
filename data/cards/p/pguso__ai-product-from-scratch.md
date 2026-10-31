# pguso/ai-product-from-scratch

⭐ 44 · TypeScript · MIT · 推送 2026-02-07 · [GitHub](https://github.com/pguso/ai-product-from-scratch) · 个人维护

**教学项目：从零构建本地 LLM 消息分析工具，理解 AI 产品原理**

面向开发者的 10 课教学仓库，通过逐步构建一个 Communication Mirror 应用（分析消息的情感影响）讲解多步 AI 推理、提示工程、JSON Schema 语法约束、REST API 与 React 前端等。模型侧使用 node-llama-cpp 在本地加载 GGUF 格式模型（推荐 Qwen3 系列，兼容 Llama 3、Mistral），CPU 推理即可运行，4GB 内存可跑 1.7B 量化模型。明确声明不含生产化、可扩展性与部署内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 节课覆盖提示工程、语法约束输出、多步推理分解、输出验证与重试
- 基于 node-llama-cpp 本地加载 GGUF 模型，CPU-only 可运行
- 给出按内存分档的模型选择与量化级别参考表
- 前端 React + 后端 Express，npm run dev 一键运行

## 适用场景

- 系统学习不依赖框架的 AI 产品构建流程
- 在本地跑通一个含 LLM 推理与校验的完整全栈应用
- 了解 GGUF 模型量化与内存需求的对应关系

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **Goal:** Understanding, not production.
> L32: This repository includes 10 comprehensive lessons that guide you through building an AI product from scratch. Follo
> L37: |02|Understanding Local LLMs and GGUF Models|Learn about local LLMs, GGUF format, quantization, and how to load mod

## 星数曲线

```mermaid
xychart-beta
    title "pguso/ai-product-from-scratch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-31 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `681f6c6d6de0` · [字段定义](../../DATASET.md)*
