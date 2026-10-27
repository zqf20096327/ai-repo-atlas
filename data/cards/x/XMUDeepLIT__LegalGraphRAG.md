# XMUDeepLIT/LegalGraphRAG

⭐ 64 · Python · 推送 2026-08-03 · [GitHub](https://github.com/XMUDeepLIT/LegalGraphRAG) · [官网](https://arxiv.org/abs/2605.28120) · 组织维护 · 中文 README

**法律判决预测的多智能体图 RAG 评测框架（论文官方代码）**

ACL'26 论文 LegalGraphRAG 的官方实现：面向法律推理的评测框架，整合多智能体图检索增强生成，提供可复现的主实验流水线。自动计算罪名、法条、刑期三类指标；内置 14,049 案例图语料与 568 案例 CAIL 评测集（另含 CMDL 1,374 条）；支持 Qwen、DeepSeek、GPT、InternLM、GLM、Gemma 等模型与多 GPU 分布执行。主实验需 Python 3.10+、CUDA 环境与本地嵌入服务（默认 bge-m3，经 localhost:11434 端点）。基线系统（HippoRAG2、LightRAG 等）不含在仓库内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动计算罪名/法条/刑期的 exact-match、Micro-F1 与月数 MAE 指标
- 内置 14,049 案例图语料与 568 案例 CAIL 评测集
- 支持 Qwen/DeepSeek/GPT/InternLM/GLM/Gemma 等模型，多 GPU 分布运行
- 图数据库可持久化复用（--no-build-graph 跳过重建）

## 适用场景

- 复现论文主实验并生成 Table 2 指标
- 在 CAIL/CMDL 数据集上评测法律判决预测
- 更换 LLM 后端对比图 RAG 法律推理效果

## 场景标签

`多智能体` `模型评测` `知识图谱` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: > An evaluation framework for legal judgment prediction that integrates multi-agent graph retrieval and provides a r
> L7: - ✅ **Automated Evaluation**: Computes charge, law-article, and imprisonment metrics for the main LegalGraphRAG expe
> L112: Baseline systems such as HippoRAG2, RAPTOR, LightRAG, LegalDelta, and ADAPT are not included in this repository. T

## 星数曲线

```mermaid
xychart-beta
    title "XMUDeepLIT/LegalGraphRAG 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-27"]
    y-axis "stars" 60 --> 65
    line [61, 62, 64, 64]
```

2026-10-18 61 → 2026-10-27 64（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `7f7bd9a1ccf2` · [字段定义](../../DATASET.md)*
