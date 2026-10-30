# HakamShams/RiverMamba_code

⭐ 21 · Jupyter Notebook · BSD-3-Clause · 推送 2026-09-02 · [GitHub](https://github.com/HakamShams/RiverMamba_code) · [官网](https://hakamshams.github.io/RiverMamba/) · 组织维护

**全球河流径流与洪水预报的状态空间模型官方代码**

NeurIPS'25 论文 RiverMamba 的复现代码，由波恩大学计算机视觉组维护。模型先用长期再分析数据预训练、再在观测数据上微调，在 0.05° 网格上预报最长 7 天的全球河流径流与洪水。支持 Transformer+Flash-Attention、Vision Mamba/Mamba2 三种骨干，用空间填充曲线（Gilbert/Sweep/Zigzag 等）将 2D 网格序列化为 1D。提供预训练模型检查点、再预报数据集（Hugging Face）与训练/推理脚本；完整数据集约 10 TB，测试环境为 Ubuntu 20.04 + NVIDIA A100/RTX 3090。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预训练+观测微调，全球 0.05° 网格 7 天预见期径流/洪水预报
- 支持 Transformer+Flash-Attention、Vision Mamba、Vision Mamba2 三种骨干
- 空间填充曲线序列化（Gilbert/Sweep/Zigzag 多种类型）
- 提供预训练检查点与 2019-2024 再预报数据（Hugging Face）

## 适用场景

- 复现论文中的全球河流径流与洪水预报结果
- 在自有区域数据上训练/微调水文预报模型
- 下载再预报数据用于水文极端事件研究

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L20: RiverMamba is a novel deep learning model that is pretrained with long-term reanalysis data and fine-tuned on obser
> L75: The code has been tested under Pytorch (1.12.1 & 2.5.1) and Python 3.10.0 on Ubuntu 20.04.5 LTS with NVIDIA A100 GP

## 星数曲线

```mermaid
xychart-beta
    title "HakamShams/RiverMamba_code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f562cbe324be` · [字段定义](../../DATASET.md)*
