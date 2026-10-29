# google-deepmind/sam_edge

⭐ 22 · Python · Apache-2.0 · 推送 2026-06-23 · [GitHub](https://github.com/google-deepmind/sam_edge) · 组织维护

**论文实验复现代码：SAM 与稳定性边缘的优化研究**

DeepMind 发布的《Sharpness-Aware Minimization and the Edge of Stability》论文配套实验代码，面向论文读者提供图像分类（MNIST/CIFAR-10，MLP/CNN）与语言建模（Transformer）两类实验的复现入口。通过 python3 -m image_classification / transformer 运行，记录 Hessian 算子范数、主特征值、梯度对齐等训练过程统计并输出 PDF 图表；语言建模数据需自行下载切分。依赖见 requirements.txt，附 run.sh 一键脚本。

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

- 图像分类与语言建模两条实验命令行入口
- 计算并绘制 Hessian 特征值、SAM-edge、梯度对齐曲线等统计
- 以时间限制（time_limit_in_hours）控制训练时长，支持缩小网络与数据集

## 适用场景

- 复现论文中 SAM 与 Edge of Stability 的实验结果
- 检查论文实现细节或在其上运行变体实验
- 研究训练动态中 Hessian 谱的行为

## 场景标签

 · 领域:机器学习研究/优化

## 证据(README 行号)

> L3: This code is provided to enable readers of "Sharpness-Aware Minimization and the Edge of Stability" to reproduce the
> L7: The two commands that run experiments are `image_classification` and `transformer`. The default command-line argumen

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/sam_edge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `76aaac2d0849` · [字段定义](../../DATASET.md)*
