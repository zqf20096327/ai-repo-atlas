# Nano-Collective/nanotune

⭐ 39 · TypeScript · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/Nano-Collective/nanotune) · [官网](https://nanocollective.org) · 组织维护

**面向开发者的 Apple Silicon 小模型交互式微调 CLI**

Nano Collective 开发的命令行工具，用于在 Apple Silicon 上微调小型语言模型。以交互式 TUI 引导用户完成初始化、数据添加与训练流程，不依赖 YAML 配置与复杂命令行参数，内部自动处理 MLX 与 llama.cpp 工具链。通过 npm 全局安装或 npx 直接运行，文档涵盖命令参考、训练数据、基准测试与 LLM judge 配置。面向希望在 Mac 上进行模型微调的开发者，仅限 Apple Silicon 硬件环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 交互式 TUI 引导微调流程，无需 YAML 配置
- 自动处理 MLX 与 llama.cpp 工具链
- npm 全局安装或 npx 直接运行
- 支持 LoRA 微调小型语言模型

## 适用场景

- 在 Apple Silicon Mac 上微调小型语言模型
- 通过交互式命令行管理训练数据并启动训练
- 使用内置 LLM judge 与基准测试评估调优效果

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: A simple, interactive CLI for fine-tuning small language models on Apple Silicon — built by the Nano Collective, a c
> L5: No YAML configs, no complex flags — just an interactive TUI that guides you through each step. Nanotune handles the 

## 星数曲线

```mermaid
xychart-beta
    title "Nano-Collective/nanotune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cf7e98744ada` · [字段定义](../../DATASET.md)*
