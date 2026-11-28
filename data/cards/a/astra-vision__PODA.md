# astra-vision/PODA

⭐ 125 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/astra-vision/PODA) · [官网](https://astra-vision.github.io/PODA/) · 组织维护

**研究者：单文本提示引导的零样本域自适应分割框架**

PØDA 是 ICCV 2023 发表的零样本域自适应框架，核心机制为 Prompt-driven Instance Normalization（PIN）：依据目标域文本描述与特征相似度对特征风格做增强，从而将源域分割模型适配到未见目标域。面向计算机视觉研究者，提供源训练、特征优化、模型适配与评估的完整流水线，并支持对单张图像的推理与可视化。安装依赖 conda 环境文件，需自行下载 Cityscapes、ACDC、GTA5 数据集并遵循指定目录结构；目标检测代码在独立分支发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PIN（Prompt-driven Instance Normalization）基于文本提示做特征风格增强
- 仅需一条目标域文本描述即可进行零样本域自适应
- 提供分割任务完整的训练、适配、评估与推理可视化脚本
- 特征增强作用于特征提取器层面，作者演示可迁移到目标检测

## 适用场景

- 用一条文本提示把分割模型适配到夜间/雾天等未见场景
- 在无目标域标注数据的情况下做零样本域自适应
- 在 Cityscapes/ACDC/GTA5 等数据集上复现 ICCV 2023 论文实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: TL; DR: PØDA (or PODA) is a simple feature augmentation method for zero-shot domain adaptation guided by a single t
> L33:  We propose Prompt-driven Instance Normalization (PIN) to augment feature styles based on "feature/target domain de


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `1d5123d45c9b` · [字段定义](../../DATASET.md)*
