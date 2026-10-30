# polyaxon/cli

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/polyaxon/cli) · [官网](https://docs.polyaxon.com/) · 组织维护

**面向团队的 MLOps 平台 CLI：训练、跟踪与调度机器学习工作流**

Polyaxon 的核心客户端与命令行工具，用于在其 MLOps 平台上创建项目、上传代码、启动并跟踪实验的日志与资源、启动 Jupyter Notebook 与 TensorBoard。平台部署于数据中心或云厂商，基于 Kubernetes，通过智能容器与节点管理共享 GPU 资源；支持分布式训练（TensorFlow/PyTorch/MPI/Horovod/Ray/Dask）、超参数搜索（网格/随机/Hyperband/贝叶斯等）、并行执行与 DAG 工作流。面向需要复现性、自动化与可扩展性的机器学习团队与企业。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI 管理项目、实验运行、日志与资源跟踪及 Dashboard 启动
- 支持分布式训练：TensorFlow、PyTorch、MPI、Horovod、Ray、Dask
- 超参数搜索：网格、随机、Hyperband、贝叶斯优化、Hyperopt
- 容器原生 DAG 工作流引擎管理多操作依赖的机器学习流水线

## 适用场景

- 团队在 Kubernetes 上共享 GPU 资源运行深度学习实验
- 跟踪与比较多次实验的日志、指标与资源占用
- 用网格/贝叶斯等方法做超参数搜索与并行调参
- 编排由作业、服务、分布式任务组成的 DAG 流水线

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L19: Welcome to Polyaxon, a platform for building, training, and monitoring large scale deep learning applications.
> L24: Polyaxon makes it faster, easier, and more efficient to develop deep learning applications by managing workloads wi
> L131: Polyaxon DAGs is a tool that provides container-native engine for running machine learning pipelines.

## 星数曲线

```mermaid
xychart-beta
    title "polyaxon/cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `57570e1f3022` · [字段定义](../../DATASET.md)*
