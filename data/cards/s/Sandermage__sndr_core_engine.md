# Sandermage/sndr_core_engine

⭐ 133 · Python · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/Sandermage/sndr_core_engine) · [官网](https://github.com/Sandermage/sndr_core_engine) · 个人维护

**让 vLLM 在消费级 24GB NVIDIA 卡上运行 Qwen3.6/Gemma4 的运行时补丁层**

面向 vLLM 的内存态补丁覆盖层（非 fork）：启动时通过 vllm.general_plugins 入口点按锚点应用 329 个补丁，使 Qwen3.6（7B-35B-A3B）与 Gemma 4（26B/31B/DiffusionGemma）在 RTX 3090/4090/5090、A5000 等 24GB 级卡上运行，提供 TurboQuant k8v4 KV 量化、MTP 投机解码、混合 GDN 注意力与量化后可用的工具调用，服务上下文至 280K。附 GUI Control Center、15 个预设与持久化神经图记忆组件（CPU 容器）。要求 Linux + CUDA + Docker，Mac/Windows 仅可远程客户端模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 启动时内存态应用 329 个补丁，不改 vLLM 磁盘文件、不 fork
- TurboQuant k8v4 KV 量化使 24GB 卡服务 280K 上下文
- MTP 投机解码 + 量化模型上 7/7 工具调用门通过
- 附带 GUI Control Center 与持久化神经图记忆（CPU 容器，零 GPU 热路径）

## 适用场景

- 在 24GB 消费级卡上本地服务 35B 级模型做推理与工具调用
- 数据不可出楼的本地自托管 LLM 部署
- 性能工程师复现补丁注册表与基准套件数据

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L51: transforms the open-source vLLM engine
> L150: A **drop-in runtime patcher** for vLLM. It pins to a specific vLLM nightly
> L163: **The overlay / apply model.** Genesis never edits vLLM on disk. At every

## 星数曲线

```mermaid
xychart-beta
    title "Sandermage/sndr_core_engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 132 --> 134
    line [133, 133]
```

2026-10-18 133 → 2026-10-22 133（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `89b480cf3240` · [字段定义](../../DATASET.md)*
