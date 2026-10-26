# FanKang2021/GPU-Health-eXpert

⭐ 85 · C · 推送 2025-10-30 · [GitHub](https://github.com/FanKang2021/GPU-Health-eXpert) · 组织维护 · 中文 README

**Kubernetes 上的 GPU 集群健康监控与诊断系统**

面向大规模 GPU 计算环境的集群健康监控与诊断系统，微服务架构：Python/Flask 后端提供 REST API 与 SSE，Next.js 15 前端仪表板展示集群状态；GPU 检测 Job 执行带宽、P2P、NCCL 性能测试与 DCGM、IB 网络健康检查，并与标准基准值对比，支持 RTX3090/L40S/A100/H100/H200 等多型 GPU。调度模块自动识别空闲节点避免资源冲突。通过 Helm 或 YAML 部署到 Kubernetes，需 NVIDIA GPU 驱动、CUDA、Docker、Helm。README 声明项目由 Cursor 与 v0 两个 AI 工具协作孵化开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GPU 诊断覆盖性能测试（带宽/P2P/NCCL）与硬件检查（DCGM/IB 网络），并与基准值对比
- Web 仪表板实时展示集群概览、单节点详情、历史记录与诊断日志，中英文界面
- 调度系统自动识别空闲节点，避免与生产任务资源冲突
- 支持 Helm 一键部署与 YAML 部署，Job 模板经 ConfigMap 动态管理

## 适用场景

- 运维团队定期体检大规模 GPU 集群的硬件与互联健康状态
- 排查节点 GPU 故障并追溯历史诊断记录
- 在 Kubernetes 环境中调度诊断任务而不影响生产负载

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: **一个基于Kubernetes的智能GPU集群健康监控与诊断系统**
> L30: GHX (GPU Health Expert) 是一个企业级的GPU集群健康监控与诊断系统，专为大规模GPU计算环境设计。系统采用微服务架构，提供自动化GPU诊断、实时监控、智能调度和可视化展示功能。

## 星数曲线

```mermaid
xychart-beta
    title "FanKang2021/GPU-Health-eXpert 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 84 --> 86
    line [85, 85]
```

2026-10-18 85 → 2026-10-26 85（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `51936195905f` · [字段定义](../../DATASET.md)*
