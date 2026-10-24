# ArnovanHilten/GenNet

⭐ 117 · Jupyter Notebook · Apache-2.0 · 推送 2026-07-29 · [GitHub](https://github.com/ArnovanHilten/GenNet) · 个人维护

**面向遗传学的可解释神经网络框架：用生物学知识定义网络连接**

基于 TensorFlow 的命令行深度学习框架，用于（主要）遗传学的表型预测。用户可通过 topology 文件自行定义网络连接，例如用基因注释把遗传变异分组到基因、通路，形成可解释连接；训练后按权重判断连接重要性。支持从 plink/VCF 文件转换基因型矩阵，提供 convert/train/plot/interpret 等命令及六种解释方法（权重打分、DeepExplain、RLIPP、NID、DFIM、PathExplain），输出性能文本、连接权重 CSV 与 Manhattan/Sunburst 图。提供 Docker 镜像与 Colab 教程。限制：稀疏矩阵乘法不受益于 GPU，官方限定测试环境为 Python 3.10 + TensorFlow 2.2，其他版本可能有依赖冲突；Jupyter notebooks 未更新。

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

- topology 文件自定义网络连接（如变异→基因→通路），生成可解释结构
- plink/VCF 基因型文件自动转换为 genotype.h5 输入
- 六种特征重要性/特征交互解释方法（含 DeepExplain、RLIPP、DFIM 等）
- 输出连接权重 CSV、Manhattan 图与 Sunburst 图可视化

## 适用场景

- 用基因注释等先验知识构建可解释网络做基因型-表型预测
- 识别重要遗传变异与相互作用特征并可视化
- 在 Colab 中单键运行教程试用自有数据

## 场景标签

 · 领域:遗传学/生物信息学

## 证据(README 行号)

> L14: GenNet is a command line tool that can be used to create neural networks for (mainly) genetics. GenNet gives the op
> L16: GenNet framework: interpretable neural networks for phenotype prediction

## 星数曲线

```mermaid
xychart-beta
    title "ArnovanHilten/GenNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 116 --> 118
    line [117, 117]
```

2026-10-18 117 → 2026-10-24 117（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `423e99e53061` · [字段定义](../../DATASET.md)*
