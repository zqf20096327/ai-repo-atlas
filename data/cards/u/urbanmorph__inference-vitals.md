# urbanmorph/inference-vitals

⭐ 4 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/urbanmorph/inference-vitals) · [官网](https://vitals.urbanmorph.com) · 个人维护

**本地模型运行与微调的单屏监控仪表盘（Prometheus 原生）**

在 Apple Silicon Mac 或 NVIDIA GPU 的 Linux 上，把模型推理与微调的训练/验证指标与机器的内存、GPU、温度、功耗、电量放在同一条时间线上记录，数据存于 Prometheus，可用自带页面或 Grafana 查看。通过代理接入有 HTTP API 的本地推理引擎，或用 Python 库三行调用上报自定义运行；微调用 train 子命令包裹训练命令。全部数据仅监听本机 127.0.0.1，只采集数值，不收集提示词与回答。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 推理与微调指标和机器内存/GPU/温度/功耗共处一条时间线
- 代理模式接入 Ollama、LM Studio、llama.cpp、MLX 服务器等本地引擎
- Prometheus 存储，Grafana 等外部工具可读取
- 仅监听 127.0.0.1，不采集提示词与回答

## 适用场景

- 在 Mac 上跑本地模型时观察推理速度与内存压力的关系
- 微调训练中判断模型是在学习还是开始记忆样本
- 估算一段运行消耗的电量中 AI 占比与电费成本
- 笔记本上预警电量撑不完当前训练任务

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L10: **Training and inference on one timeline, open and Prometheus-native.**
> L20: the requests they send themselves. inference-vitals sits beside whatever you are running and records both
> L26: - **Model runs**, with any local engine (Ollama, LM Studio, llama.cpp, the MLX servers, Jan, LocalAI) or

## 星数曲线

```mermaid
xychart-beta
    title "urbanmorph/inference-vitals 星数(近 3 点)"
    x-axis ["2026-11-14", "2026-11-16", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-14 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `8759c3a0e3cb` · [字段定义](../../DATASET.md)*
