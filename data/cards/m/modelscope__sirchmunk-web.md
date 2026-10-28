# modelscope/sirchmunk-web

⭐ 20 · HTML · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/modelscope/sirchmunk-web) · 组织维护

**Sirchmunk 文档网站源码：无嵌入的 agentic 搜索引擎官方站点**

本仓库是 Sirchmunk 官方文档网站的源码（部署于 modelscope.github.io/sirchmunk-web），而非搜索引擎本体（本体在 modelscope/sirchmunk）。Sirchmunk 是开源、免嵌入的 agentic 搜索引擎：读取原始文件即时检索，无需向量库、预索引或 ETL；知识簇随检索自我演化；用蒙特卡洛证据采样从大文档抽取片段；标准检索不足时由 ReAct Agent 迭代探索；提供 MCP、REST API、WebSocket、CLI 与 Web UI。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免嵌入检索：无需向量库、预索引、ETL，放入文件即可搜索
- 知识簇随每次检索自我演化
- 蒙特卡洛证据采样 + ReAct Agent 回退策略
- MCP / REST API / WebSocket / CLI / Web UI 多接入方式

## 适用场景

- 跳过 ETL 与向量化流程直接对原始文件做问答检索
- 通过 MCP 或 REST API 将检索能力接入自己的应用
- 长期使用中让知识库随检索积累而演化

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: Sirchmunk is an open-source, embedding-free, agentic search engine that transforms raw data into self-evolving intel
> L13: - **Multi-Surface Integration** — MCP, REST API, WebSocket, CLI, and Web UI — all built in.

## 星数曲线

```mermaid
xychart-beta
    title "modelscope/sirchmunk-web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `05a2f6562b4d` · [字段定义](../../DATASET.md)*
