# ThinkParQ/beegfs-csi-driver

⭐ 78 · Go · Apache-2.0 · 推送 2026-07-16 · [GitHub](https://github.com/ThinkParQ/beegfs-csi-driver) · 组织维护

**让 Kubernetes 容器访问 BeeGFS 并行文件系统的 CSI 驱动**

面向 Kubernetes 等容器编排系统的 Container Storage Interface 驱动，使容器能访问既有 BeeGFS 数据集或按需申请临时/持久的高速共享存储。支持动态与静态供给，可将 BeeGFS 目录作为 Persistent Volume 隔离暴露给应用；Storage Class 可映射 BeeGFS 存储池、配额与条带参数。提供 amd64/arm64 多架构容器镜像、可选 Operator 自动化部署，以及 Nomad 的实验性支持。前置要求：每个 Kubernetes 节点预装 BeeGFS DKMS 客户端，且需已存在 BeeGFS 文件系统。

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

- 动态/静态存储供给，BeeGFS 目录作为 PV 并提供应用间隔离
- Storage Class 映射 BeeGFS 存储池、配额与条带参数
- 支持 ReadWriteOnce/ReadOnlyMany/ReadWriteMany 访问模式
- amd64/arm64 多架构镜像与可选 Operator 部署

## 适用场景

- 在 Kubernetes 中把 HPC 共享数据集挂载给工作负载
- 为分布式训练等作业提供跨节点共享的高速持久存储
- 通过 Storage Class 按不同层级/条带配置申请存储

## 场景标签

 · 领域:云原生存储/HPC

## 证据(README 行号)

> L12: The BeeGFS Container Storage Interface (CSI) driver provides high performing and
> L14: Kubernetes. This driver allows containers to access existing datasets or request

## 星数曲线

```mermaid
xychart-beta
    title "ThinkParQ/beegfs-csi-driver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-29 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `8bdca10a6780` · [字段定义](../../DATASET.md)*
