# huggingface/hf-csi-driver

⭐ 15 · Go · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/huggingface/hf-csi-driver) · 组织维护

**将 HF Hub 仓库/存储桶以 FUSE 卷挂载进 K8s Pod 的 CSI 驱动**

面向 Kubernetes 用户的 CSI 驱动：把 Hugging Face 存储桶与模型/数据集仓库封装为 hf-mount（Rust FUSE 文件系统）并经 CSI 接口挂载为 Pod 卷。机制包括专用 mount Pod（驱动重启后存活）、以 HFMount CRD 为状态源的自愈重建、HF token 经 Secret 传递并热刷新、孤儿 FUSE 连接周期清理。要求 K8s 1.26+、节点 FUSE 支持、容器以 privileged 运行、DaemonSet 需 hostPID。提供 Helm 与裸清单两种安装方式。

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

- 每个 FUSE 挂载运行在独立 Pod 中，驱动重启后仍存活
- HFMount CRD 作为状态源，mount Pod 崩溃后自动重建
- HF token 经 Kubernetes Secret 传递并通过 requiresRepublish 热刷新
- 孤儿 FUSE 连接周期性扫描清理，避免卡住节点级 sync/umount

## 适用场景

- 在 Kubernetes 中把 HF 模型/数据集仓库直接挂载为 Pod 内卷
- 训练或推理作业直接读取 Hub 上的模型文件而无需预下载
- 通过读写卷将训练产物写入 HF 存储桶

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: Kubernetes CSI driver for mounting Hugging Face Buckets and model/dataset repos as FUSE volumes in pods.
> L5: Wraps hf-mount (Rust FUSE filesystem) behind the CSI interface so kubelet can manage mount lifecycle automatically.

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/hf-csi-driver 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3a78a98fd493` · [字段定义](../../DATASET.md)*
