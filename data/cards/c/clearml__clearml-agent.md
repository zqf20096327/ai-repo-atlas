# clearml/clearml-agent

⭐ 314 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/clearml/clearml-agent) · [官网](https://clear.ml/docs/) · 组织维护

**面向 ML/DL 研发与运维的实验调度与集群执行 Agent**

ClearML Agent 是监听 ClearML 任务队列、拉取实验、构建执行环境（virtualenv 或 Docker 容器）、运行代码并监控进度的调度执行代理，覆盖本地、云与混合 GPU 资源，支持云自动扩缩容、优先级队列与 K8s Glue 模式（将 ClearML 任务映射为 K8s Job），可选 SLURM 集成。配合 ClearML Server（自托管或免费托管）使用，通过 pip 安装、clearml-agent init 配置后以 daemon 方式运行，GPU 分配由 --gpus 或 NVIDIA_VISIBLE_DEVICES 控制。3.0.0 起提供 bootstrap 包以预编译二进制加速容器冷启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 监听队列拉取实验，自动建 virtualenv 或 Docker 环境并执行监控
- 可选 Kubernetes Glue 模式将任务映射为 K8s Job（含 Helm Chart）
- 优先级队列、多 GPU 分配（--gpus / NVIDIA_VISIBLE_DEVICES）与 Docker 模式
- bootstrap 包预编译 Python/Git 二进制加速容器任务冷启动

## 适用场景

- 把任意 GPU 机器组成动态集群跑 ClearML 实验
- 在 Kubernetes 上为 ClearML 任务补充调度能力
- 无人值守运行实验并从 Web UI 监控与中止

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L2: MLOps/LLMOps scheduler & orchestration solution supporting Linux, macOS and Windows**
> L102: The ClearML Agent is a job scheduler that listens on job queue(s), pulls jobs, sets the job environments, executes
> L103: job and monitors its progress.

## 星数曲线

```mermaid
xychart-beta
    title "clearml/clearml-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 313 --> 315
    line [314, 314]
```

2026-10-18 314 → 2026-10-28 314（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `75b014e3effc` · [字段定义](../../DATASET.md)*
