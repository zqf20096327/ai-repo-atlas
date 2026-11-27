# jundot/omlx

⭐ 24,009 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/jundot/omlx) · [官网](https://omlx.ai) · 个人维护 · 中文 README

**macOS 菜单栏管理的本地 LLM 推理服务器（Apple Silicon）**

面向 Apple Silicon Mac 的本地 LLM 推理服务器：以 continuous batching 与分层 KV 缓存（内存热层 + SSD 冷层，前缀复用、重启后可恢复）为核心机制，支持文本 LLM、VLM、OCR、embedding 与 reranker 的同服务器多模型服务，提供 LRU 逐出、模型常驻、按模型 TTL 与进程内存上限管理。通过 macOS 菜单栏应用、CLI 或 Homebrew 服务运行，内置 Web 管理面板（监控/聊天/基准测试），对外暴露 OpenAI 兼容 API；要求 macOS 15.0+、Python 3.11–3.13。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.6 天,年发版 100,307 位贡献者
- 涨星:近 1 天 **+30**(自 20261016 起算)
- 安装:pypi 包 `mcp` 月下载 235,193,557
- 平台:MACOS / WEB · 协议:OPENAI-API / MCP

## 能力要点

- 分层 KV 缓存：内存热层 + SSD 冷层，前缀缓存跨请求与重启复用
- 同一服务器混布 LLM/VLM/embedding/reranker，支持 LRU 逐出与模型常驻
- OpenAI 兼容 API（localhost:8000/v1），内置 Web 管理面板与聊天界面
- 多 Mac 分布式推理实验特性（MLX pipeline + RDMA/JACCL）

## 适用场景

- 在 Mac 上本地运行并管理多个 LLM 供开发工具调用
- 为 Claude Code 等编码工具提供本地模型后端
- 长上下文编码场景下通过 SSD 缓存减少重复计算
- 从菜单栏/管理面板一键下载 HuggingFace 模型并做基准测试

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L4:  LLM inference, optimized for your Mac Continuous batching and tiered KV caching, managed directly from your menu ba
> L94: The server discovers LLMs, VLMs, embedding models, and rerankers from subdirectories automatically. Any OpenAI-comp
> L115: Supports text LLMs, vision-language models (VLM), OCR models, embeddings, and rerankers on Apple Silicon.

## 星数曲线

```mermaid
xychart-beta
    title "jundot/omlx 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 22933 --> 24106
    line [23030, 23043, 23073, 23105, 23130, 23158, 23203, 23227, 23265, 23030, 23461, 23511, 23536, 23577, 23607, 23636, 23654, 23671, 23699, 23734, 23757, 23767, 23807, 23840, 23884, 23953, 24009]
```

2026-10-25 23,030 → 2026-11-27 24,009（+979）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4dad5c758099` · [字段定义](../../DATASET.md)*
