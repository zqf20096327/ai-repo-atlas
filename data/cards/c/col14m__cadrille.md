# col14m/cadrille

⭐ 188 · Python · Apache-2.0 · 推送 2026-09-01 · [GitHub](https://github.com/col14m/cadrille) · 组织维护

**多模态 3D CAD 重建研究代码：从点云/图像/文本生成 CadQuery 代码**

论文 cadrille 的官方实现：一种多模态（点云/图像/文本）3D CAD 重建方法，输出 CadQuery 参数化 CAD 代码，使用在线强化学习训练。仓库提供 train.py、test.py、evaluate.py 脚本，支持 DeepCAD、Fusion360、Text2CAD、CAD-Recode 数据集；SFT 与 RL 模型可从 HuggingFace 下载，RL 微调代码暂不提供。安装依赖参照 Dockerfile，需自行下载预处理数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 点云/图像/文本三种模态可组合输入，生成 CadQuery CAD 代码
- 提供训练、推理与评测脚本（IoU、无效比率、chamfer 距离）
- SFT 与 RL 模型权重可从 HuggingFace 下载
- 支持 DeepCAD/Fusion360/Text2CAD/CAD-Recode 四个数据集

## 适用场景

- 复现论文中的 CAD 重建实验与基准评测
- 从点云或图像反推参数化 CAD 模型
- 在 Text2CAD 数据集上训练或微调多模态重建模型

## 场景标签

`多模态` `代码生成` `强化学习` · 领域:编码与开发

## 证据(README 行号)

> L6: This repository contains an implementation of `cadrille`, a multi-modal (point clouds / images / text) 3D CAD recons
> L34: To predict CadQuery codes run *test.py* script:

## 星数曲线

```mermaid
xychart-beta
    title "col14m/cadrille 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 187 --> 189
    line [188, 188]
```

2026-10-18 188 → 2026-10-26 188（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `fb0911db9f3f` · [字段定义](../../DATASET.md)*
