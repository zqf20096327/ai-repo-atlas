# mlverse/torch

⭐ 569 · C++ · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/mlverse/torch) · [官网](https://torch.mlverse.org) · 组织维护

**R 语言的 Torch 深度学习接口：张量运算与自动微分**

mlverse 维护的 R 包，封装 libtorch 提供 R 语言版本的张量创建、张量与 R 数组的相互转换、autograd 自动求导与 CUDA 支持，用于在 R 中构建与训练深度学习模型。通过 CRAN 的 install.packages 或 GitHub 安装开发版；首次加载包时会自动安装附加软件（libtorch 运行时）。项目自我标注 lifecycle 为 experimental 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- R 中创建/操作 Torch 张量并与 R 数组互转
- autograd 自动微分计算导数
- CRAN 发布，首次加载时自动安装附加运行时
- 支持 CUDA

## 适用场景

- 在 R 环境中原生构建深度学习模型
- 利用自动微分做梯度计算与模型训练
- 复用既有 R 数据处理流程衔接 Torch 张量运算

## 场景标签

 · 领域:深度学习/科学计算

## 证据(README 行号)

> L1: # torch
> L44: In the following snippet we let torch, using the autograd feature,

## 星数曲线

```mermaid
xychart-beta
    title "mlverse/torch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 568 --> 570
    line [569, 569]
```

2026-10-18 569 → 2026-10-22 569（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5ab713bbbd7b` · [字段定义](../../DATASET.md)*
