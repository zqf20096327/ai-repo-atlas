# mashijie1028/Happy-CGCD

⭐ 49 · Python · MIT · 推送 2026-08-26 · [GitHub](https://github.com/mashijie1028/Happy-CGCD) · [官网](https://arxiv.org/abs/2410.06535) · 个人维护

**NeurIPS 2024 论文 Happy 的 C-GCD 官方 PyTorch 实现**

持续广义类别发现（C-GCD）方法 Happy 的官方代码库：在无监督持续学习设定下同时处理旧类与新类样本，核心机制为难度感知原型采样与软熵正则化。训练分两阶段：Stage-0 有标注离线训练，Stage-1~T 无标注持续训练，通过 train_happy.py 脚本配合命令行参数执行。README 提供 CIFAR-100 与 CUB 的完整训练命令，另列出 TinyImageNet、ImageNet-100、Stanford Cars、FGVC-Aircraft 共 6 个实验数据集，需在 config.py 中配置数据路径并使用 CUDA GPU。扩展版 Happy++ 已被 TPAMI 接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段训练流程：离线有标注训练 + 无标注持续训练
- 支持 CIFAR-100、ImageNet-100、CUB、Stanford Cars 等 6 个数据集
- 单一 train_happy.py 脚本通过命令行参数控制训练
- 对应 NeurIPS 2024 论文，扩展版已被 TPAMI 接收

## 适用场景

- 复现论文中的 C-GCD 实验结果
- 在自有数据集上做持续新类发现研究
- 作为 C-GCD 方向方法的对比基线

## 场景标签

 · 领域:机器学习研究/持续学习

## 证据(README 行号)

> L3: Official implementation of our NeurIPS 2024 paper: **Happy: A Debiased Learning Framework for Continual Generalized 
> L35: CUDA_VISIBLE_DEVICES=0 python train_happy.py --dataset_name 'cifar100' --batch_size 128 --transform 'imagenet' --lr

## 星数曲线

```mermaid
xychart-beta
    title "mashijie1028/Happy-CGCD 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-27 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5e2a3f664a04` · [字段定义](../../DATASET.md)*
