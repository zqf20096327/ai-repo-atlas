# oguzyl11/ast-pack

⭐ 6 · Rust · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/oguzyl11/ast-pack) · 个人维护

**把代码库折叠进 LLM token 预算的 CLI 与 MCP 服务器**

Rust 编写的 CLI 与 MCP 服务器：将仓库按 token 预算打包为分层内容（L0 全文至 L4 省略），被折叠符号保留稳定 fold id，agent 可通过 unfold 按需取回函数体，内容不删除仅延后。内部用 Tree-sitter 解析 7 种语言、构建符号图并以 personalized PageRank 排序决定升级层级，用 o200k/cl100k tokenizer 计数，同一输入输出字节一致。提供 setup 命令向 Cursor、Claude Code、Codex、Gemini CLI 注册 MCP 服务器，自带 context-bench 基准语料。

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

- L0-L4 四级折叠与稳定 fold id，unfold 按需取回符号体
- Tree-sitter 解析 Rust/TypeScript/TSX/JavaScript/Python/Go/Java，blake3 缓存
- personalized PageRank 排序符号，按每 token 收益升级层级
- 提供 MCP 服务器与 context-bench 基准（6 仓库×25 问题）

## 适用场景

- 把大型仓库压缩进 agent 的上下文窗口预算
- 在 Claude Code/Cursor 等 agent 中按需展开符号代码
- 评估不同上下文打包方式的 token 覆盖率

## 场景标签

 · 领域:开发工具/LLM 基础设施

## 证据(README 行号)

> L5: `ast-pack` is a Rust CLI and MCP server. It packs a repository into a hard token budget. Anything it leaves out keep
> L40: `setup` registers the MCP server with Cursor, Claude Code, Codex, and Gemini CLI. It copies each file it edits asid


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `effed4646de6` · [字段定义](../../DATASET.md)*
