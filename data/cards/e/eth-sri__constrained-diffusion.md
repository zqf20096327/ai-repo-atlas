# eth-sri/constrained-diffusion

⭐ 58 · Rust · MIT · 推送 2026-10-20 · [GitHub](https://github.com/eth-sri/constrained-diffusion) · [官网](https://constrained-diffusion.ai) · 组织维护

**用上下文无关语法对扩散 LLM 与填空模型做受限解码的库**

ETH Zurich SRI Lab 的研究代码，实现基于上下文无关文法（CFG）的受限解码方法，面向扩散 LLM（LLaDA、Dream-Coder、DiffuCoder）与 Fill-in-the-Middle、多区域填空模型（StarCoder、DeepSeek Coder、CodeGemma），保证输出相对文法的语法正确性，并在论文中报告功能正确性提升。约束语言示例含 JSON Schema、C++、SMILES。安装需 Python 3.11+、Rust 工具链（maturin 构建绑定）与 CUDA GPU，并提供评测数据集与复现脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CFG 受限解码保证语法正确性
- 支持扩散 LLM 与 FIM/MRI 两类模型的非自回归生成
- 约束语言示例覆盖 JSON Schema、C++、SMILES
- 提供评测执行 harness 与论文实验复现脚本

## 适用场景

- 让扩散 LLM 代码生成输出严格符合 C++ 或 JSON Schema 文法
- 在多区域填空任务中施加语法约束做评测
- 复现论文实验结果或扩展新约束语言/新模型

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L11: This repository contains the implementation of Constrained Decoding of Diffusion LLMs with Context-Free Grammars, i
> L17: - **Works with SOTA diffusion LLMs** like LLaDA, Dream-Coder and DiffuCoder for non-autoregressive generation
> L18: - **Also works for Fill-in-the-Middle (FIM) and Multi-Region Infilling (MRI) models** like StarCoder, DeepSeek Code

## 星数曲线

```mermaid
xychart-beta
    title "eth-sri/constrained-diffusion 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 56 --> 59
    line [57, 58, 58]
```

2026-10-18 57 → 2026-10-27 58（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2f32bdeedbce` · [字段定义](../../DATASET.md)*
