# opentrace/opentrace

⭐ 108 · JavaScript · Apache-2.0 · 推送 2026-08-12 · [GitHub](https://github.com/opentrace/opentrace) · [官网](https://opentrace.ai) · 组织维护

**把代码库索引自建知识图谱并通过 MCP 暴露给 AI 工具的平台**

对任意仓库建立代码知识图谱：用 tree-sitter WASM 语法解析（12 种语言），抽取类、函数、导入与调用关系，存入嵌入式图数据库 LadybugDB，并通过 MCP 工具与插件暴露给 AI 客户端。面向使用 Claude Code、OpenCode、Gemini CLI 等 AI 编码工具的开发者，为 LLM 提供代码库上下文。提供 uvx/PyPI CLI、Claude 与 OpenCode 插件、浏览器版与本地 UI；knowledge vaults 功能可调用 LLM（Anthropic/Gemini/OpenAI/本地）编译 markdown wiki。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tree-sitter 解析 12 种语言，抽取符号、调用与依赖关系构建知识图谱
- 通过 MCP 及 Claude Code/OpenCode 插件向 AI 客户端暴露图查询工具
- 浏览器版（app.opentrace.ai）无需安装即可使用
- knowledge vaults 可用 LLM 编译 markdown wiki，支持多家 LLM 供应商及本地模型

## 适用场景

- 为 Claude Code/OpenCode 等 AI 编码工具提供代码库真实上下文
- 分析代码依赖与变更影响范围（blast radius）
- 可视化浏览服务架构与模块关系

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L8: A knowledge graph that maps your codebase structure, service architecture, and system relationships — then exposes i
> L22: 5. **Expose** the graph via MCP tools to any compatible AI client

## 星数曲线

```mermaid
xychart-beta
    title "opentrace/opentrace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-23 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `11552f929494` · [字段定义](../../DATASET.md)*
