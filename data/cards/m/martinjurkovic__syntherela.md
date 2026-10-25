# martinjurkovic/syntherela

⭐ 69 · Python · MIT · 推送 2026-06-09 · [GitHub](https://github.com/martinjurkovic/syntherela) · 个人维护

**合成关系数据库生成方法的评测基准框架**

SyntheRela 是一个用于评测与比较合成关系数据库生成方法的基准库：在多个真实数据库上评估合成数据的保真度与效用，提供面向关系数据的新评测指标（如卡方检验、MMD），支持开源与商业生成方法，并可在自定义数据集上运行、可扩展新指标。研究以 ICLR 2025 Workshop 论文形式发表，另在 Hugging Face 维护公开排行榜（由维护者在标准化硬件上执行评测，单张 NVIDIA H100、每数据集 48 小时限时）。以 Python 包经 pip 安装，附带示例 notebook 与复现论文结果的文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨多个真实数据库评估合成关系数据的保真度与效用
- 提供面向关系数据的新评测指标，可扩展自定义指标
- 支持在用户自定义数据集上运行评测
- 维护 Hugging Face 官方排行榜，评测在标准化硬件上由维护者执行

## 适用场景

- 评测自己生成的关系型合成数据质量
- 对比不同合成数据生成方法的表现
- 复现论文基准结果或提交新方法到排行榜

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L18: SyntheRela is a comprehensive benchmark designed to evaluate and compare synthetic relational database generation m
> L22: Our research on SyntheRela is presented in the paper **"SyntheRela: A Benchmark For Synthetic Relational Database G

## 星数曲线

```mermaid
xychart-beta
    title "martinjurkovic/syntherela 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 67 --> 70
    line [68, 69, 69]
```

2026-10-18 68 → 2026-10-25 69（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `85d96dfb0117` · [字段定义](../../DATASET.md)*
