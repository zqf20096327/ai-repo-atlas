# JawherKl/AegisOps

⭐ 4 · Python · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/JawherKl/AegisOps) · 个人维护

**面向研究者的 LLM+DevOps 自动化可复现实验平台**

作为博士论文的 artifact companion 开源的研究实验床：提供 Kind 三节点 Kubernetes 环境、Prometheus/Loki/Tempo/Grafana 全栈可观测组件、标准化故障注入库（Chaos Mesh 三层分类与 ground-truth JSON）与统一 TelemetryEvent 遥测归一层，配套 aegisops-collect CLI。LLM 后端以 Ollama 本地推理为主、预留接口对接前沿模型基线；基线 RCA agent 与评测基准仍在路线图中尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一条 `make up` 命令拉起 Kubernetes+可观测栈测试床
- Chaos Mesh 三层故障分类与带 ground-truth 标签的注入记录
- 统一 TelemetryEvent 遥测 schema 与 aegisops-collect CLI
- 可插拔 LLM 后端：Ollama 本地推理加前沿模型基线接口

## 适用场景

- 在可复现环境中研究 LLM 驱动的根因分析（RCA）
- 对自愈/自动修复 agent 做安全性与准确性评测
- 基于故障注入与 ground-truth 标注构建 DevOps 基准数据集

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: AegisOps is an **open, reproducible research testbed** for investigating how Large Language Models (LLMs) and class
> L30: > **Research context.** This repository is the artifact companion to a PhD thesis on AI-augmented DevOps automation
> L42: |5|Baseline RCA agent|🔄 Next|Ollama-backed agentic loop|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `96fae071c1b7` · [字段定义](../../DATASET.md)*
