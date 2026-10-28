# Nurysso/eulix

⭐ 21 · Rust · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/Nurysso/eulix) · 个人维护

**本地优先的大型代码库索引与检索工具：符号、调用图、可选 LLM 问答**

面向大型代码库的本地代码智能工具：将仓库解析为可查询索引（符号、调用图、可选的本地嵌入），按问题类型路由到最廉价机制——精确符号查找、调用图、项目元数据走确定性路径，语义/推理类问题走检索加可选 LLM。支持 C/C++/Go/Java/JS/PHP/Python/Rust/TS 九种语言，Linux 内核 37.3M 行 57 秒完成解析。通过 CLI、MCP 服务器（供 Claude Code 等编码代理查询）、Beta LSP、Rust 库 libeulix 和浏览器调用图浏览器等多种形态提供。需 Linux 或 Windows，macOS 二进制未测试；JSX/TSX 暂不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 查询分类路由：多数问题不调用 LLM，直接由索引确定性回答
- Linux 内核 37.3M 行 57 秒解析，约 65 万行/秒
- 解析、索引、检索、嵌入全程本地运行，LLM 为可选层
- 多形态交付：CLI、stdio MCP 服务器、Beta LSP、libeulix Rust crate、浏览器调用图浏览器

## 适用场景

- 在超大陌生代码库中定位符号、追踪调用链与依赖
- 通过 MCP 让 Claude Code / Windsurf / Cline 等编码代理查询仓库获取有出处的代码上下文
- 对私有仓库做全本地、不外发数据的代码问答
- 在浏览器中交互式浏览项目调用图与子系统结构

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: Eulix parses your repository into a queryable index — symbols, call graphs, and optional embeddings — and routes eve
> L191: ## Ecosystem
> L205: An MCP server (stdio) that lets agents such as Claude Code, Windsurf, Cline, Continue, and LM Studio query any ana

## 星数曲线

```mermaid
xychart-beta
    title "Nurysso/eulix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b9d3cc7ebc54` · [字段定义](../../DATASET.md)*
