# Leoomk/contextmap

⭐ 4 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Leoomk/contextmap) · 个人维护

**为 AI 编码助手提供本地 AST 代码上下文映射的 MCP 服务器**

在本地运行的 MCP 服务器与仪表盘：用 Tree-sitter 从 AST 解析代码库，生成依赖图、PageRank 中心文件、1-3 级影响追踪（domino effect）与代码骨架，配合增量 SHA-256 缓存减少重复解析；通过 MCP 工具向 Cursor、Claude 等客户端提供上下文，并内置模态框误关闭、N+1 查询、表单草稿等代码传感器与持久化检查清单。面向用 AI 助手开发应用的开发者，要求 Node.js v18+，代码不离开本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 web-tree-sitter 的 AST 依赖图与增量哈希缓存
- PageRank 识别中心文件并追踪 1-3 级影响
- 提取代码骨架以减少 prompt token 消耗
- 提供 9 个 MCP 工具与本地双语仪表盘（localhost:3000）

## 适用场景

- 让 AI 编辑代码前先获取精确的依赖影响范围
- 标记已决策的检查项避免 AI 重复审查
- 检测模态框误关闭、N+1 查询等常见缺陷模式

## 场景标签

 · 领域:开发者工具/AI 编码基础设施

## 证据(README 行号)

> L15: **ContextMap** runs **100% locally on your machine** (your code never leaves your computer), parses your codebase d
> L55: ## 🔌 Connecting to Your AI via MCP (Cursor, Claude, Antigravity, Windsurf)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `a56000777320` · [字段定义](../../DATASET.md)*
