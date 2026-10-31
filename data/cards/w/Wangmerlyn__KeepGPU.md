# Wangmerlyn/KeepGPU

⭐ 40 · Python · MIT · 推送 2026-07-04 · [GitHub](https://github.com/Wangmerlyn/KeepGPU) · 个人维护

**保持共享 GPU 占用的 CLI 工具：按需申请轻量显存占用**

面向共享机器用户的命令行工具，通过周期性申请指定量的显存（如 1GiB、间隔 60 秒）维持 GPU 处于被占用状态，仅在利用率回退允许时分配，Ctrl+C 即释放。后端依赖 PyTorch 能识别目标设备，支持 CUDA、ROCm/HIP 与 Apple Silicon MPS。以 pip 安装的 Python 包形式提供，发布于 PyPI，文档含安装选项与硬件检查指引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 GPU ID 与显存额度周期性申请占用的 CLI
- 仅在利用率回退允许时分配，显存信号轻量
- 支持 CUDA、ROCm/HIP、Apple Silicon MPS（经 PyTorch）

## 适用场景

- 在共享集群上防止空闲 GPU 被他人抢占
- 需要保持 GPU 分配状态的调试或占位场景

## 场景标签

 · 领域:HPC/系统工具

## 证据(README 行号)

> L7: KeepGPU is a small, polite GPU keeper for shared machines. It allocates only
> L18: Press `Ctrl+C` to release. CUDA, ROCm/HIP, and Apple Silicon MPS are supported

## 星数曲线

```mermaid
xychart-beta
    title "Wangmerlyn/KeepGPU 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-31 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `51e4aa952cc7` · [字段定义](../../DATASET.md)*
