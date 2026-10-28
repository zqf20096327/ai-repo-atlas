# d4ichi/PassGAN

⭐ 152 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/d4ichi/PassGAN) · 个人维护

**基于 GAN 的密码猜测模型：生成/训练密码样本（Python3/TF2 更新版）**

PassGAN 论文的代码更新版，命令行训练与采样迁移到 Python 3.12 与 TensorFlow 2（tf.compat.v1），模型基于 Improved Wasserstein GAN。附带在 RockYou 数据集上训练的预训练模型，可用 sample.py 生成指定数量密码样本，或用自有密码泄露数据集训练新模型。Jupyter 调试笔记本仍停留在 TensorFlow 1.x 未迁移。预训练采样已在 Windows 11 x64 CPU 环境验证，无需 CUDA；GPU 训练未在当前环境评估，GTX 1080 训练时长仅为原始环境估计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 命令行接口 sample.py / train.py，支持 Python 3.12 + TensorFlow 2（tf.compat.v1）
- 附带 RockYou 数据集预训练模型，可直接生成密码样本
- 可用自有密码数据集训练，保留原始命令行选项与输出布局
- 含单元测试：验证 24 个生成器张量并与保存的 .meta 图对比输出

## 适用场景

- 用预训练模型批量生成密码样本用于密码强度研究
- 在自有密码泄露数据集上训练 GAN 密码猜测模型
- 复现 PassGAN 论文方法并做兼容性验证

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository is an updated version of @brannondorsey/PassGAN. It contains code for the _PassGAN: A Deep Learning 
> L5: Command-line training and pretrained sampling now support Python 3.12 and TensorFlow 2 using `tf.compat.v1`. The not
> L12: - A pretrained PassGAN model trained on the RockYou dataset

## 星数曲线

```mermaid
xychart-beta
    title "d4ichi/PassGAN 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-10-28"]
    y-axis "stars" 151 --> 153
    line [152, 152]
```

2026-10-25 152 → 2026-10-28 152（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3e9a355e854e` · [字段定义](../../DATASET.md)*
