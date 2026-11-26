# ccfos/huatuo

⭐ 1,152 · Go · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/ccfos/huatuo) · [官网](https://huatuo.tech/) · 组织维护 · 中文 README

**基于 eBPF 的 Linux 内核与 Agent 沙箱可观测性工具**

滴滴开源、CCF 孵化的云原生操作系统可观测性项目：整合 kprobes/tracepoints/ftrace/eBPF 提供内核级指标、运行时上下文自动捕获与性能剖析，覆盖内存、调度、网络、块 I/O，宣称开销低于 1%。支持 GPU/NPU 异构硬件监控，可对接 Prometheus/Grafana/Pyroscope/Elasticsearch 并自动关联 Kubernetes 容器标签。通过 Docker 镜像或 Docker Compose 部署，要求内核 4.18 及以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- eBPF 内核级观测，覆盖内存/CPU 调度/网络/块 I/O
- AutoTracing 自动触发与快照保留机制
- 持续性能剖析（CPU/Memory/I/O/Locks）
- 对接 Prometheus/Grafana/Pyroscope/Elasticsearch 并关联 K8s 容器标签

## 适用场景

- 云原生集群的内核级故障排查
- AI 基础设施中 CPU idle 下降、I/O 激增等性能抖动定位
- 混沌工程与稳定性建设中的持续性能剖析

## 场景标签

 · 领域:云原生/系统可观测性

## 证据(README 行号)

> L24: **HUATUO**, named after Hua Tuo, a legendary physician in ancient China, is a cloud-native OS observability project
> L30: - **Kernel-Wide Insight**: Leverages eBPF to keep performance overhead below 1%, delivering full-stack, low-level o
> L34: - **Heterogeneous Computing Hardware**: Encompassing core system components such as CPUs, memory, PCIe interconnect

## 星数曲线

```mermaid
xychart-beta
    title "ccfos/huatuo 星数(近 13 点)"
    x-axis ["2026-10-24", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-20", "2026-11-22", "2026-11-26"]
    y-axis "stars" 1134 --> 1153
    line [1135, 1136, 1135, 1136, 1137, 1135, 1139, 1146, 1147, 1148, 1151, 1152, 1152]
```

2026-10-24 1,135 → 2026-11-26 1,152（+17）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `535fd68c26e8` · [字段定义](../../DATASET.md)*
