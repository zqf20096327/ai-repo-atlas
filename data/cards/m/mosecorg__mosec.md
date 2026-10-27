# mosecorg/mosec

⭐ 902 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/mosecorg/mosec) · [官网](https://mosecorg.github.io/mosec/) · 组织维护

**面向开发者的 ML 模型服务化框架，支持动态批处理与流水线**

用 Rust 构建网络层与任务协调、Python 编写服务逻辑的模型 serving 框架：开发者继承 Worker 类编写 forward 处理器，即可把训练好的 ML 模型封装为在线 API 服务。核心机制包括动态批处理（max_batch_size/max_wait_time 聚合请求）、多阶段 CPU/GPU/IO 混合流水线（多进程 + IPC）、模型预热、优雅关闭与 Prometheus 指标，输出 OpenAPI 文档。框架与 ML 框架无关，提供 PyPI/conda/pixi 安装与官方 GPU Docker 镜像。限制：需 Python 3.7+，源码构建需 Rust。

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

- Rust 网络层 + Python 服务逻辑，ML 框架无关
- 动态批处理聚合多客户端请求提升吞吐
- 多阶段流水线（多进程 IPC）处理 CPU/GPU/IO 混合负载
- 内置模型预热、优雅关闭、Prometheus 指标与 OpenAPI 文档生成

## 适用场景

- 把刚训练好的模型快速封装为在线推理 API
- 为 GPU 推理服务做动态批处理与吞吐调优
- 在 Kubernetes/容器环境中部署和管理模型服务
- 一个服务内托管多个模型或多阶段推理流水线

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L25: Mosec is a high-performance and flexible model serving framework for building ML model-enabled backend and microser
> L27: - **Highly performant**: web layer and task coordination built with Rust 🦀, which offers blazing speed in addition 

## 星数曲线

```mermaid
xychart-beta
    title "mosecorg/mosec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 901 --> 903
    line [902, 902]
```

2026-10-18 902 → 2026-10-27 902（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `dfedb0706556` · [字段定义](../../DATASET.md)*
