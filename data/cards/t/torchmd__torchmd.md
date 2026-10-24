# torchmd/torchmd

⭐ 721 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/torchmd/torchmd) · 组织维护

**基于 PyTorch 的端到端分子动力学引擎，供力场与神经网络势研究**

提供用 PyTorch 进行分子动力学的 API：以 PyTorch 张量运算运行 MD 模拟，单位与经典 MD 代码（ACEMD）一致（kcal/mol、K、g/mol、Å），可将神经网络势集成进动力学过程，面向做力场开发与机器学习势研究的科研人员。项目自述为 WIP 状态。安装依赖 Moleculekit（其读取器为非营利研究许可）；通过 pip/conda 安装，examples 目录提供示例，并推荐参考 TorchMD-Net 与教程 notebook 复现论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- PyTorch 实现的分子动力学 API，支持神经网络势集成到动力学
- 单位与经典 MD 代码（ACEMD）一致
- examples 目录提供多种动力学示例
- 引用信息与论文复现教程 notebook

## 适用场景

- 用力场开发与机器学习势做分子模拟研究
- 在 PyTorch 生态中运行端到端 MD 模拟
- 复现 TorchMD 相关论文实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: TorchMD intends to provide a simple to use API for performing molecular dynamics using PyTorch. This enables researc
> L19:       title={TorchMD: A deep learning framework for molecular simulations},

## 星数曲线

```mermaid
xychart-beta
    title "torchmd/torchmd 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 720 --> 722
    line [721, 721]
```

2026-10-18 721 → 2026-10-24 721（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `96f9b6f17978` · [字段定义](../../DATASET.md)*
