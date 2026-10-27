# zjunlp/predict-before-execute

⭐ 25 · Python · MIT · 推送 2026-07-07 · [GitHub](https://github.com/zjunlp/predict-before-execute) · 组织维护 · 中文 README

**论文官方实现：用 LLM 预测 ML 代理方案性能，免物理执行**

ACL 2026 论文的官方代码与数据仓库：提出 Data-centric Solution Preference 任务，构建 18,438 对来自 AIDE/AutoMind 在 MLE-bench 上真实执行轨迹的成对比较语料，评测 LLM 是否具备隐式执行先验；并实现 FOREAGENT 代理，采用 Predict-then-Verify 循环，用 LLM 作为隐式世界模型剪枝搜索空间，将探索与物理执行解耦。报告 6 倍加速、3.2 倍更广搜索与对人类榜单选手 +6% 胜率。语料在 Hugging Face 提供，代理实现基于 MLE-bench。

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

- 18,438 对真实执行轨迹构建的方案偏好语料
- 对 LLM（DeepSeek-V3.2、GPT-5.1 等）预测能力的分层评测
- FOREAGENT：Predict-then-Verify 循环的自主代理实现
- 偏好语料经 HuggingFace datasets 一行代码加载

## 适用场景

- 研究 LLM 能否不经执行预测 ML 方案优劣
- 复现论文的语料构建与预测基准实验
- 用 FOREAGENT 思路加速 ML 代理的方案搜索

## 场景标签

`模型评测` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: This repository contains the official implementation and data for the paper **"Can We Predict Before Executing Mach
> L51:  * Leveraging these findings, we developed **FOREAGENT**, an autonomous agent that integrates the "Predict-then-Ver
> L114: Our agent implementation is based on MLE-bench. Please refer to `mle-bench/README.md` for detailed installation an

## 星数曲线

```mermaid
xychart-beta
    title "zjunlp/predict-before-execute 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-27 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a39e7701045c` · [字段定义](../../DATASET.md)*
