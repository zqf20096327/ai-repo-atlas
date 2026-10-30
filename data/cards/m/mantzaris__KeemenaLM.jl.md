# mantzaris/KeemenaLM.jl

⭐ 16 · Julia · MIT · 推送 2026-10-29 · [GitHub](https://github.com/mantzaris/KeemenaLM.jl) · [官网](https://mantzaris.github.io/KeemenaLM.jl/) · 个人维护

**Julia 语言从零构建/训练/运行 GPT 式解码器模型的研究包**

Julia 语言的 GPT 风格解码器语言模型研究工具：覆盖语料准备、tokenizer 训练、基于 Flux/Lux 的模型构建与训练、JLD2 权重 bundle 导出、行为评测与单轮对话 REPL。当前基线为从零训练的 336M 参数聊天模型，经 1.5B 字符预训练与 39,584 条 SFT，但自述未通过常识/算术/事实性检查，不适用于真实用户。支持 CUDA 训练，CPU 自动回退，Metal 为可选实验路径。权重不进 git，经 Julia artifact 从 GitHub Release 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Flux 实例化/前向/生成/训练，CUDA 支持（auto 回退 CPU）
- JLD2 可移植模型 bundle 与可恢复 checkpoint
- 行为门评测（behavior gate）与单轮聊天 REPL
- tokenizer bundle sidecar 与 release artifact 打包脚本

## 适用场景

- 在 Julia 中从零训练小型 GPT 式解码器模型
- 加载 336M 基线 bundle 运行对话 REPL 或 prompt probe
- 复现语料构建、训练、评测的完整研究流水线

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L6: KeemenaLM.jl is a Julia proof-of-concept for building, training, exporting, and
> L53: - Flux model instantiate, forward pass, generation, and training
> L61: - one-turn chatbot REPL from a saved bundle

## 星数曲线

```mermaid
xychart-beta
    title "mantzaris/KeemenaLM.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ce9885a4031b` · [字段定义](../../DATASET.md)*
