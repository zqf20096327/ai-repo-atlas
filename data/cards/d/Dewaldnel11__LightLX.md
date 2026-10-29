# Dewaldnel11/LightLX

⭐ 18 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/Dewaldnel11/LightLX) · 个人维护

**Apple Silicon 上从磁盘流式运行超出内存的模型的 MLX 运行时**

基于 MLX/mlx-lm 构建的本地模型运行时：对放得进内存的模型全量驻留 GPU 全速运行；对放不进内存的模型按层流式读取原始 BF16 safetensors 权重，MoE 模型仅读取每 token 路由到的 top-k 专家，密集与 MoE 架构均支持，并复用 mlx-lm 前向使输出与原生逐位一致。内置针对 753B GLM-5.2 的专用流式引擎。流式模式速度受磁盘带宽限制，约每 token 数十秒。另带编码 agent（文件/Shell/MCP/子代理/记忆），可连接 Ollama、LM Studio、vLLM、llama.cpp 等 OpenAI 兼容服务。

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

- 驻留/流式两种模式按模型大小自动选择
- MoE 模型仅读取每 token 的 top-k 活跃专家，减少 I/O
- 复用 mlx-lm 前向，流式输出与原生逐位一致
- 内置编码 agent：文件、Shell、MCP、子代理、跨项目记忆

## 适用场景

- 在内存不足的 Mac 上运行全精度超大模型（如 753B GLM-5.2）
- 本地 MLX 模型聊天与流式推理
- 连接本地 Ollama/LM Studio 运行编码 agent 工作流

## 场景标签

`推理引擎` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L17: **Run models too big for your RAM on Apple Silicon — any Hugging Face model that
> L39: pip install -e .          # once; then `lightlx` works from any directory
> L252: How it works: LightLX builds the model via mlx-lm (MLX is lazy, so instantiating a

## 星数曲线

```mermaid
xychart-beta
    title "Dewaldnel11/LightLX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `455e5131cc24` · [字段定义](../../DATASET.md)*
