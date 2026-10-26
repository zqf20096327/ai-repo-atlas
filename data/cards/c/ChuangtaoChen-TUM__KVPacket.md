# ChuangtaoChen-TUM/KVPacket

⭐ 39 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/ChuangtaoChen-TUM/KVPacket) · [官网](https://arxiv.org/abs/2604.13226) · 组织维护

**面向 LLM 推理的无重算、上下文无关 KV 缓存库**

KV Packet 是论文《KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs》的可复用 Python 库实现：通过可训练的 soft-token header/trailer 适配器，离线独立预计算各文档的 KV 缓存，服务时仅做 RoPE 位置重对齐即可拼接缓存，免去文档 token 重算。面向构建 LLM 推理服务的开发者，提供 Hugging Face 后端、OpenAI Responses 兼容 HTTP/SSE 端点、KVPress 可选压缩、MCP agent 支持，以及仅训练 header/trailer 张量的训练器。需 Python 3.12+ 与 PyTorch；训练时冻结基础模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 离线独立预计算文档 KV 缓存，服务时 RoPE 重对齐直接拼接，无需重算
- 可训练 header/trailer soft-token 适配器，仅优化选定张量、冻结基础模型
- 可选 OpenAI Responses 兼容 HTTP/SSE 端点与 KVPress 缓存压缩
- MCP 支持的 agentic 流（Codex 渐进披露式技能分包示例）

## 适用场景

- 多文档/技能密集的 agent 推理场景中复用预计算 KV 缓存
- 为现有推理服务器集成 packet 感知的前向路径
- 训练并评估 header/trailer 适配器

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L27: Recomputation-free, context-independent KV caching for LLMs via trainable
> L32: This repository is the reusable library implementation of
> L110: Inference sessions require an explicit compute backend. The Hugging Face backend owns

## 星数曲线

```mermaid
xychart-beta
    title "ChuangtaoChen-TUM/KVPacket 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `deda0a1f83bf` · [字段定义](../../DATASET.md)*
