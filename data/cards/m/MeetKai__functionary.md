# MeetKai/functionary

⭐ 1,593 · Python · MIT · 推送 2026-06-30 · [GitHub](https://github.com/MeetKai/functionary) · 组织维护

**支持工具调用的开源对话语言模型（含代码解释器）**

由 MeetKai 开发的函数调用语言模型系列：模型按需触发函数（支持并行/串行调用）、以 JSON Schema 定义工具、理解函数执行结果并生成回复，v4r 版本可在调用工具前生成推理步骤。提供 vLLM 与 SGLang 服务器脚本、TGI Docker 部署、llama.cpp 推理与 Modal 无服务器部署，API 兼容 OpenAI 客户端。模型规模从 7B（FP16 约 24GB 显存）到 70B（160GB）。注意：仓库已声明弃用、不再维护，仅为旧快照。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按需触发函数调用，支持并行/串行与多轮，工具以 JSON Schema 定义
- v4r-small-preview 支持工具调用前先生成推理步骤
- 提供 vLLM/SGLang/TGI/Modal 多种部署方式，API 兼容 OpenAI 客户端
- 支持 LoRA 适配器加载与代码解释器工具

## 适用场景

- 为应用搭建本地函数调用/工具调用模型服务
- 通过 OpenAI 兼容 API 接入现有客户端做 agent 应用
- 在 llama.cpp 上以 GGUF 量化模型本地推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L10: Functionary is a language model that can interpret and execute functions/plugins.
> L12: The model determines when to execute functions, whether in parallel or serially, and can understand their outputs. 

## 星数曲线

```mermaid
xychart-beta
    title "MeetKai/functionary 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 1592 --> 1594
    line [1593, 1593]
```

2026-10-18 1,593 → 2026-10-29 1,593（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `97f6edf9f07e` · [字段定义](../../DATASET.md)*
