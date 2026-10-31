# sgyaqing/RAG-BenchLab

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/sgyaqing/RAG-BenchLab) · 组织维护 · 中文 README

**从自有文档生成评测集并打分 RAG 系统的工具**

面向 RAG 系统的评测工具：用户上传文档，工具生成问答对测试集（自动审查过滤），再通过适配器调用用户的 RAG 系统，用 ragas 0.4.3 计算五个指标（Context Precision/Recall、Faithfulness、Response Relevancy、Answer Correctness）并给出总体与逐题评分。全程在浏览器 UI 完成，无需写代码；支持 Smart Fill 自动生成适配器配置。结果有缓存以减少重复评测的 token 消耗。提供 Docker 镜像与 macOS/Windows 便携包；0.1.1 版无鉴权，需保持在内网或加代理认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一工具内完成测试集生成与 RAG 系统评测
- 基于 ragas 0.4.3 的五个指标，报告含总体分与逐题分
- UI 全流程操作，无需写脚本；Smart Fill 自动生成适配器配置
- 评测结果缓存，调参重复评测更省 token

## 适用场景

- 用自己的文档生成 RAG 评测问答集
- 对 RAGFlow 等 RAG 系统做多指标打分对比
- 调优 RAG 系统时反复评测并跟踪得分

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: A fast, intelligent, out-of-the-box evaluation tool for RAG systems: **build a testset (question–answer pairs) from 
> L52: The metrics are computed by ragas; the definitions below are taken from ragas 0.4.3.
> L33: Add one LLM and one Embedding: fill in Base URL, API Key and Model, then click Save.

## 星数曲线

```mermaid
xychart-beta
    title "sgyaqing/RAG-BenchLab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `785e8cc6892c` · [字段定义](../../DATASET.md)*
