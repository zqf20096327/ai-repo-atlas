# helasaoudi/llm-inspector

⭐ 76 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/helasaoudi/llm-inspector) · 个人维护

**LLM 推理进程的 GPU 显存分解与量化收益测算工具**

Python 编写的 htop 风格 CLI 工具，检视运行中的推理进程，展示 GPU 显存按 Weights / KV Cache / Workspace / Other 的分配，以及进程、硬件、模型、运行时配置等实测信息（不可用时标注原因与来源）。基于实测数据做量化策略（FP8/AWQ）显存节省的投影分析，不改动模型。深度指标需通过可选的嵌入式 attach() 在推理进程同环境下采集。支持 NVIDIA GPU 机器，也覆盖多卡 vLLM 张量并行与 CPU 场景（如 macOS 上的 Ollama）。

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

- GPU 显存按 Weights/KV Cache/Workspace/Other 分解到进程级
- FP8/AWQ 等量化策略的显存节省投影，不改动模型
- 每个字段可显示来源（provenance）与不可用原因
- 支持 vLLM 多卡张量并行与多核 CPU 场景的单一报告检视

## 适用场景

- 排查推理进程显存占用构成与 KV Cache 瓶颈
- 量化前预估不同量化策略的显存节省
- 检视 vLLM 多卡或 Ollama CPU 推理的工作负载配置

## 场景标签

`模型量化` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L13: LLM Inspector inspects live inference processes and shows exactly how GPU memory is being used, what model is runni
> L15: Unlike traditional monitoring tools, it doesn't stop at inspection. It also analyzes the running workload and proje
> L63: That bridge—**system observability + model internals**, with an `htop`-style CLI—is the innovation. Deep metrics co

## 星数曲线

```mermaid
xychart-beta
    title "helasaoudi/llm-inspector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-29 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a92710a760cc` · [字段定义](../../DATASET.md)*
