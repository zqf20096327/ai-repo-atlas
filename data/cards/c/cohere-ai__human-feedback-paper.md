# cohere-ai/human-feedback-paper

⭐ 20 · Jupyter Notebook · 推送 2026-08-09 · [GitHub](https://github.com/cohere-ai/human-feedback-paper) · 组织维护

**论文《Human Feedback is not Gold Standard》代码与标注数据仓库**

发布于 ICLR 的研究论文配套仓库：批判性分析人类偏好反馈在 LLM 训练与评估中的作用，发现偏好分数对事实性等维度覆盖不足，且输出的断言性会偏移事实性错误的标注率。仓库含修改版 Potato 标注界面与配置、数据预处理及两轮实验分析 notebook、Prolific 平台收集的未聚合与聚合标注数据（parquet/jsonl）。模型补全生成需 HF_HUB_KEY 与 COHERE_API_KEY 环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 含两轮实验的标注数据集（未聚合/聚合/过滤后 parquet）
- 修改版 Potato 标注界面与多套配置
- 覆盖数据预处理、采样、分析的 notebook

## 适用场景

- 复现论文中人类反馈可靠性分析
- 获取带细粒度错误与偏好评分的标注数据集
- 研究断言性/复杂性对标注的混杂影响

## 场景标签

 · 领域:LLM 评估/科研

## 证据(README 行号)

> L1: # Human Feedback is not Gold Standard
> L7: Human feedback has become the de facto standard for evaluating the performance of Large Language Models, and is incr

## 星数曲线

```mermaid
xychart-beta
    title "cohere-ai/human-feedback-paper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c09448952ecc` · [字段定义](../../DATASET.md)*
