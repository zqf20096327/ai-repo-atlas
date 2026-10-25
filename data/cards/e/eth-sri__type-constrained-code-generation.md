# eth-sri/type-constrained-code-generation

⭐ 105 · Python · MIT · 推送 2026-03-11 · [GitHub](https://github.com/eth-sri/type-constrained-code-generation) · [官网](https://pldi25.sigplan.org/details/pldi-2025-papers/25/Type-Constrained-Code-Generation-with-Language-Models) · 组织维护

**类型约束 LLM 代码生成：约束采样只产出类型安全的 TypeScript 程序**

PLDI 2025 论文 Type-Constrained Code Generation with Language Models 的复现包，实现一个增量解析 TypeScript 程序的补全引擎，保证中间输出可补全为类型安全程序，并用于约束 LLM 采样使其只生成类型安全代码。包含采样算法与解析器两部分，可独立使用解析器。实验需 NVIDIA GPU（80GB VRAM、CUDA 12.4+）、conda 安装，覆盖 MBPP/HumanEval 上 6 个模型（Gemma 2、Qwen 2.5、DeepSeek Coder、CodeLlama）的合成/翻译/修复任务，随附原始结果与画图脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 增量解析 TypeScript 的补全引擎，保证输出可补全为类型安全程序
- 约束 LLM 采样只生成类型安全的 TypeScript 代码
- 解析器可独立使用，不依赖 torch/flash-attention
- 提供论文全部实验的复现脚本与原始结果数据

## 适用场景

- 在 LLM 代码生成中强制类型安全约束解码
- 研究约束解码对代码生成正确性的影响
- 复现 PLDI 2025 论文的实验结果与图表

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: This is an implementation of a completion engine that parses type safe programs incrementally, guaranteeing that int
> L6: The completion enginge can be used to constrain the sampling from an LLM model to only type-safe programs.
> L78: In this section we provide an overview on how to reproduce the experiments presented in our paper.

## 星数曲线

```mermaid
xychart-beta
    title "eth-sri/type-constrained-code-generation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-25 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0c1ee700da0c` · [字段定义](../../DATASET.md)*
