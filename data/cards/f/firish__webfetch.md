# firish/webfetch

⭐ 60 · Python · MIT · 推送 2026-07-23 · [GitHub](https://github.com/firish/webfetch) · 个人维护

**本地运行的 LLM 联网搜索工具：搜索→抓取→压缩流水线**

以 MCP 服务器或 Python 库形式提供的 web_search 工具，替代托管搜索服务：多引擎 RRF 融合（DuckDuckGo 免 key 可用，可加 Brave/Serper/Tavily）、本地页面抓取与抽取、BM25+bi-encoder+cross-encoder 级联排序、句级压缩；配双层 sqlite 语义缓存（NLI 校验、按查询波动性分级 TTL），并提供 save_finding、fetch_url、费用报告等工具。限制：语义能力需 [all] 安装（torch），缓存假设单进程独占文件；README 报告 SimpleQA 50 题上的 token/成本数据并附带可复现评测脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多引擎 RRF 融合搜索 + 本地抓取 + 句级压缩的 web_search 工具
- 双层缓存：精确匹配 + NLI 校验的语义缓存，TTL 按查询类型分级
- DuckDuckGo 无 key 零成本起步，其余引擎 key 可选
- 评测 harness 与数据集随仓库提供，表格可一条命令复现

## 适用场景

- 给 Claude Code / 自建 agent 循环接入自托管的联网搜索工具
- 降低 agent 联网搜索的 token 消耗与每次查询成本
- 让重复/改述查询命中缓存，避免重复付费

## 场景标签

`RAG` `网页抓取` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: compression - exposed as a `web_search` tool your model calls like any
> L114: claude mcp add webfetch -- uvx --from webfetch-llm@latest webfetch-mcp

## 星数曲线

```mermaid
xychart-beta
    title "firish/webfetch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-25 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `47f74bda0c9c` · [字段定义](../../DATASET.md)*
