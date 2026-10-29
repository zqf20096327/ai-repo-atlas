# clearml/clearml-fractional-gpu

⭐ 97 · NOASSERTION · 推送 2026-03-12 · [GitHub](https://github.com/clearml/clearml-fractional-gpu) · [官网](https://clear.ml) · 组织维护

**单 GPU 上多容器共存的驱动级显存限制容器集**

ClearML 提供的预打包 Docker 容器系列，内置 CUDA 11.x/12.x/13.x 与 2/4/8/12 GiB 显存上限，允许多个容器共享同一块 GPU 而互不占用全部显存，通过 --pid=host 使驱动区分容器进程实施限制。支持 NVIDIA（驱动 ≤545.x.x，RTX 10-40 系、A 系列、H100 等）与 AMD GPU，可运行于裸机或 Kubernetes Pod（hostPID: true）。动态 MIG 切分、容器级时间片、统一内存等列为需企业许可的功能；Windows 主机不支持；许可限研究/开发用途，商业产品内使用需购买商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预打包容器含 2/4/8/12 GiB 显存上限，多容器共享同一 GPU
- 基于驱动级的容器显存限制与计算时间片（需 --pid=host）
- 支持 NVIDIA 与 AMD GPU，可用于裸机与 Kubernetes Pod
- 容器内 nvidia-smi 可直接报告本容器的显存限制

## 适用场景

- 让多个团队成员/工作负载共用一块 GPU 而不互相耗尽显存
- 在 Kubernetes Pod 中限制作业显存占用
- 在不使用 MIG 静态分区的情况下共享消费级 GPU

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L12: ClearML offers a comprehensive suite of tools to help AI builders accelerate their AI development and increase util
> L16: * Pre-packaged containers with CUDA 11.x, 12.x and 13.x support, featuring built-in GPU memory limits. Multiple con
> L19: * Driver-level container memory limits and compute-time slicing - With ClearML’s enterprise dynamic fractional-GPU,

## 星数曲线

```mermaid
xychart-beta
    title "clearml/clearml-fractional-gpu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-29 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `685a57633152` · [字段定义](../../DATASET.md)*
