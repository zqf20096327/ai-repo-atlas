# pollinations/search.elixpo

⭐ 24 · Python · CC0-1.0 · 推送 2026-10-27 · [GitHub](https://github.com/pollinations/search.elixpo) · [官网](https://search.elixpo.com) · 组织维护

**开源 AI 网页搜索与深度研究引擎，OpenAI 兼容 API**

OreoLook（lixSearch）是可自托管的 agentic 搜索引擎：多搜索代理并行检索网页、YouTube 与图片，提取信息后由模型合成带来源引用的回答。提供 OpenAI 兼容的 /v1/chat/completions API（SSE 流式与非流式）、无状态 Streamable HTTP MCP 工具（研究/深度研究/PDF 导出）。机制上含 Redis 语义缓存（余弦相似度 0.90）、双层多轮记忆（Redis 热窗口 + Huffman 压缩磁盘归档）、深度搜索模式（子查询分解与并行流水线）。通过 Pollinations.ai 使用或自行部署（Docker Compose），需联网检索，支持 CPU 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多搜索代理并行检索网页/YouTube/图片并合成带来源的回答
- OpenAI 兼容 /v1/chat/completions API，SSE 流式输出
- Redis 语义缓存 + 双层多轮记忆（热窗口与磁盘归档）
- 无状态 MCP 端点提供研究、深度研究与 PDF 导出工具

## 适用场景

- 给自己的聊天机器人或助手接入带来源的实时网页搜索后端
- 自托管部署一个可定制的研究/搜索 API 服务
- 做市场调研或文献调研，拿到带引用的综合回答

## 场景标签

`RAG` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L3: **A curious, open-source AI search scout with real-time web research, RAG, and an OpenAI-compatible API.**
> L105: OreoLook exposes an **OpenAI-compatible** API. Keep using `lixsearch` as the model ID for direct and Pollinations-
> L150: |`/v1/chat/completions`|POST|OpenAI-compatible chat completions (stream + non-stream)|

## 星数曲线

```mermaid
xychart-beta
    title "pollinations/search.elixpo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-29 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3702f059694f` · [字段定义](../../DATASET.md)*
