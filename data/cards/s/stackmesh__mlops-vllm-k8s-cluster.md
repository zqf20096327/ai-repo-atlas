# stackmesh/mlops-vllm-k8s-cluster

⭐ 5 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/stackmesh/mlops-vllm-k8s-cluster) · 个人维护

**面向开发者的本地 Kubernetes 集群 vLLM 部署规划平台**

在严格算力预算下运行的开源 LLM 部署平台：规划器按参数量、KV cache 与 MIG profile 内存估算容量，在不满足预算时在创建 pod 前拒绝部署；通过的计划渲染为 vLLM manifest，按副本规模选择 MIG 切片、张量并行或流水线并行。网关从 Qdrant 检索 runbook 片段并校验引用，无引用的回答被替换为守卫原因。提供 CLI、Airflow DAG 包装与 k8s/kind 部署清单；限制部分声明 CI 只做计划与渲染，不启动 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于参数量×字节与 KV cache 估算的容量规划器，预算不满足则在建 pod 前拒绝
- 按副本规模自动选择 MIG 切片 / 张量并行 / 流水线并行并生成 manifest
- 网关校验回答引用必须落在检索到的 doc_id 集合内
- 未设 VLLM_BASE_URL 时可在 CPU 笔记本上运行控制平面

## 适用场景

- 在配额受限的多节点 GPU 集群中规划开源 LLM 部署方案
- 为 vLLM 生成 MIG / 张量并行 / 流水线并行的部署清单
- 搭建带引用校验的 RAG 网关与 Qdrant/MLflow 组件

## 场景标签

`RAG` `推理引擎` `MLOps` · 领域:知识与检索

## 证据(README 行号)

> L3: A high-throughput, low-latency model inference platform. Automates multi-node GPU slicing and open-source LLM deploy
> L7: **Stack:** Kubernetes, vLLM, Triton Inference Server, MLflow, Airflow, PyTorch, Qdrant.
> L116: This is a local reference platform. CI plans and renders; it does not boot a GPU, NCCL, or Triton. The memory math


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4abb341c2fbe` · [字段定义](../../DATASET.md)*
