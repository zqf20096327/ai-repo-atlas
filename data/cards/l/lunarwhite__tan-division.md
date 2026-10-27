# lunarwhite/tan-division

⭐ 64 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/lunarwhite/tan-division) · 个人维护 · 中文 README

**基于谭松波酒店评论数据集的中文情感分析训练项目**

以 RNN、LSTM、Bi-LSTM 为基础模型的中文文本情感二分类训练项目，数据集为谭松波酒店评论（pos/neg 各 2000 条 txt）。使用 TensorFlow 2.0.0 + Keras 2.3.1 + Python 3.6.2 搭建训练流程，包含分词、序列补全/裁剪、索引化、Zhihu_QA Word+Ngram 词向量构建等预处理步骤，支持在 run.py 中调节学习率、epochs、batch_size、dropout 等参数，README 报告测试集准确率为 92%。以源码仓库形式提供，需 clone 后按步骤配置环境并下载中文词向量。

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

- RNN/LSTM/Bi-LSTM 三种基础模型的中文情感二分类训练
- 完整预处理流程：分词、补全裁剪、索引化、预训练词向量
- 支持学习率/epochs/batch_size/dropout/early-stopping 等参数调节
- 提供 loss 与 accuracy 的可视化训练分析

## 适用场景

- 我想跑一个中文情感分析的端到端训练示例
- 学习 RNN/LSTM 在中文短文本分类上的完整工作流
- 在谭松波酒店评论数据集上复现并调参实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L20: - 基于谭松波老师的酒店评论数据集的中文文本情感分析，二分类问题
> L22: - 选择 RNN、LSTM 和 Bi-LSTM 作为基础模型，借助 Keras 搭建训练

## 星数曲线

```mermaid
xychart-beta
    title "lunarwhite/tan-division 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 62 --> 65
    line [63, 64, 64]
```

2026-10-18 63 → 2026-10-27 64（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e78ba1cd2e9f` · [字段定义](../../DATASET.md)*
