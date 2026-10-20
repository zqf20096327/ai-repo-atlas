# jundot/omlx

⭐ 22,907 · Python · Apache-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/jundot/omlx) · [官网](https://omlx.ai) · 个人维护

**macOS 菜单栏管理的 Apple Silicon 本地 LLM 推理服务器**

面向 Apple Silicon 的本地 LLM 推理服务器，通过 macOS 菜单栏应用或 CLI 管理服务；核心机制包括块式 KV 缓存的内存热层与 SSD 冷层两级缓存（跨请求、可跨重启复用）、基于 mlx-lm BatchGenerator 的连续批处理、多模型共存时的 LRU 逐出/固定/TTL 管理。提供 OpenAI 与 Anthropic 兼容 API、管理仪表盘 Web UI、HuggingFace 模型下载与一键基准测试。要求 macOS 15+、Python 3.11–3.13、Apple Silicon 芯片。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.6 天,年发版 100,307 位贡献者
- 涨星:近 1 天 **+30**(自 20261016 起算)
- 安装:pypi 包 `mcp` 月下载 235,193,557
- 平台:MACOS / WEB · 协议:OPENAI-API / MCP

## 能力要点

- KV 缓存热(RAM)+冷(SSD)两级分层，前缀匹配可跨请求与重启复用
- 同一服务器加载 LLM、VLM、OCR、embedding、reranker，支持 LRU 逐出/固定/TTL
- OpenAI 与 Anthropic API 兼容端点，内置管理仪表盘与聊天 UI
- 实验性多 Mac 流水线推理（Ring/Thunderbolt RDMA）

## 适用场景

- 在 Mac 上通过菜单栏启停并监控本地 LLM 服务
- 为 Claude Code、OpenCode 等工具提供本地 OpenAI 兼容后端
- 用 SSD 缓存复用前缀，降低长上下文编码工具场景的重复计算
- 在多台内存不等的 Mac 间切分一个大模型做分布式推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L4:  LLM inference, optimized for your Mac Continuous batching and tiered KV caching, managed directly from your menu ba
> L56: Requires macOS 15.0+ (Sequoia), Python 3.11–3.13, and Apple Silicon (M1/M2/M3/M4/M5).
> L114: Supports text LLMs, vision-language models (VLM), OCR models, embeddings, and rerankers on Apple Silicon.

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `c37b5072e34f` · [字段定义](../../DATASET.md)*
