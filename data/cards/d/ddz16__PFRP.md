# ddz16/PFRP

⭐ 14 · Python · MIT · 推送 2025-11-22 · [GitHub](https://github.com/ddz16/PFRP) · [官网](https://arxiv.org/abs/2511.05859) · 个人维护

**AAAI 2026 论文官方 PyTorch 代码：检索历史预测时序未来**

论文 Predicting the Future by Retrieving the Past 的 PyTorch 实现仓库。方法分两阶段：先用预测性对比学习（PCL）训练回看窗口编码器，将全训练样本特征构建为全局记忆库（GMB）；预测阶段通过检索 GMB 中的历史相似片段增强时序预测模型。仓库提供 TSLib 数据集的预训练编码器与 GMB，以及多组模型实验脚本（如 SparseTSF，含带/不带 PFRP 对照）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段流程：PCL 训练编码器后构建全局记忆库（GMB）
- GMB 以三个 numpy 数组保存（past/feature/future）
- 预置全部数据集的编码器 checkpoint 与 GMB
- 提供带/不带 PFRP 的对照实验脚本

## 适用场景

- 复现 AAAI 2026 论文的时序预测实验结果
- 将 PFRP 检索增强机制接入自己的时序预测模型
- 研究检索增强在长时序预测中的作用

## 场景标签

 · 领域:时间序列预测/机器学习研究

## 证据(README 行号)

> L2: This repository contains the pytorch code for the paper "Predicting the Future by Retrieving the Past”.
> L28: The second stage focuses on prediction through GMB retrieval, i.e., predicting the future by retrieving the past. Y

## 星数曲线

```mermaid
xychart-beta
    title "ddz16/PFRP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `e1a3f9a7db3d` · [字段定义](../../DATASET.md)*
