# jundot/omlx

⭐ 23,840 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/jundot/omlx) · [官网](https://omlx.ai) · 个人维护 · 中文 README

**macOS 菜单栏管理的 Apple Silicon LLM 推理服务器**

运行于 Apple Silicon 的本地 LLM 推理服务器，提供 OpenAI 兼容 API（/v1），支持文本 LLM、VLM、OCR、embedding 与 reranker 模型。关键机制：连续批处理、热内存+冷 SSD 两级 KV 缓存（safetensors 落盘、跨请求与重启复用）、LRU/固定/TTL 的多模型管理、进程内存上限防 OOM。通过 macOS 菜单栏 App（dmg）、Homebrew 或源码安装，自带 Web 管理面板、聊天 UI 与 HuggingFace 模型下载器。要求 macOS 15.0+、Python 3.11–3.13；原生自定义内核需完整 Xcode，缺失时部分模型族回退到较慢路径。

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

- 热内存+SSD 两级 KV 缓存，前缀命中可跨请求与重启复用
- OpenAI 兼容 API，同时服务 LLM/VLM/embedding/reranker
- LRU 驱逐、模型固定、按模型 TTL 与进程内存上限
- 一键接入 Codex/Copilot CLI 等客户端并下发模型目录

## 适用场景

- 在 Mac 上为编码工具提供本地 OpenAI 兼容推理端点
- 菜单栏管理多个本地模型的加载/卸载与显存占用
- 用多台 Mac 流水线拆分单个大模型做分布式推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L4:  LLM inference, optimized for your Mac Continuous batching and tiered KV caching, managed directly from your menu ba
> L94: The server discovers LLMs, VLMs, embedding models, and rerankers from subdirectories automatically. Any OpenAI-comp
> L115: Supports text LLMs, vision-language models (VLM), OCR models, embeddings, and rerankers on Apple Silicon.

## 星数曲线

```mermaid
xychart-beta
    title "jundot/omlx 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 22846 --> 23930
    line [22936, 22975, 22991, 23013, 23030, 23043, 23073, 23105, 23130, 23158, 23203, 23227, 23265, 23030, 23461, 23511, 23536, 23577, 23607, 23636, 23654, 23671, 23699, 23734, 23757, 23767, 23807, 23840]
```

2026-10-21 22,936 → 2026-11-23 23,840（+904）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `a9f20f5efd0f` · [字段定义](../../DATASET.md)*
