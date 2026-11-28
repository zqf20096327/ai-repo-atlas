# dedene/Inkling-2-Mini-DGX-Spark

⭐ 8 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/dedene/Inkling-2-Mini-DGX-Spark) · 个人维护

**在单台 DGX Spark 上用 vLLM 部署 Inkling 2 Mini 的 Docker Compose 配方**

面向拥有 NVIDIA DGX Spark 的用户提供一键式本地部署：通过 Docker Compose 下载锁定的第一方检查点（NVFP4 专家，20.2 GB），用 vLLM 启动 OpenAI 兼容 API，支持文本、图像、推理与工具调用。配置覆盖推理努力、KV 缓存、上下文长度（本机上限 262,144 tokens）与投机解码；附带功能自检脚本与作者自己的 Agent 基准测试结果（AgentDojo、BFCL、注入攻击等）。依赖 GB10 硬件、CUDA 13、驱动 580 与 NVIDIA Container Toolkit。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- docker compose 一条命令完成下载、加载与健康检查
- OpenAI 兼容 API，支持图像、reasoning_effort 推理控制与工具调用
- DSpark 投机解码与前缀缓存，全服务器内存约 56 GB
- 附带 inspect_evals 基准与提示注入攻击结果数据

## 适用场景

- 在 DGX Spark 上本地自托管 26B MoE 模型并提供 API
- 为本地 LLM 测试长上下文召回与 Agent 工具调用
- 在局域网内为多个客户端提供共享推理端点

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: # Inkling 2 Mini on a single DGX Spark (vLLM, Docker Compose)
> L3: Serve Inkling 2 Mini from Thinking Machines on one NVIDIA DGX Spark with vLLM. One command downloads the pinned firs
> L7: **Hardware:** DGX Spark (GB10, sm_121, aarch64), driver 580, CUDA 13, Docker with the NVIDIA Container Toolkit and C

## 星数曲线

```mermaid
xychart-beta
    title "dedene/Inkling-2-Mini-DGX-Spark 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 6 --> 9
    line [7, 8]
```

2026-11-26 7 → 2026-11-28 8（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b7126866533c` · [字段定义](../../DATASET.md)*
