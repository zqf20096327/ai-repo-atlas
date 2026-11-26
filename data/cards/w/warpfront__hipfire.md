# warpfront/hipfire

⭐ 837 · Rust · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/warpfront/hipfire) · 组织维护

**面向 AMD GPU 的本地 LLM 推理引擎（Rust 编写）**

hipfire 是运行在 AMD GPU 上的 LLM 推理引擎，自带 Rust 运行时、模型实现、量化格式（MQ3–MQ6、MQ4R、MFP4）与 HIP 内核，动态加载 ROCm，热路径不含 Python/PyTorch/CUDA 转译层。提供模型注册表（94 条目）、CLI（pull/run/chat/serve/bench/quantize）和 OpenAI 兼容 HTTP 服务，支持投机解码、多 GPU 专家与张量并行、图像生成。面向拥有 AMD 显卡（RDNA/CDNA、Strix Halo）的本地部署用户。

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

- 自带 Rust 运行时与 HIP 内核，动态加载 ROCm，热路径无 Python/CUDA 转译
- CLI 提供拉取、运行、聊天、服务、基准测试、量化命令
- OpenAI 兼容 API 守护进程（127.0.0.1:11435）
- 支持投机解码（DFlash/MTP）、多 GPU 专家与张量并行、flux.schnell 图像生成

## 适用场景

- 在 AMD 显卡上本地运行和对话开源大模型
- 为本地模型提供 OpenAI 兼容 API 供其他工具调用
- 对模型进行量化与推理基准测试
- 多卡环境下并行运行大参数模型

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L24: hipfire is an inference engine for AMD GPUs. It ships its own Rust runtime,
> L31: `bench`, `quantize`) and an OpenAI-compatible HTTP daemon. Speculative
> L6:  Rust + HIP + Redline. No Python in the hot path. Pull, serve, chat.

## 星数曲线

```mermaid
xychart-beta
    title "warpfront/hipfire 星数(近 25 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 724 --> 847
    line [734, 741, 749, 756, 758, 762, 764, 768, 777, 782, 741, 805, 807, 810, 811, 813, 816, 818, 819, 820, 821, 827, 832, 835, 837]
```

2026-10-24 734 → 2026-11-26 837（+103）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `57a801c0e781` · [字段定义](../../DATASET.md)*
