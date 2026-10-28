# DLS5-Omics/CellNavi

⭐ 57 · Python · GPL-3.0 · 推送 2026-07-10 · [GitHub](https://github.com/DLS5-Omics/CellNavi) · 组织维护

**预测驱动细胞状态转变基因的深度学习框架**

CellNavi 是面向单细胞转录组数据的深度学习框架，基于 2000 万单细胞预训练并结合先验因果基因图，将细胞数据投影到低维且具生物学意义的空间，以预测驱动细胞转变的基因。应用包括 CRISPR 靶点识别、主调节因子预测、疾病驱动基因发现与药物 MoA 解析。训练与推理均需 NVIDIA GPU（已在 V100/A100 测试），要求 Python 3.12+ 与 CUDA 12.1+，通过 conda 环境加源码 pip 安装，配置集中于 config.json，提供微调、评估与 perturbation logits 计算脚本及教程数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 2000 万单细胞预训练权重，结合先验因果基因图
- 跨细胞情境的通用框架：CRISPR 靶点、主调节因子、疾病驱动、MoA
- 训练与推理均需 NVIDIA GPU（V100/A100 已测试）
- 配置集中于 config.json，提供微调/评估/推理脚本与教程数据集

## 适用场景

- 我想找出驱动某类细胞状态转变的关键基因
- 为 CRISPR 实验筛选候选靶点基因
- 在自有单细胞数据上微调并评估模型预测效果

## 场景标签

 · 领域:生物信息学/单细胞分析

## 证据(README 行号)

> L3: CellNavi is a deep learning framework designed to predict genes driving cellular transitions. It is trained on large
> L40: |pretrain_weights.pth|Model parameters pre-trained on 20 million single cells.|link|

## 星数曲线

```mermaid
xychart-beta
    title "DLS5-Omics/CellNavi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-28 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `458d85ba3d21` · [字段定义](../../DATASET.md)*
