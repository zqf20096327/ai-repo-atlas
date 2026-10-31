# memseekai/membukkit

⭐ 22 · Python · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/memseekai/membukkit) · 组织维护

**为 LLM 应用提供带收据与时效查询的长期记忆库**

Python 库 + CLI + 本地 GUI + HTTP + MCP 的长期记忆层：写入时用 LLM 把会话/文档蒸馏为带日期的原子事实，并保留逐字原文双通道；新事实取代旧事实但不删除，支持 as-of 时间点查询。每个回答附带收据：使用的证据行、来源、token 与成本、扫描比例。检索用扁平嵌入索引 + 可选 KMeans 主题桶与默认关闭的 BM25 词法通道。蒸馏写入需 LLM 调用（有缓存），完全本地可用（配 Ollama）。Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- dated atomic facts + verbatim 双通道，支持 as-of 时间点查询与 supersession
- 每个回答输出收据（证据行、来源、token/成本、扫描比例）
- 同一存储暴露 Python/CLI/GUI/HTTP/MCP 五种接口，支持完全本地运行（Ollama）
- 冻结配方一条命令复现基准（membukkit bench --repro）

## 适用场景

- 给 LLM 应用/agent 挂上可追溯的长期记忆
- 导入 WhatsApp/ChatGPT/Claude 导出等个人数据建记忆库
- 通过 MCP 让 Cursor/Claude Desktop 复用同一记忆库
- 按时间点回查『当时为真』的事实

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: **MemBukkit is long-term memory for LLM apps that shows its work.** It turns conversations and documents into dated
> L146: A thin stdio server gives Cursor / Claude Desktop three tools over the same stores: `memory_add`, `memory_search`,

## 星数曲线

```mermaid
xychart-beta
    title "memseekai/membukkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `af092754837f` · [字段定义](../../DATASET.md)*
