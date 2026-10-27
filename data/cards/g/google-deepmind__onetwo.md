# google-deepmind/onetwo

⭐ 274 · Python · Apache-2.0 · 推送 2026-06-02 · [GitHub](https://github.com/google-deepmind/onetwo) · 组织维护

**开发和部署生产级 LLM agent 的 Python 库**

OneTwo 是 Google DeepMind 开发的 Python 库，面向在构建 LLM 应用与 agent 的开发者。它提供统一 API 让代码在不同内外部模型间切换，支持以格式化字符串、Jinja 模板或函数调用构建 prompt，自动缓存结果以复现实验并节省配额，支持外部工具集成（含安全沙箱中运行模型生成的 Python 代码）与有状态 agent 的定义与组合，并自动处理异步执行、请求批处理与缓存。也提供检索增强生成（RAG）工作流支持。通过 pip 从 GitHub 安装，非官方 Google 产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 在不同模型间切换而无需修改逻辑
- 结果自动缓存以复现实验、节省配额
- 外部工具集成与安全沙箱中运行模型生成的 Python 代码
- 有状态 agent 定义与组合，自动处理异步执行与请求批处理

## 适用场景

- 构建需要工具调用与多步推理的 LLM agent
- 搭建基于自有数据的 RAG 问答工作流
- 在不同模型后端间切换运行同一套 agent 代码

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  One Two is a python library for developing and deploying LLM
> L13: * **Swap models easily (Model-agnostic)**: Write code once using a uniform API

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/onetwo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 273 --> 276
    line [275, 274, 274]
```

2026-10-18 275 → 2026-10-27 274（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9d23025f518b` · [字段定义](../../DATASET.md)*
