# daidaiJ/websearch-mcpserver

⭐ 27 · Go · MIT · 推送 2026-10-25 · [GitHub](https://github.com/daidaiJ/websearch-mcpserver) · 个人维护 · 中文 README

**零 API Key 的 Go 版 MCP 搜索服务，供 LLM/Agent 调用**

用 Go 编写的单二进制 MCP 搜索服务：聚合百度/Bing/DuckDuckGo 等通用引擎、Parallel/AnySearch/Exa/Firecrawl 四个零 Key 托管 MCP 上游及 9 个学术引擎，本地完成 RRF/MMR 融合评分、SQLite 缓存；提供网页抓取（SSRF 防护）、MinerU PDF 解析、可选 LLM 摘要、本地文件检索与只读 dashboard。面向接入 Claude Code、Qwen Code、Cursor 等 MCP 客户端的开发者，也可作为 Go 模块嵌入。限制：默认仅监听 127.0.0.1，部分上游需代理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零 API Key 可运行，mcphub 托管级联失败冷却自动切换
- 9 通用引擎 + 4 托管 MCP 上游 + 9 学术引擎并行，本地 RRF/MMR 融合评分
- cleanfetch 网页抓取带 SSRF/DNS rebinding 防护，PDF 可回退 MinerU OCR
- 单二进制、无 CGO，可嵌入 Go 模块，含只读控制中心与 Prometheus metrics

## 适用场景

- 给 Claude Code / Qwen Code / Cursor 等 MCP 客户端接入免费搜索
- 国内无 Key 环境下让 Agent 检索网页与学术论文
- 抓取网页与解析 PDF 正文供 LLM 分段消费

## 场景标签

`网页抓取` `RAG` `文档解析` · 领域:效率与自动化

## 证据(README 行号)

> L15: 用 Go 编写的 MCP 搜索服务。内置百度网页、Bing、DuckDuckGo 等通用引擎、Parallel / AnySearch / Exa / Firecrawl 四个零 Key 托管 MCP 上游和 9 个学术引擎，搜索
> L27: |**接入**|Claude Code / Qwen Code / Cursor / HTTP API / 嵌入 Go 模块|

## 星数曲线

```mermaid
xychart-beta
    title "daidaiJ/websearch-mcpserver 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-10-30", "2026-10-31"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-26 26 → 2026-10-31 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fdf4b6ca375d` · [字段定义](../../DATASET.md)*
