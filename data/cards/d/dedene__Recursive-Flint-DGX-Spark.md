# dedene/Recursive-Flint-DGX-Spark

⭐ 4 · Python · MIT · 推送 2026-11-06 · [GitHub](https://github.com/dedene/Recursive-Flint-DGX-Spark) · 个人维护

**在单台 DGX Spark 上用 llama.cpp 部署 Recursive Flint 40B 模型的部署栈**

一个 Docker Compose 部署模板：在 NVIDIA DGX Spark (GB10) 上以官方 llama.cpp 镜像伺服 Recursive Flint（39.8B 参数 MoE，每 token 约 2.5B 激活，262K 上下文，仅文本）的 NVFP4 GGUF 权重。一条命令完成固定版本的模型下载（含 sha256 校验）、健康检查与服务启动，暴露 OpenAI 兼容 API，支持推理输出与工具调用。提供 .env 配置项、速度调优表和 Inspect 评测套件上的 agent 基准结果。模型权重不在本仓库内；仅面向 DGX Spark 硬件。

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

- 一条 docker compose 命令完成下载（22.9 GB）、校验与健康检查启动
- OpenAI 兼容 API，返回 message.reasoning_content 并支持工具调用
- 提供 CONTEXT/PARALLEL/采样参数等 .env 配置与功能检查脚本 check.py
- 附 BFCL/AgentDojo/IFEval 等 agent 基准与速度调优数据

## 适用场景

- 在 DGX Spark 上本地伺服 Flint 并接入 OpenAI 兼容客户端
- 为本地编码 agent 提供带工具调用的推理端点
- 在 DGX Spark 上对比多个本地模型做选型评估

## 场景标签

`推理引擎` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Serve Recursive Flint on one NVIDIA DGX Spark with stock llama.cpp, from the official NVFP4 GGUF. One command downlo
> L35: - **`compose.yaml`:** the `download` service fetches the pinned GGUF and checks it, then `flint` serves it. A healt

## 星数曲线

```mermaid
xychart-beta
    title "dedene/Recursive-Flint-DGX-Spark 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-11-28"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-10-30 4 → 2026-11-28 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `c4a76182d56f` · [字段定义](../../DATASET.md)*
