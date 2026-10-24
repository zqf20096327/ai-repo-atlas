# cleanlab/label-errors

⭐ 190 · Apache-2.0 · 推送 2025-12-16 · [GitHub](https://github.com/cleanlab/label-errors) · [官网](https://labelerrors.com/) · 组织维护

**十大 ML 基准测试集的标注错误修正数据与复现工具**

提供 ImageNet、MNIST、CIFAR-10/100、Caltech-256、QuickDraw、IMDB、Amazon Reviews、20News、AudioSet 十个常见基准测试集的标注错误修正结果与复现工具：修正基于 confident learning（cleanlab v1.0），并在 labelerrors.com 提供在线浏览。仓库不直接发布单一修正版测试集，而是提供构建组件，支持用户自选修正策略（如 mTurk 标注 3/5 或 5/5 共识）。对 QuickDraw、Amazon Reviews 等错误过多的数据集仅提供查找工具；各数据集的下载、预处理与索引对齐代码逐集给出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 10 个常见 ML 基准测试集的标注错误修正
- 基于 confident learning（依赖 cleanlab v1.0）可复现
- 提供 mTurk 标注文件支持不同共识阈值的修正策略
- 为 AudioSet/Amazon Reviews 发布预处理后的 Numpy 版数据集

## 适用场景

- 用修正标签重评模型在基准上的真实表现
- 复现各数据集的标注错误查找流程
- 研究数据集噪声与测试集可靠性问题

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Label Errors in Benchmark ML Test Sets
> L3: This repo provides the tools to clean and correct the test sets for ten of the most common ML benchmark test sets: I
> L15: Label errors are found based on confident learning via the open-source cleanlab package. Specifically, cleanlab v1.

## 星数曲线

```mermaid
xychart-beta
    title "cleanlab/label-errors 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 189 --> 191
    line [190, 190]
```

2026-10-18 190 → 2026-10-24 190（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d9d768447a6f` · [字段定义](../../DATASET.md)*
