# sodiumsun/snackcache

⭐ 44 · Python · MIT · 推送 2026-01-08 · [GitHub](https://github.com/sodiumsun/snackcache) · 个人维护

**OpenAI/Anthropic API 的语义缓存代理，降低重复请求成本**

本地运行的缓存代理服务器：应用将 SDK 的 base_url 指向 SnackCache 即可，代理拦截请求并做两层缓存——精确哈希匹配与基于嵌入相似度的语义匹配，命中时直接返回缓存响应，未命中则转发到 OpenAI/Anthropic API 并缓存新响应。语义匹配使用 all-MiniLM-L6-v2 本地嵌入模型（约 23M 参数）与 FAISS 向量检索，不产生额外 API 调用；相似度阈值可配置（默认 0.85）。通过 pip 安装，首次运行下载约 100MB 嵌入模型。面向本地开发调试、CI/CD 测试流水线及查询模式重复的应用。持久化存储与多用户共享等在 Roadmap 中尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两层缓存：精确哈希匹配 + 嵌入语义匹配
- all-MiniLM-L6-v2 本地嵌入 + FAISS 向量检索，无额外 API 调用
- 仅需修改 SDK base_url，兼容现有 OpenAI/Anthropic SDK
- 相似度阈值可配置（0.75/0.85/0.95），提供 snackcache stats 统计

## 适用场景

- 本地调试时反复发送相同提示词，只付费一次
- CI/CD 测试流水线中跨运行缓存 LLM 调用
- 客服机器人、FAQ 系统等查询模式重复的应用降低 API 成本

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L14: SnackCache is a caching layer for OpenAI and Anthropic APIs. It **reduces your LLM API costs** by caching responses
> L63: Your App -> SnackCache -> OpenAI/Anthropic
> L74: Uses `all-MiniLM-L6-v2` embeddings (~23M params, runs locally) and FAISS for vector search. No additional API calls

## 星数曲线

```mermaid
xychart-beta
    title "sodiumsun/snackcache 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6ecce8a18826` · [字段定义](../../DATASET.md)*
