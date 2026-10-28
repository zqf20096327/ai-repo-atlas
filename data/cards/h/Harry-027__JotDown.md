# Harry-027/JotDown

⭐ 23 · Rust · MIT · 推送 2026-02-24 · [GitHub](https://github.com/Harry-027/JotDown) · 个人维护

**Rust 编写的 MCP 服务器：让 LLM 创建 Notion 页面与生成 mdBook**

基于 Rust 实现的 Model Context Protocol（MCP）服务器，向 LLM 提供两个工具：Notion 页面工具（通过 Notion API 创建或更新页面）与 mdbook 工具（生成含 SUMMARY.md、README.md 与各章节 Markdown 文件的 mdbook，需安装 mdbook CLI）。面向使用 Claude Desktop、Cline、Continue 等 MCP 客户端的开发者；运行需 Rust 工具链、Notion internal integration token，且需在 Notion 工作区创建名为 Jot It Down 的页面并与连接共享。安装方式为克隆仓库后 cargo build --release 编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Notion 页面创建/更新工具，调用 Notion API
- 提供 mdbook 生成工具，自动生成 SUMMARY.md 与章节结构
- 以 MCP 协议与 Claude Desktop、Cline、Continue 等客户端集成

## 适用场景

- 让 Claude 等 MCP 客户端把生成的内容直接写入 Notion
- 从 LLM 生成的内容自动构建完整的 mdbook 文档
- 在内容管理与发布工作流中接入 MCP 工具

## 场景标签

 · 领域:LLM 工具集成/MCP 服务器

## 证据(README 行号)

> L4: Jotdown is a Model Context Protocol (MCP) server that allows large language models (LLMs) to interact with **Notion*
> L22: - 🌿 **MCP Support**: Leverages the Model Context Protocol to maintain context over interactions, enabling more inte

## 星数曲线

```mermaid
xychart-beta
    title "Harry-027/JotDown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ba3dd69b090a` · [字段定义](../../DATASET.md)*
