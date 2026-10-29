# yueqingliang1/UNBench

⭐ 17 · Jupyter Notebook · MIT · 推送 2026-01-23 · [GitHub](https://github.com/yueqingliang1/UNBench) · [官网](https://arxiv.org/abs/2502.14122) · 组织维护

**基于联合国安理会记录的 LLM 政治决策基准（四任务）**

论文 Benchmarking LLMs for Political Science 的数据与代码仓库：基于联合国安理会记录构建多阶段基准，覆盖共同起草者选择、投票模拟、决议通过预测、外交声明生成四个任务。仓库内提供每任务约 30 个代表性样本及 Jupyter Notebook 运行脚本，完整数据集经 Google Drive 发布；默认接入 Together API，也可替换为用户自有 LLM。任务 2/3 输出 Accuracy、AUC、F1 等指标，任务 4 计算 ROUGE-L。面向政治科学与 LLM 评测研究者。

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

- 四任务覆盖起草、投票、通过与声明生成的决策流程
- 每任务发布约 30 个代表性样本，完整数据集托管于 Google Drive
- 任务 2/3 输出 Accuracy/AUC/F1，任务 4 输出 ROUGE-L
- AAAI 2026 (Oral) 论文配套代码与数据

## 适用场景

- 评测 LLM 在高风险政治决策任务上的表现
- 复现论文中的投票模拟与决议通过预测实验
- 获取联合国安理会决议结构化数据用于研究

## 场景标签

 · 领域:LLM 评测/政治科学

## 证据(README 行号)

> L3: UNBench is a comprehensive multi-stage benchmark built on United Nations Security Council (UNSC) records to evaluate
> L16: This repository provides tools and sample data for analyzing, simulating, and generating content related to UNSC dr

## 星数曲线

```mermaid
xychart-beta
    title "yueqingliang1/UNBench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `6c6300b450fe` · [字段定义](../../DATASET.md)*
