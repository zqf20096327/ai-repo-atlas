# sciai-lab/structures25

⭐ 25 · Python · LGPL-3.0 · 推送 2026-02-02 · [GitHub](https://github.com/sciai-lab/structures25) · [官网](https://sciai-lab.github.io/structures25/) · 组织维护

**机器学习无轨道 DFT：用等变图神经网络学习动能泛函**

JACS 2025 论文 Stable and Accurate Orbital-Free Density Functional Theory Powered by Machine Learning 的配套代码。使用等变图神经网络从数据中学习动能泛函，从而实现无轨道密度泛函理论（OF-DFT）计算。支持两条路径：通过 PyPI 安装 mldft 包后用 mldft_setup 下载模型，对 xyz 文件运行推理（QM9 或 QMUGS 训练的模型）；或 clone 仓库用 uv sync 完成完整研究工作流，含数据生成、训练与密度优化，提供论文复现指南与文档构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 等变图神经网络学习动能泛函实现 OF-DFT 计算
- PyPI 发布 mldft 包，含模型下载与 xyz 推理 CLI
- 完整研究工作流：数据生成、训练、密度优化
- 提供论文复现指南 REPLICATION_GUIDE.md

## 适用场景

- 对分子 xyz 文件做无轨道 DFT 能量/密度计算
- 复现 JACS 2025 论文结果
- 基于 QM9/QMUGS 数据重新训练或扩展动能泛函模型

## 场景标签

 · 领域:计算化学/科学计算

## 证据(README 行号)

> L12: This repository contains the code used in our publication Stable and Accurate Orbital-Free Density Functional Theor
> L104:     author = {Remme, Roman and Kaczun, Tobias and Ebert, Tim and Gehrig, Christof A. and Geng, Dominik and Gerhart

## 星数曲线

```mermaid
xychart-beta
    title "sciai-lab/structures25 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e1de81a8022f` · [字段定义](../../DATASET.md)*
