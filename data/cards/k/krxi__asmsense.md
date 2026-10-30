# krxi/asmsense

⭐ 17 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/krxi/asmsense) · [官网](https://huggingface.co/datasets/krxi123/asmsense) · 个人维护

**为剥离符号的 x86-64 二进制函数自动命名与描述的小模型研究**

面向逆向工程场景的研究项目：输入剥离符号二进制中某函数的汇编（可含调用上下文与匿名化 Ghidra 伪代码），输出建议的函数名与简短描述。自建数据集（v4 含 341 项目、228,177 个函数、5 个优化级别，发布于 Hugging Face/Kaggle），以 Qwen3-8B + LoRA（Apache-2.0）为贡献模型，并与多个大模型在同一测试集对比。README 报告 v6 部分指标未达既定目标（name F1 0.135，两个 F1 目标 0.14/0.17 均未命中），且输出仍需人工复核；还报告了记忆化与供应商代码重叠等数据审计发现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输入函数汇编（含调用上下文与匿名化 Ghidra 伪代码），输出函数名与英/土语描述
- v4 数据集 228,177 函数 / 341 项目 / 5 个优化级别，发布于 Hugging Face（krxi123/asmsense）
- Qwen3-8B + LoRA v6 适配器以 Apache-2.0 公开，附全精度证据
- 对多个大型开源模型做同测试集对比，并报告记忆化与 vendored 代码重叠审计

## 适用场景

- 逆向剥离符号二进制时获取函数名与描述的候选建议（需人工复核）
- 研究小模型在函数命名任务上相对大模型的表现与数据污染问题
- 复用汇编-函数名数据集做逆向工程相关模型训练

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: **A small language model that looks at a function in a stripped binary and gives it a meaningful name and a short de
> L36: 1. **Data generation (`cikar.py`):** Open-source C projects are compiled for x86-64 at different optimization level
> L139: Qwen2.5-Coder-0.5B (4-bit), 1,500 steps (~1 hour 40 minutes, 4,8 GB memory). Neither attempt **worked**:

## 星数曲线

```mermaid
xychart-beta
    title "krxi/asmsense 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `63bf9abdb474` · [字段定义](../../DATASET.md)*
