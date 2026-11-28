# accso/ai-context-opencode-plugin

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-10 · [GitHub](https://github.com/accso/ai-context-opencode-plugin) · 组织维护

**OpenCode 本地代码索引插件：为 agent 提供语义搜索与影响分析**

以 OpenCode 原生插件形式运行，为 agent 构建本地、无需 Docker 的代码索引，提供语义搜索、符号查找、仓库结构、调用/导入影响分析和文档检索共六类工具。索引流程用本地 OpenAI 兼容 LLM（LM Studio、Ollama、oMLX）生成文件摘要块，不可达时回退到确定性摘要；检索结合向量、FTS5 BM25 与小型交叉编码器重排。支持 OpenCode 1.x 与 2.x，可在 TUI 和 ACP（JetBrains AI Assistant）下运行。索引与搜索在本地执行，但检索结果会随对话发送到所配置的模型提供方。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六类 agent 工具：semantic_search、find_symbol、analyze_impact、repo_structure、search_docs、index_status
- 本地嵌入 + FTS5 BM25 混合检索与交叉编码器重排
- 通过系统提示规则、工具描述后缀与结果附注引导 agent 减少使用 grep/glob
- 单条命令覆盖 OpenCode 1.x 与 2.x 两种插件接口

## 适用场景

- 让 coding agent 用语义搜索理解大型代码库而非反复 grep
- 修改符号前查看调用方/被调方影响范围
- 检索仓库内的 Markdown 文档、ADR 与 RFC

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: A native OpenCode plugin that gives the agent a local,
> L4: Docker-free code index (indexing and search run locally; see the data boundary below): semantic search, repository s

## 星数曲线

```mermaid
xychart-beta
    title "accso/ai-context-opencode-plugin 星数(近 2 点)"
    x-axis ["2026-11-11", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-11 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `9ff7eeb6bcd3` · [字段定义](../../DATASET.md)*
