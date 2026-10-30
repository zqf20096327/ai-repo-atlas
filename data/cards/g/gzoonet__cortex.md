# gzoonet/cortex

⭐ 24 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/gzoonet/cortex) · [官网](https://github.com/gzoonet/cortex) · 个人维护

**给开发者的本地优先知识图谱工具，跨项目查询决策与模式**

面向开发者的本地优先知识图谱工具：监控项目文件（md/ts/js/py/json/yaml）变更，经 tree-sitter/remark 解析分块后由 LLM 抽取实体（决策、模式、组件、依赖等）并推断跨项目关系，自动检测矛盾，支持自然语言查询与带来源引用的回答合成。数据存储于本地 SQLite + LanceDB，受限项目不外发。LLM 提供商无关：支持 Anthropic/Gemini/DeepSeek/Groq/OpenAI 兼容 API/Ollama，并提供 cloud-first/hybrid/local-first/local-only 四种路由模式与月度预算上限。以 npm CLI 提供，含 Web 仪表盘与面向 Claude Code 的 MCP 服务器（12 个工具）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件变更驱动的实体/关系抽取管线，自动检测决策矛盾
- 自然语言查询（带来源引用）与可选向量语义搜索（默认关闭）
- 多 LLM 提供商与四种路由模式（含完全本地 Ollama），月度预算上限
- Web 仪表盘（D3 知识图谱、实时事件流、矛盾解决器）与 Claude Code MCP 集成

## 适用场景

- 跨多个项目检索自己曾做过的架构决策与技术选型
- 自动累积团队/个人代码库中的决策、模式与组件知识并发现冲突
- 在 Claude Code 中通过 MCP 直接查询知识图谱

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L5: **Local-first knowledge graph for developers.** Watches your project files,
> L6: extracts entities and relationships using LLMs, and lets you query across
> L29: - **Queries** in natural language with source citations

## 星数曲线

```mermaid
xychart-beta
    title "gzoonet/cortex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-30 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2d0d7634ef59` · [字段定义](../../DATASET.md)*
