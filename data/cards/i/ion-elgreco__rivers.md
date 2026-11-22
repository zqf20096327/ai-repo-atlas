# ion-elgreco/rivers

⭐ 107 · Rust · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/ion-elgreco/rivers) · [官网](https://orchestrator.rs) · 个人维护

**面向数据/ML 管道的 Rust 编排平台，Python 定义管道**

以数据资产为核心的编排平台：用 Python 函数定义数据资产，平台在编译后的 Rust 中完成依赖图解析、执行计划、分区逻辑与调度，控制面不运行 Python 解释器。支持单/多输出/子 DAG/外部资产类型，静态与时间窗等多维分区，内置内存、pickle、Delta Lake（含 merge）与 Apache Iceberg（含 upsert）IO 处理器，提供并行子进程与 K8s 逐 pod 执行、声明式调度与传感器、回填策略及嵌入式 SurrealDB 存储。单二进制开发模式下一条命令启动存储、调度器与 Web UI。

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

- 图解析、调度等热路径在 Rust 中运行，官方称数千节点图计划时间为亚毫秒级
- 内置 Delta Lake merge 与 Apache Iceberg upsert IO 处理器
- 提供 Kubernetes operator、CRD 与 Helm charts，多架构镜像发布于 ghcr.io
- Python 定义管道，控制面无 Python 解释器

## 适用场景

- 用 Python 定义带依赖图的数据资产管道并自动调度
- 在 Kubernetes 上以 pod-per-step 方式分布式执行管道
- 对 Delta Lake/Iceberg 表做带分区的回填与 upsert 写入
- 本地单进程起一套含 Web UI 的开发环境

## 场景标签

`工作流自动化` `MLOps` · 领域:效率与自动化

## 证据(README 行号)

> L5: rivers is a Rust-powered orchestration platform built around data assets. Define pipelines in Python; rivers resolve
> L11: - **Asset-based orchestration** — define data assets as Python functions; rivers resolves the dependency graph auto
> L16: - **Parallel & distributed execution** — `Executor.parallel()` for concurrent subprocess workers, `Executor.kuberne


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `2d32a1892efa` · [字段定义](../../DATASET.md)*
