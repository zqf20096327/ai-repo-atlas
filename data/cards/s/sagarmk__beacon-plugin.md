# sagarmk/beacon-plugin

⭐ 43 · JavaScript · MIT · 推送 2026-09-13 · [GitHub](https://github.com/sagarmk/beacon-plugin) · [官网](https://github.com/sagarmk/beacon-plugin) · 个人维护

**Claude Code 语义代码搜索插件：混合向量+BM25+符号图**

面向 Claude Code 用户的代码搜索插件，通过 MCP 服务器向 Claude 提供 find_symbol、find_references、outline、search_code 等工具，检索机制为语义向量、BM25 关键词、标识符加权与符号引用图（Personalized PageRank）的混合。默认经 Ollama 本地运行开源嵌入模型（qwen3-embedding:0.6b），也可切换 OpenAI、Voyage AI、LiteLLM 代理或任意 OpenAI 兼容端点。借助 Claude Code hooks 在会话启动时自动安装依赖并建索引，编辑时增量重嵌入；嵌入服务不可用时降级为 BM25 关键词检索。基准数字为作者在单一代码库上的自测结果，README 自述样本小、数值有噪声。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 工具集：find_symbol/find_references/outline/search_code/index_status
- 混合检索：语义向量 + BM25 + 标识符加权 + 符号引用图（PageRank）
- 默认 Ollama 本地嵌入，无 API key；支持 OpenAI/Voyage/LiteLLM/自定义 OpenAI 兼容端点
- hooks 自动索引与增量重嵌入，嵌入服务不可用时降级为 BM25 检索

## 适用场景

- 让 Claude Code 按语义描述定位代码而非仅字符串匹配
- 查询符号定义位置与全部调用点以评估修改影响
- 在本地免 API key 地为代码库建语义索引

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L102: Beacon ships an MCP server, so Claude picks the right tool for the question
> L155: Beacon runs on **open-source models by default** — no API keys, no cloud costs, fully local via Ollama.
> L275: Beacon uses Claude Code hooks to stay in sync with your codebase:

## 星数曲线

```mermaid
xychart-beta
    title "sagarmk/beacon-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-30 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `07fb54892279` · [字段定义](../../DATASET.md)*
