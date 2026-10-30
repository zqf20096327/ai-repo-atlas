# sbelharbi/sr-caco-2

⭐ 23 · Python · BSD-3-Clause · 推送 2026-01-30 · [GitHub](https://github.com/sbelharbi/sr-caco-2) · [官网](https://sbelharbi.github.io/sr-caco-2) · 组织维护

**共聚焦荧光显微图像超分辨率数据集与基准（NeurIPS 2024）**

面向共聚焦荧光显微镜单图像超分辨率（SISR）研究的公开数据集：包含人上皮细胞系 Caco-2 的低/高分辨率图像对，2,200 张原图、4 种分辨率、3 种荧光标记，切分为 9,937 个 patch，支持 X2/X4/X8 三档放大评估。附带 16 种 SISR 方法的基准结果，并以 CC BY-NC-SA 4.0 许可发布。代码基于 PyTorch 2.0.0，提供 create_env.sh 脚本创建虚拟环境、训练/评估脚本，以及 144 个预训练模型权重（16 方法×3 细胞×3 尺度）托管在 Hugging Face，可复现论文结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2,200 张共聚焦显微图像（4 种分辨率、3 种荧光标记），切分为 9,937 个 patch
- 支持 X2/X4/X8 三档超分辨率评估
- 16 种 SISR 方法的基准结果与挑战性分析
- 提供 144 个预训练模型权重与复现评估脚本

## 适用场景

- 在显微镜图像超分任务上训练和评测深度学习模型
- 复现论文中 16 种 SISR 方法的基准结果
- 开展低光毒性成像参数下的图像质量恢复研究

## 场景标签

`模型评测` `图像视频处理` · 领域:评测与运维

## 证据(README 行号)

> L41: microscopy. In this paper, we introduce a large scanning confocal microscopy
> L52: represents a challenging problem. The dataset is released under a Creative

## 星数曲线

```mermaid
xychart-beta
    title "sbelharbi/sr-caco-2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `128bb55c0545` · [字段定义](../../DATASET.md)*
