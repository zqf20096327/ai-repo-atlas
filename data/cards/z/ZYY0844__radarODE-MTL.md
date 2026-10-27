# ZYY0844/radarODE-MTL

⭐ 58 · Python · 推送 2026-01-26 · [GitHub](https://github.com/ZYY0844/radarODE-MTL) · 组织维护

**毫米波雷达非接触 ECG 重建的深度学习官方实现**

radarODE 与 radarODE-MTL 两篇论文的官方代码仓库，基于 PyTorch 与多任务学习框架 LibMTL 实现：radarODE 面向单周期 ECG 恢复的鲁棒性，radarODE-MTL 面向长期 ECG 恢复，核心机制是以 ODE 解码器生成 ECG 参考辅助域变换，并通过离心梯度对齐提升运动鲁棒性。输入为 MMECG 数据集生成的 50x71x120 时频谱图。面向科研复现与验证，README 建议新用户参考后续工作 CFT-RFcardi。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- radarODE 与 radarODE-MTL 两篇论文的官方 PyTorch 实现
- ODE 解码器生成 ECG 参考以辅助长期 ECG 域变换
- 基于 LibMTL 的多任务学习框架，支持多种 MTL 架构与优化策略
- 提供 MMECG 数据预处理脚本与演示文稿

## 适用场景

- 复现雷达 ECG 重建论文实验结果
- 研究运动鲁棒的非接触心电/生命体征监测方法
- 基于 LibMTL 框架做多任务学习实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: ``radarODE-MTL`` is an open-source repository built on PyTorch and Multi-Task Learning (MTL) framework LibMTL and co
> L6: 1. radarODE: An ODE-embedded deep learning model for contactless ECG reconstruction from millimeter-wave radar
> L7: 2. radarODE-MTL: A Multi-Task Learning Framework with Eccentric Gradient Alignment for Robust Radar-Based ECG Recons
> L21: This repository contains two of our studies to improve the robustness of ECG recovery using the multi-task learning

## 星数曲线

```mermaid
xychart-beta
    title "ZYY0844/radarODE-MTL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 56 --> 59
    line [57, 58, 58]
```

2026-10-18 57 → 2026-10-27 58（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `93bc18683daf` · [字段定义](../../DATASET.md)*
