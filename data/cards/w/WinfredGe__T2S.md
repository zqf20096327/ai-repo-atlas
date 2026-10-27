# WinfredGe/T2S

⭐ 95 · Python · Apache-2.0 · 推送 2026-05-01 · [GitHub](https://github.com/WinfredGe/T2S) · [官网](https://arxiv.org/abs/2505.02417) · 组织维护

**从文本生成高分辨率时间序列的扩散模型官方实现（IJCAI'25）**

IJCAI 2025 论文 T2S 的官方实现：以自然语言描述为条件，通过扩散 transformer（T2S-DiT）与长度自适应 VAE（LA-VAE）生成高分辨率、语义对齐的变长时间序列，面向非专家数据交互、专业人员快速原型与系统压力测试。配套发布 600K 片段级文本–时间序列对齐数据集 TSFragment-600K（Hugging Face）及预训练模型，提供训练、推理与评测脚本；代码基于 Time-Series-Library、TOTEM 等修改，需 Python 3.10 与 torch 2.3.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本到时间序列的领域无关条件生成框架（T2S-DiT + LA-VAE）
- LA-VAE 支持变长时间序列生成
- 配套 TSFragment-600K 多模态数据集（600K 文本–时间序列对，6 个领域）
- 提供预训练模型与训练/推理/评测脚本

## 适用场景

- 用自然语言描述生成合成时间序列数据
- 专业人员快速模拟系统时间动态做原型分析
- 生成极端场景时间序列做系统压力测试
- 复现论文实验或在其数据集上开展研究

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L14: **T2S** is the first domain-agnostic model that enables **text-to-time series generation**. It allows users—both no
> L29: - **T2S-DiT**: A diffusion-based transformer tailored for conditional generation from natural language.

## 星数曲线

```mermaid
xychart-beta
    title "WinfredGe/T2S 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 93 --> 96
    line [94, 95, 95]
```

2026-10-18 94 → 2026-10-27 95（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8428e6eb0188` · [字段定义](../../DATASET.md)*
