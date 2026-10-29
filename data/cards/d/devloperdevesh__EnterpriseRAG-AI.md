# devloperdevesh/EnterpriseRAG-AI

⭐ 18 · Python · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/devloperdevesh/EnterpriseRAG-AI) · [官网](https://enterpriserag-ai.vercel.app) · 个人维护

**面向企业生产环境的 RAG 与 AI 负载安全治理基础设施平台**

开源 AI 基础设施平台，定位为构建和运行生产级 RAG 系统与 AI agent 负载的基础设施层，覆盖检索基础设施（语义/混合检索、元数据处理、检索诊断）、可观测性（请求生命周期追踪、token 监控、分布式追踪）、安全治理（认证授权、租户隔离、审计日志、策略驱动）与可靠性工程（异步执行、重试、故障诊断），并包含统一的 Enterprise Control Center 运营仪表盘。技术栈为 FastAPI/PostgreSQL/FAISS/React/OpenTelemetry 等，Docker/Kubernetes 部署。多项能力（token 分析、eBPF 内核遥测、治理层）仍处于 Planned/Research 状态。README 未给出具体安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检索基础设施：语义/混合检索、文档处理管道、检索诊断与性能监控
- AI 可观测性：请求生命周期追踪、LLM 执行流、token 用量与分布式追踪
- 安全治理层：认证授权、RBAC、租户数据隔离、审计日志
- 统一 Enterprise Control Center 仪表盘（系统总览/检索智能/安全运营等模块）

## 适用场景

- 为生产级 RAG 系统提供检索、安全与可观测性基础设施
- 企业环境中按租户隔离数据并做审计与策略治理
- 监控 AI 请求全链路：检索阶段、LLM 执行、延迟与 token 成本

## 场景标签

`RAG` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L16: EnterpriseRAG-AI provides an infrastructure layer for building and operating production-grade Retrieval-Augmented G
> L12: EnterpriseRAG-AI is an open-source AI infrastructure platform designed to make enterprise AI workloads secure, obse

## 星数曲线

```mermaid
xychart-beta
    title "devloperdevesh/EnterpriseRAG-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3873a7d68a76` · [字段定义](../../DATASET.md)*
