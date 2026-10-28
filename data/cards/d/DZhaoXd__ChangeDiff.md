# DZhaoXd/ChangeDiff

⭐ 55 · Jupyter Notebook · 推送 2026-03-18 · [GitHub](https://github.com/DZhaoXd/ChangeDiff) · 组织维护

**扩散模型生成多时相遥感变化检测合成数据的 PyTorch 实现**

AAAI-2025 论文 ChangeDiff 的官方 PyTorch 实现：基于扩散模型，通过灵活的文本提示生成多时相语义变化合成数据，用于变化检测任务。在稀疏标注的 SECOND 数据集上训练，支持训练、采样与测试脚本，提供数据预处理流程，可接入自有数据。环境通过 conda 创建（Python 3.8.5、PyTorch 1.13.1、CUDA 11.7），训练与采样各以 bash 脚本启动。部分代码改编自 FreestyleNet、TokenCompose 与 A2Net，采用 Apache 2.0 许可证发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于扩散模型与文本提示生成多时相语义变化数据
- 在稀疏标注的 SECOND 数据集上训练
- 提供训练、采样、测试脚本与数据预处理流程
- 支持使用自有数据（preprocess_data）

## 适用场景

- 为遥感变化检测生成稀缺标注的合成训练数据
- 复现 AAAI-2025 ChangeDiff 论文实验
- 基于自有遥感数据训练变化数据生成模型

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: (AAAI-2025) ChangeDiff: A Multi-Temporal Change Detection Data Generator with Flexible Text Prompts via Diffusion Mo
> L4: This is a pytorch implementation of our paper ChangeDiff.
> L8: It is trained on the sparsely labeled semantic change detection SECOND (Yang et al. 2021) dataset.

## 星数曲线

```mermaid
xychart-beta
    title "DZhaoXd/ChangeDiff 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bab87580156d` · [字段定义](../../DATASET.md)*
