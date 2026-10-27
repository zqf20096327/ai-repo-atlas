# darkmatter2222/COD-MW-2019-DNN

⭐ 82 · Python · GPL-3.0 · 推送 2026-09-13 · [GitHub](https://github.com/darkmatter2222/COD-MW-2019-DNN) · 个人维护

**检测 COD 屏幕中敌人的神经网络模型与训练脚本集**

针对《使命召唤：现代战争 2019》的深度神经网络项目，包含脚本、训练数据（>5GB）、验证数据（>200MB）与 .h5 模型文件。提供两个网络：EnemyDetector 在屏幕中央 200x200 像素块中判定是否存在敌人（基于 Gamertag 检测，置信度>95%输出），HeadHunter 将该区域划为 10x10 网格分类头部位置（102 分类）。模型与数据托管在 Kaggle，本地需 Python venv 与 TensorFlow 2.0，GPU 运行可提升推理帧率（CPU 约 2 FPS，GTX 1080 TI 约 12 FPS）。附带 Overlay 实时显示、自训练数据采集（观看 Twitch 流截图）与训练脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- EnemyDetector：200x200 块内敌人检测，置信度>95% 输出
- HeadHunter：10x10 网格 102 分类定位头部并绘制准星
- 自训练流程：从 Twitch 1080p 流截图按置信度归档并迭代训练
- 提供 .h5 模型、训练/验证数据集（Kaggle 托管）

## 适用场景

- 在 COD 游戏画面上实时检测敌人并叠加显示
- 复用数据集与脚本训练/验证自己的检测网络
- 研究屏幕区域目标检测的自训练数据采集流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: Contained are the scripts, training data, validation data as well as the .h5 model files for various Call of Duty Mo
> L13: Look at a 200x200 pixel block at the center of the uers screen, determine if there is an enemy somewhere in that bl
> L42: Grab the center 200x200 pixel block, and run it through the Neural Network. It will print to the console any time i

## 星数曲线

```mermaid
xychart-beta
    title "darkmatter2222/COD-MW-2019-DNN 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-27 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bff7c51a5ccf` · [字段定义](../../DATASET.md)*
