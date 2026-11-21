# anupbagale/cnn-one-image

⭐ 5 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/anupbagale/cnn-one-image) · 个人维护

**用 NumPy 从零复现 CNN，逐层讲解单张 MRI 图像的分类过程**

教学型仓库：将一张合成脑部 MRI 切片逐层送入纯 NumPy 实现的卷积网络，展示 conv、ReLU、max-pool、dense 与 softmax 每一步的实际数值，仅 dense 层参与训练（softmax 回归，1,000 张合成切片）。面向想理解 CNN 内部机制的学习者与教学者。README 明确声明局限：数据为合成、卷积核手工设定，不构成临床工具。运行仅需笔记本 CPU，含 pytest 测试与可视化复现脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 NumPy 约 70 行实现的 conv2d/relu/max_pool/dense/softmax，无深度学习框架
- 展示每层输出的实际数值与证据图，可对照 CAM/Grad-CAM 概念
- 附反事实测试：去除病灶后预测翻转为 normal
- laptop CPU 半分钟内跑完，可复现全部图像

## 适用场景

- 想逐层看清 CNN 内部数值变化的学习者自学
- 教学中演示卷积、池化与 softmax 的实际计算
- 作为把实现迁移到 PyTorch 或换成真实数据集的练习起点

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L13: Most CNN tutorials show a diagram of boxes. This repo shows **the actual numbers** inside each box for
> L35: > **Why synthetic?** No patient data, no licence, no download. Anyone can clone the repo and reproduce every

## 星数曲线

```mermaid
xychart-beta
    title "anupbagale/cnn-one-image 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-10-31", "2026-11-21"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-28 4 → 2026-11-21 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ed8e5fbfdb99` · [字段定义](../../DATASET.md)*
