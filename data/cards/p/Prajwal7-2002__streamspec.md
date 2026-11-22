# Prajwal7-2002/streamspec

⭐ 6 · Jupyter Notebook · AGPL-3.0 · 推送 2026-11-14 · [GitHub](https://github.com/Prajwal7-2002/streamspec) · 个人维护

**在消费级硬件上运行 70B/DeepSeek-R1 的推测解码层流式推理库**

StreamSpec 以 Python/PyTorch 库形式实现推测式解码与分层权重流式加载的组合：内存中的小型草稿模型生成候选 token 块，目标大模型层经 VRAM 单次流过进行批量验证，配合 MLA KV 压缩、4-bit 块量化流式传输、MoE 活跃专家过滤与异步预取。面向需要在 8–16 GB 显存的消费级设备上运行 70B 及 DeepSeek-R1 级模型的开发者与研究者。输出遵循目标模型的精确分布（Leviathan 等价性）。支持 PyPI 安装与 Google Colab/Kaggle 免本地存储运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 草稿模型 + 单遍层流的推测解码架构，含精确分布不变性证明
- DeepSeek MLA KV 压缩（README 声称 85.9%–93.0% 缩减）
- 4-bit 块量化流式与 MoE 活跃专家联合过滤
- 提供 PyPI 安装、本地模拟器、真实权重基准与 Colab/Kaggle 笔记本

## 适用场景

- 在消费级笔记本上运行 70B 或 DeepSeek-R1 级模型
- 评估推测解码在层卸载场景下的 I/O 收益
- 复现基准遥测与数学等价性测试套件

## 场景标签

`模型量化` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L23: `StreamSpec` decouples execution into an in-memory small speculator and single-pass layer streaming:
> L55: `StreamSpec` natively supports **DeepSeek-V3 / DeepSeek-R1 Multi-Head Latent Attention (MLA)**.
> L136: ### 1. Instant Installation from PyPI

## 星数曲线

```mermaid
xychart-beta
    title "Prajwal7-2002/streamspec 星数(近 3 点)"
    x-axis ["2026-11-11", "2026-11-12", "2026-11-22"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-11-11 5 → 2026-11-22 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `db9669a714b3` · [字段定义](../../DATASET.md)*
