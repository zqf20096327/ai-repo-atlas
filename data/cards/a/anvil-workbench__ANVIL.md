# anvil-workbench/ANVIL

⭐ — · [GitHub]() · 组织维护

**AI 编码代理的本地确定性验证层，合并前检查代码变更**

ANVIL 是一个面向 AI 辅助软件工程的本地验证工具：当 Claude Code、Cursor、Codex 等编码代理生成代码变更后，ANVIL 在本地评估 AST、依赖图与 git diff，提供爆炸半径计算、策略门禁、密钥扫描与测试建议。通过只读 MCP 服务器以少于 1.5k token 输出架构摘要，供代理查询仓库结构。提供 CLI 命令集、pre-commit hook、GitHub Action 与 SARIF 报告，MIT 许可，fork 自 FORGE 项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 只读 MCP 服务器输出架构摘要与循环依赖图（<1.5k token）
- 确定性质量与策略门禁，支持 SARIF 与 baseline 对比
- 硬编码密钥扫描与 agent 指令/提示注入审计
- 爆炸半径计算与下游受影响模块及建议测试

## 适用场景

- AI 代理生成的代码在合并前做本地验证
- CI 中对 PR 执行策略与安全门禁
- 防止密钥或策略回退被提交到仓库

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L23: **ANVIL** is a local-first, deterministic **verification layer** for AI-assisted software engineering.
> L97: |`anvil mcp [setup\|start]`|Sets up or runs local read-only Model Context Protocol server|`[setup]`|**Available**|
> L107: [ AI Coding Agent ] ──writes code──> [ Local Repo ] ──verified by──> [ ANVIL Gate ] ──PR──> [ Merge ]


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `071675899837` · [字段定义](../../DATASET.md)*
