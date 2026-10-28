# IGNF/odeon

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/IGNF/odeon) · 组织维护

**面向 GIS 遥感深度学习的任务无关框架（语义分割转型中）**

ODEON（Object Delineation on Earth Observations with Neural network）是法国国家地理与林业信息局（IGNF）名下的遥感深度学习库：原为语义分割命令行工具集，现转型为面向 GIS 行业的任务无关深度学习框架。新版本处于高开发阶段，README 提供旧版（odeon-legacy 分支）与新版的源码安装流程，因含 GDAL 依赖，建议先用 conda/mamba 建环境再 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 从语义分割 CLI 工具转型为任务无关的遥感深度学习框架
- 基于 PyTorch / PyTorch Lightning / rasterio 技术栈（主题标签声明）
- 提供 legacy 分支与新版两套源码安装路径

## 适用场景

- 对遥感影像做语义分割地物勾绘
- 在 GIS 生产流程中集成深度学习模型训练
- 复用框架开发遥感领域的自定义任务

## 场景标签

`模型训练` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L12: it is now pivoting to an agnostic framework for deep learning applied to
> L8: ODEON stands for Object Delineation on Earth Observations with Neural network.

## 星数曲线

```mermaid
xychart-beta
    title "IGNF/odeon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f615e97bb890` · [字段定义](../../DATASET.md)*
