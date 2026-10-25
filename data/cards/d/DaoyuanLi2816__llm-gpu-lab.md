# DaoyuanLi2816/llm-gpu-lab

⭐ 36 · Python · Apache-2.0 · 推送 2026-07-11 · [GitHub](https://github.com/DaoyuanLi2816/llm-gpu-lab) · [官网](https://pypi.org/project/llm-gpu-lab/) · 个人维护

**单卡 NVIDIA GPU 上完整本地 LLM 工作流工具包（预训练到部署）**

面向拥有单张消费级 NVIDIA GPU（12–24 GB）的开发者：提供从环境诊断、tokenizer 训练、TinyGPT 从零预训练、LoRA/QLoRA 微调小模型、轻量评测、GGUF 导出与 llama.cpp 部署，到 GPU 基准测试与可复现 HTML 报告的端到端流程。两条路径共享 JSON artifact 与报告基础设施，所有数字由实际运行产生。以 PyPI 包与 git clone 两种方式安装，附 CLI 与 Makefile 驱动的配置化流水线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从零预训练 + LoRA/QLoRA SFT 两条并行路径
- GGUF 导出与 llama.cpp serving 部署分支
- 每步输出 JSON artifact，生成自包含 HTML 基准报告
- CLI 覆盖 doctor/train-tokenizer/pretrain 等步骤，附 lm-evaluation-harness 可选集成

## 适用场景

- 在单张 RTX 显卡上学习完整本地 LLM 训练与部署流程
- 复现或生成自己 GPU 上的真实基准报告
- 作为模板扩展自己的微调与评测流水线

## 场景标签

`微调` `模型训练` `模型评测` `推理引擎` · 领域:评测与运维

## 证据(README 行号)

> L12: `llm-gpu-lab` is a hands-on, end-to-end LLM toolkit you can run on a single
> L33: 5. LoRA / QLoRA supervised fine-tuning of a small open model
> L36: 8. GGUF export and llama.cpp serving

## 星数曲线

```mermaid
xychart-beta
    title "DaoyuanLi2816/llm-gpu-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4aa75dc545c7` · [字段定义](../../DATASET.md)*
