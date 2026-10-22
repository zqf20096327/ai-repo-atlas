# TrustGen/TrustEval-toolkit

⭐ 136 · Python · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/TrustGen/TrustEval-toolkit) · [官网](https://trusteval-docs.readthedocs.io) · 组织维护 · 中文 README

**生成式基础模型可信度评测工具包与基准（ICLR'26/NAACL'25 Demo）**

TrustGen/TrustEval 是面向生成式基础模型（LLM/VLM/T2I）的可信度评测框架与基准：按安全、公平性、鲁棒性、隐私、真实性等维度，通过动态数据集生成、上下文变异、生成模型回答、裁判评判与指标计算的五步流水线完成评测，并输出交互式 HTML 报告（含模型得分、LLM 生成的性能摘要、错误案例与排行榜）。支持本地与 API 两类模型，本地 T2I 模型需额外安装 diffusers/torch 等依赖，支持 1-8 GPU 并发推理与显存优化。面向研究者的 Python 包，配合 Hugging Face 数据集脚本使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖安全/公平/鲁棒/隐私/真实性等维度的五步评测流水线
- 动态数据集生成与上下文变异（contextual variation）
- 支持 LLM/VLM/T2I 多类模型的本地与 API 调用
- 多 GPU 并发推理（1-8 GPU，官方称 7-8 倍提速）与交互式 HTML 报告

## 适用场景

- 对自有 LLM/VLM/T2I 模型做多维度可信度评测
- 生成安全或公平性维度的测试集并跑通评测流程
- 对比多个模型的可信度表现并生成排行榜报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L15: **Trustgen** is a dynamic and comprehensive framework for evaluating the trustworthiness of Generative Foundation M
> L29: - **Comprehensive Dimensions**: Evaluate models across safety, fairness, robustness, privacy, and truthfulness.
> L234: 1. **Judge the Responses**


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `684b18dde652` · [字段定义](../../DATASET.md)*
