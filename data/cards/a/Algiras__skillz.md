# Algiras/skillz

⭐ 33 · Rust · MIT · 推送 2026-02-18 · [GitHub](https://github.com/Algiras/skillz) · [官网](https://algiras.github.io/skillz) · 个人维护

**可在运行时自建工具的 MCP 服务器：AI 动态创建并执行工具**

Rust 实现的 MCP 服务器，让 AI 客户端在运行时创建并执行自定义工具：将 Rust 代码编译为 WASM 工具（支持 crate 依赖），或注册 Python/Node.js 等脚本工具并自动安装依赖。支持导入外部 stdio MCP 服务器、声明式流水线、Docker 服务管理、持久化存储、版本回滚与可选沙箱隔离（bubblewrap/firejail/nsjail）。技能机制兼容 Claude Skills 的 SKILL.md 格式，可从 GitHub 仓库导入技能。通过 crates.io 以 cargo 安装，配置到 Cursor、Claude Desktop 等 MCP 客户端使用；也支持 HTTP 传输模式。限制：导入外部 MCP 仅支持 stdio，HTTP/SSE 尚未支持。

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

- 运行时将 Rust 编译为 WASM 工具，支持 serde/regex 等 crate 依赖
- 注册多语言脚本工具并自动安装 pip/npm/cargo 依赖
- 导入外部 stdio MCP 服务器、从 GitHub 仓库导入 Claude Skills 兼容技能
- 可选沙箱隔离（bubblewrap/firejail/nsjail）与 Docker 服务管理

## 适用场景

- 让 Claude/Cursor 等 MCP 客户端在对话中自行创建所需工具
- 将常用脚本封装为可被 AI 调用的 MCP 工具
- 为工具声明依赖的 Docker 服务（如 Postgres）并自动管理启停

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: **Build and execute custom tools at runtime. Let your AI create its own tools.**
> L23: Traditional MCP servers have a fixed set of tools. **Skillz lets your AI create new tools on the fly.**
> L143: |🔌 **MCP Integration**|Import external stdio MCP servers, expose tools under namespaces|

## 星数曲线

```mermaid
xychart-beta
    title "Algiras/skillz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5060014a352d` · [字段定义](../../DATASET.md)*
