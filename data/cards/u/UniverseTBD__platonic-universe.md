# UniverseTBD/platonic-universe

⭐ 17 · Jupyter Notebook · AGPL-3.0 · 推送 2026-07-27 · [GitHub](https://github.com/UniverseTBD/platonic-universe) · [官网](https://discord.gg/VQvUSWxnu9) · 组织维护

**检验模型表示对齐假说的天文研究代码库**

论文 'The Platonic Universe' 的配套代码，在多模态天文数据（光学/红外图像、光谱、光变曲线、表格星表）上检验 Platonic Representation Hypothesis：提取 ViT/DINOv2/ConvNeXtv2/IJEPA/AstroPT 及时间序列、光谱、表格基础模型的逐层嵌入，用 Mutual k-NN（MKNN）度量计算模型间与模态间表示对齐分数。提供 platonic_universe CLI 与 Python API（import pu），部分模型经可选 extras 安装（sam2/moirai/spectra/tabular/timeseries）。面向复现与扩展该研究的科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 ViT/DINOv2/ConvNeXtv2/IJEPA/AstroPT 等视觉模型及时间序列/光谱/表格基础模型
- 用 Mutual k-NN（MKNN）度量模型间与跨模态表示对齐
- 提供 CLI（platonic_universe run/compare）与 Python API（import pu）
- 覆盖 HSC/JWST/Legacy Survey/DESI 等天文数据集

## 适用场景

- 复现论文中模型表示收敛的实验结果
- 对比不同基础模型在天文数据上的嵌入对齐程度
- 扩展测试新模型或新天文模态的表示一致性

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains the code for testing the **Platonic Representation Hypothesis (PRH)** on astronomical data,
> L98: The code measures **representational alignment** using the Mutual k-Nearest Neighbour (MKNN) metric:
> L103: # Calculate MKNN score between two embedding sets

## 星数曲线

```mermaid
xychart-beta
    title "UniverseTBD/platonic-universe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8a5eaa59f1df` · [字段定义](../../DATASET.md)*
