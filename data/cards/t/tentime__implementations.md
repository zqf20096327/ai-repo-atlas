# tentime/implementations

⭐ 26 · Python · 推送 2026-04-09 · [GitHub](https://github.com/tentime/implementations) · 个人维护

**机器学习里程碑的从零实现合集：12 个独立教学实现**

按时间线组织的机器学习历史实现集合：从 n-gram 语言模型、反向传播到 Transformer、BERT、GPT、Scaling Laws、LoRA、RLHF 等 12 个里程碑，每个文件夹为独立完整实现，早期用 NumPy 手写梯度，后期用 PyTorch。提供 pytest 行为测试（固定种子、确定性），各实现 CPU 运行时间从数秒到约一小时不等。无共享工具库，文件夹之间无交叉导入。面向学习机器学习原理的开发者与学习者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个里程碑实现覆盖 1948 至 2022 年
- 每个文件夹独立完整，无跨文件夹导入
- 确定性测试（固定种子，单文件夹 <30s）
- 早期实现用 NumPy 手写梯度以呈现数学细节

## 适用场景

- 通过可运行代码学习 Transformer/BERT/GPT 等经典结构
- 理解反向传播与梯度计算的手写实现
- 按时间线纵览机器学习关键转折点

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A temporal museum of machine learning — one self-contained implementation per major milestone, from n-gram language 
> L9: |#|Folder|Era|Stack|CPU time|

## 星数曲线

```mermaid
xychart-beta
    title "tentime/implementations 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c0d21e9642bc` · [字段定义](../../DATASET.md)*
