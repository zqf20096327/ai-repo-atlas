# Moissanite-Labs/siliquant

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/Moissanite-Labs/siliquant) · [官网](https://moissanite-labs.github.io/siliquant/) · 个人维护

**模型权重量化的研究仓库：证明、计数与实验记录**

围绕将模型权重舍入到低位宽的量化研究仓库，包含已证明的上下界、组合计数、格点码本与最近点解码器等代码目录，以及按预注册规则保存的实验记录：每项研究先提交计划再产出数据，数字可溯源到提交的输出文件，不提交模型权重与数据集。附带 harness 可读取 GGUF 文件、在 GPU 上舍入并用 llama.cpp 工具评分；另含基于 Qwen2.5-0.5B 的 CUDA/AVX-512 解码引擎研究，部分步骤标注需在 sm_86 GPU 上确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 保持已证明极限表，提案先对照该表再运行
- harness 读取 GGUF 权重并在 GPU 上舍入，用 llama.cpp 工具评分
- 实验记录遵循预注册约定：计划先行、数字可溯源、负结果同记录
- 附带 sm_86 GPU 与 AVX-512 内核基准及其构建命令

## 适用场景

- 查阅权重量化码本（E8、p-范数球等）的实测数据与证明
- 复现或扩展基于格点量化的舍入实验
- 用打包格式在少量字节中存储整数量化权重块

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: Research on rounding model weights to a few bits each (quantisation), and on the mathematics around it. It sits besi
> L5: The repository follows one rule from weft-loom: a path is closed only on a proof. So it keeps a table of proved limi
> L18: |`experiments/`|One folder per study, each with its plan, program, output and limits. Index in experiments/README.m


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `548c1fb26b70` · [字段定义](../../DATASET.md)*
