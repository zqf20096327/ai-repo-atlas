# FareedKhan-dev/multi-agent-training-grpo

⭐ 66 · Jupyter Notebook · MIT · 推送 2026-02-09 · [GitHub](https://github.com/FareedKhan-dev/multi-agent-training-grpo) · [官网](https://medium.com/@fareedkhandev/building-modern-ai-agentic-systemagentic-system-optimization-for-effective-planning-and-tool-f698e831d730) · 个人维护

**GRPO 训练多智能体系统的教程：数据预处理到强化学习实践**

由 Fareed Khan 撰写的博客式教程仓库，讲解 GRPO 算法在多智能体系统中的作用（组内轨迹比较、相对优势学习、错误抑制、子智能体协调），并以代码演示训练数据预处理：加载 Hugging Face 的 DeepMath-103K（约 103,022 条数学题）与 Natural Questions（约 79,168 条真实用户问题）两个数据集，清洗、转换为统一 schema（id/question/chain/result/source/extra_info）并合并打乱，供后续 GRPO 训练智能体规划能力使用。内容以教学讲解为主。

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

- 讲解 GRPO 在多智能体训练中的五项机制（组评估、相对优势、错误抑制等）
- DeepMath-103K 与 Natural Questions 两数据集的加载、清洗与统一 schema 转换代码
- 合并两数据集为单一训练集（约 182,190 条）并打乱分配新 ID

## 适用场景

- 学习 GRPO 算法如何改进智能体规划与减少幻觉
- 参考多智能体训练数据的预处理与合并流程
- 复用 Hugging Face datasets 的数据清洗与转换代码模式

## 场景标签

`教程课程` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L18: In this blog …
> L20: > We are going to **learn and understand how the GRPO algorithm is related to AI Agents**, and then **create a mult
> L58: We are going to use two huggingface datasets to prepare our training data:

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/multi-agent-training-grpo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-31 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `617f9d73edf2` · [字段定义](../../DATASET.md)*
