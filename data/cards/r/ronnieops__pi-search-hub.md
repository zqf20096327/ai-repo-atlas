# ronnieops/pi-search-hub

⭐ 50 · TypeScript · 推送 2026-07-24 · [GitHub](https://github.com/ronnieops/pi-search-hub) · 个人维护

**为 pi 编码 agent 提供统一 web 搜索与网页读取的扩展**

面向 pi 编码 agent 的扩展包，把 19 个搜索后端聚合成单个 web_search 工具、5 个读取后端聚合成单个 web_read 工具：支持自动回退（auto-fallback）、并行 combine 模式（RRF 倒数排名融合与 URL 去重）、targeted 定向组合，以及 env 变量/shell 命令/字面量三态凭据解析。Firecrawl 后端可无 key 使用（每月 1,000 免费额度）。通过 `pi install npm:pi-search-hub` 安装，用 search.json 全局或按项目配置，DuckDuckGo 后端需另装 ddgs Python 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 个搜索后端聚合成单一 web_search 工具，自动回退
- RRF 融合的 combine 并行查询模式与 targeted 定向组合
- 5 个 web_read 读取后端（Jina/Sofya/Firecrawl/Exa/Exa MCP）自动回退链
- apiKey 支持 env 变量名、! 前缀 shell 命令与字面量三种格式

## 适用场景

- 给 pi 编码 agent 补充联网搜索与网页内容提取能力
- 综合研究时并行查询多个搜索后端并融合排序
- 免 API key 快速起步（Firecrawl keyless / DuckDuckGo）

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: Unified web search + content extraction extension for pi with **19 backend providers** (all working). One `web_searc
> L30: Or use the tools directly — the agent picks the best configured backend automatically:

## 星数曲线

```mermaid
xychart-beta
    title "ronnieops/pi-search-hub 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-30 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `a48cf7a26bc4` · [字段定义](../../DATASET.md)*
