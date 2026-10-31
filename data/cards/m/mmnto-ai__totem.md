# mmnto-ai/totem

⭐ 18 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/mmnto-ai/totem) · 个人维护

**把项目规则与教训固化为可执行 lint 的代码库治理 CLI**

面向使用 AI 编码 agent 的团队的文件式治理工具包：以仓库内 markdown 教训文件为权威源，`totem lesson compile` 将自然语言教训编译为 AST/regex 规则，由零 LLM、离线、确定性的 `totem lint` 在 pre-push 钩子与 CI 中强制执行；`totem sync` 用 Tree-sitter + LanceDB 从教训与 ADR 派生本地语义索引，经内置 MCP server 供 agent 查询；`totem spec`/`totem review` 为可选的 LLM 驱动命令。编辑器集成覆盖 Claude Code、Gemini CLI、Copilot、Junie 等。README 明示教训编译器自 2026-05-17 冻结（fail-closed），纪律与遥测层在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 零 LLM、离线、确定性 lint：教训编译为 ast-grep/regex 规则，pre-push 拦截
- Tree-sitter + LanceDB 派生本地语义索引，内置 MCP server 供 agent 查询
- SARIF 输出接入 GitHub Code Scanning；无 Node 环境可用 Totem Lite 独立二进制
- 46 个 CLI 命令，支持 --json 脚本化

## 适用场景

- 阻止 AI 编码 agent 重复犯同类架构错误并在 push 时拦截
- 把 PR 评审教训沉淀为项目内可执行的规则
- 让 MCP 兼容 agent 在写代码前查询项目禁用模式与历史教训

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: _AI coding agents are brilliant goldfish. Totem keeps your project's lessons, rules, and context in the repository 
> L86: MCP-compatible agents query it through the bundled MCP server. Registering that server with your agent is a one-tim
> L90: Totem is a set of CLI tools, not a framework. Building blocks you wire into whatever CI and workflow you already ha

## 星数曲线

```mermaid
xychart-beta
    title "mmnto-ai/totem 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f12bdbec8934` · [字段定义](../../DATASET.md)*
