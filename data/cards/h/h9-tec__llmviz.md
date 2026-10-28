# h9-tec/llmviz

⭐ 27 · Python · Apache-2.0 · 推送 2026-08-16 · [GitHub](https://github.com/h9-tec/llmviz) · 个人维护

**从 config.json 生成出版级 LLM 架构图的命令行工具**

面向开发者的 LLM 架构可视化工具：读取 Hugging Face id、本地 config.json、GGUF 文件（仅读头部元数据）或 Ollama 已装模型，按 Sebastian Raschka LLM Architecture Gallery 的视觉语言渲染解码器塔式架构图（SVG/PNG），参数量、KV cache 与 VRAM 占用由逐层数学计算得出并与公开数字对齐。附带 diff/lineage 对比、poster/gallery 生成、GPU 显存适配判定（fit）、LLM 撰写说明（explain，经 LiteLLM 调用）以及 MCP server 供 agent 调用。需 Python 3.11+，通过 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅凭 config.json/GGUF 头部生成架构图，无需权重与 GPU
- 参数量与 VRAM 由逐层计算得出，测试对齐公开数字（误差 0.5–3%）
- diff/lineage/poster/gallery 等多种输出形式
- 提供 MCP server 与 Python API（Pydantic ArchSpec）

## 适用场景

- 为新发布的模型快速生成可发表的架构示意图
- 对比两个模型架构差异或模型家族演进
- 判定某模型量化后在本地 GPU 上能否运行
- 为 agent 提供经计算而非记忆的架构事实工具

## 场景标签

 · 领域:LLM 开发工具/可视化

## 证据(README 行号)

> L3: **Publication-quality LLM architecture figures from `config.json` alone — no weights, no GPU, no `transformers` inst
> L51: |`fit <model>`|Quantization-aware memory needs (weights + KV cache) and which GPUs fit — detects your local GPU via
> L53: |`mcp`|MCP server (stdio): `inspect_architecture`, `memory_to_run`, `render_architecture_figure`, `diff_architectur

## 星数曲线

```mermaid
xychart-beta
    title "h9-tec/llmviz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8bac4f9fb64c` · [字段定义](../../DATASET.md)*
