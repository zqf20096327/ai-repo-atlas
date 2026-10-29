# jghiringhelli/codeseeker

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-10-04 · [GitHub](https://github.com/jghiringhelli/codeseeker) · 组织维护

**给 AI 编程助手的代码库混合检索与知识图 MCP 服务器**

CodeSeeker 是一个 TypeScript 编写的 MCP 服务器，面向 Claude Code、GitHub Copilot、Cursor、Windsurf 与 Claude Desktop 等 AI 编程助手。它对代码库建立索引，将 BM25、向量嵌入、RAPTOR 目录摘要与基于 AST 解析 imports 构建的知识图融合为单个 MCP 工具，提供 search/sym/graph/analyze/index 五种 action，支持语义搜索、符号邻域查询、图遍历、编码规范检测、重复代码与死代码分析。索引快照不自动监听文件系统，需通过 Claude Code 插件 hooks 或手动 sync 保持同步。由 PragmaWorks 公司构建，属其 Generative Specification 项目组件之一。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四层混合检索：BM25 + 向量嵌入 + RAPTOR 摘要 + 图扩展，RRF 融合
- 基于 AST 解析 imports 构建知识图，支持图遍历与死代码检测
- 单个 MCP 工具 + action 路由，降低每次请求的 token 开销
- 首次搜索自动触发后台索引，stale_index 信号提示索引过期

## 适用场景

- 让 AI 编程助手按语义而非关键字检索代码库
- 查询函数/类的依赖、调用与继承关系
- 检测项目中的重复代码、死代码与既有编码规范
- 在 Devcontainer/Codespaces 中为团队预置代码检索能力

## 场景标签

`知识图谱` `语义搜索` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: **Four-layer hybrid search and knowledge graph for AI coding assistants.**
> L10: Works with **Claude Code**, **GitHub Copilot** (VS Code 1.99+), **Cursor**, **Windsurf**, and **Claude Desktop**.
> L183: CodeSeeker exposes **one** MCP tool, `codeseeker`. You pick behaviour with `action` and

## 星数曲线

```mermaid
xychart-beta
    title "jghiringhelli/codeseeker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8f7b4379a2e1` · [字段定义](../../DATASET.md)*
