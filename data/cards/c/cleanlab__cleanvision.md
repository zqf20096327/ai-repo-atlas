# cleanlab/cleanvision

⭐ 1,212 · Python · Apache-2.0 · 推送 2026-01-08 · [GitHub](https://github.com/cleanlab/cleanvision) · [官网](https://cleanvision.readthedocs.io/) · 组织维护

**自动检测图像数据集质量问题的 Python 库，供 CV 项目先审数据**

面向计算机视觉项目数据准备阶段的 Python 包：用少量代码审计任意图像文件夹，自动检测 9 类问题——完全重复、近似重复、模糊、低信息量、过暗、过亮、灰度、异常长宽比、异常尺寸；可只检查指定问题类型并生成报告。适用于分类、分割、目标检测、姿态估计、生成建模等任务前的数据清洗，标签问题需用 cleanlab 包处理。支持 Linux/macOS/Windows，Python 3.10+，pip 安装，提供教程、文档、示例脚本与 HuggingFace/Torchvision 数据集运行指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动检测 9 类图像数据问题（重复/模糊/曝光/尺寸等）
- 统一的 Imagelab 接口，几行代码审计任意格式图像文件夹
- 支持按指定问题类型检查并生成报告
- 提供 HuggingFace/Torchvision 数据集运行示例与示例脚本

## 适用场景

- 模型训练前排查数据集中的低质量与重复图像
- 数据探索阶段生成图像数据质量报告
- 只针对特定问题（如模糊、过暗）做定向检查

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: CleanVision automatically detects potential issues in image datasets like images that are: blurry, under/over-expose
> L61: This package currently detects issues in the raw images themselves, making it a useful tool for any computer vision

## 星数曲线

```mermaid
xychart-beta
    title "cleanlab/cleanvision 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 1211 --> 1213
    line [1212, 1212]
```

2026-10-18 1,212 → 2026-10-29 1,212（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `37eda5ddde9c` · [字段定义](../../DATASET.md)*
