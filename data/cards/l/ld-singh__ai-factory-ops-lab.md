# ld-singh/ai-factory-ops-lab

⭐ 19 · Shell · MIT · 推送 2026-09-14 · [GitHub](https://github.com/ld-singh/ai-factory-ops-lab) · [官网](https://ld-singh.github.io/ai-factory-ops-lab/) · 个人维护

**无需自购 GPU 的 AI/HPC 基础设施运维实操课程**

面向有终端与 Kubernetes 基础的工程师的动手课程：在笔记本上用 kind + KWOK + fake-gpu-operator 模拟 NVIDIA GPU 控制平面，覆盖 K8s GPU 调度、KAI 队列配额、HAMi GPU 共享、Volcano gang 调度、Slurm（假 GRES）、Prometheus/Grafana 可观测性与推理基准。课程 0–5 课全部无 GPU（$0），唯一真 GPU 课（第 6 课）用 $5–10 租一张入门级 NVIDIA 卡验证驱动到 Pod 路径、HAMi 共享与 DCGM 遥测。每课以模拟/真硬件模式明确标注边界，仿真模式不证明 CUDA 性能、MIG 隔离与多机分布式等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- kind + KWOK + fake-gpu-operator 模拟 GPU 控制平面，零 GPU 零云费完成 0–5 课
- 第 6 课单次 $5–10 租赁 GPU 验证真实驱动路径、HAMi 共享与 DCGM 遥测
- 覆盖 KAI Scheduler 队列配额、Volcano gang 调度、Slurm GRES/QoS、TTFT/goodput 推理 SLO
- make check / make help 命令索引与每课 evidence 捕获脚本

## 适用场景

- 不买 GPU 学习 Kubernetes GPU 调度与排障
- 练习 HAMi GPU 共享、Slurm 队列与 GPU 可观测性运维
- 用一张廉价租用 GPU 验证真实 GPU 运行时路径与基准

## 场景标签

`教程课程` `MLOps` · 领域:学习与行业

## 证据(README 行号)

> L19: A guided, learn-by-doing course in **AI/HPC infrastructure operations**: NVIDIA GPU
> L23: You don't read this repo - you *run* it. Each lesson has you stand something up,
> L72: - **🟦 Simulation mode (no GPU).** kind + KWOK fake nodes with the fake-gpu-operator

## 星数曲线

```mermaid
xychart-beta
    title "ld-singh/ai-factory-ops-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d1f102b7a112` · [字段定义](../../DATASET.md)*
