# guinmoon/llmfarm_core.swift

⭐ 283 · C++ · MIT · 推送 2025-12-09 · [GitHub](https://github.com/guinmoon/llmfarm_core.swift) · 个人维护

**在 macOS/iOS 上加载运行本地 LLM 的 Swift 库**

基于 ggml 与 llama.cpp 的 Swift 库，用于在 macOS (13+) 与 iOS (16+) 上以指定参数加载并运行不同的大语言模型，支持 Metal 加速（不适用于 Intel Mac）。提供多种推理后端与采样方法（Temperature/TFS/Mirostat/Greedy/Grammar 等）及模型设置模板；LoRA 相关能力仍在待办中。作者自述代码处于持续修订状态。通过 Swift Package Manager 集成，另有基于该库的 LLM Farm 应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 macOS 13+ 与 iOS 16+ 本地加载运行 LLM
- 多种采样方法（Temperature/TFS/Mirostat/Greedy/Grammar 等）
- Metal 加速支持（不适用于 Intel Mac）
- 基于 ggml 与 llama.cpp

## 适用场景

- 在 Swift 项目中集成本地 LLM 推理能力
- 开发 iOS/macOS 上的本地大模型应用
- 通过不同采样参数控制生成行为

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: LLMFarm_core swift library to work with large language models (LLM). It allows you to load different LLMs with certa
> L6: Based on ggml and llama.cpp by Georgi Gerganov.

## 星数曲线

```mermaid
xychart-beta
    title "guinmoon/llmfarm_core.swift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 282 --> 284
    line [283, 283]
```

2026-10-18 283 → 2026-10-27 283（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3e84699b967e` · [字段定义](../../DATASET.md)*
