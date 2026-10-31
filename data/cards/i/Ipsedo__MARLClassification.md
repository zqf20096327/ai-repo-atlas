# Ipsedo/MARLClassification

⭐ 48 · Python · 推送 2026-10-23 · [GitHub](https://github.com/Ipsedo/MARLClassification) · 个人维护

**多智能体强化学习图像分类的 PyTorch 研究实现**

论文《Multi-Agent Image Classification via Reinforcement Learning》的 PyTorch 实现：多个 agent 通过 actor-critic 强化学习在图像上选择区域/动作，最终完成图像分类。以 Python 模块形式提供训练命令（python -m marl_classification），支持 CUDA、可配置 agent 数量与网络结构，附 MNIST、NWPU-RESISC45、AID、WorldStrat 数据集下载脚本与训练结果示例。依赖 Python 3.14+ 与 uv 管理环境。README 标注 TODO：WorldStrat 训练、docstring 补全。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多智能体强化学习（actor-critic）实现图像分类
- 支持 CUDA 训练与丰富命令行参数（agent 数、网络结构、学习率等）
- 提供 MNIST/NWPU-RESISC45/AID/WorldStrat 数据集下载脚本
- 仓库内附各数据集训练结果与已训练模型路径

## 适用场景

- 复现多智能体强化学习图像分类论文实验
- 在自有图像数据集上训练多智能体分类模型
- 研究强化学习在视觉任务中的应用

## 场景标签

`强化学习` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: PyTorch implementation of Multi-Agent Image Classification via Reinforcement Learning paper.
> L39: python -m marl_classification -a 3 --step 5 --cuda --run-id train_mnist train --action [[1,0],[-1,0],[0,1],[0,-1]] 

## 星数曲线

```mermaid
xychart-beta
    title "Ipsedo/MARLClassification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fd282502ca52` · [字段定义](../../DATASET.md)*
