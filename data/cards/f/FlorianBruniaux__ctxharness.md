# FlorianBruniaux/ctxharness

⭐ 26 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/FlorianBruniaux/ctxharness) · [官网](https://ctxharness.bruniaux.com) · 个人维护

**检测 AI 指令文件中文档漂移的 CLI/TypeScript 库**

面向使用编码 agent 的开发者，CTX Harness 是本地 CLI 与 TypeScript 库：读取 CLAUDE.md、AGENTS.md、.cursorrules 等指令文件，将其中的路径、npm 脚本、版本、数量等声明与代码库实际状态比对，发现漂移即退出码 1；另提供模糊用语启发式、上下文 token 预算、Claude Code/Codex 配置诊断（doctor）及可移植 JSON 证据导出。配置用 .ctxharness.yml 声明断言，含 20 个提取器与 15 个扫描器。CLI 依赖 Node.js，即使检查 Python/Go/Rust 项目；v0.5.0 需从源码构建使用审计/导出功能（git tag 未发布 npm 包，已装包可能仍是 0.4.6）。诊断过程不执行任何被检查的 hook、skill 或 MCP 服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 文档声明与代码库比对（路径/脚本/版本/数量），发现漂移退出码 1
- 20 个提取器 + 15 个扫描器（含 gitStaleness 新鲜度、contextBudget token 估算、vaguenessPattern 模糊用语检测）
- doctor 命令诊断 Claude Code 与 Codex 的 instruction/skill/rule/agent/hook/MCP 声明
- 导出省略原始路径、消息与凭证的可移植版本化 JSON 证据

## 适用场景

- CI 中拦截 CLAUDE.md 里失效的路径和过时版本号
- 检查 rules 文件的 token 占用与模糊指令占比
- 审计 Claude Code/Codex 项目配置并导出证据供其他工具使用

## 场景标签

 · 领域:开发者工具/上下文工程

## 证据(README 行号)

> L10: Catch stale paths, scripts and versions in your AI docs. Inspect Claude Code and Codex configuration, measure stati
> L12: CTX Harness is a local CLI and TypeScript library. It reads your existing `CLAUDE.md`, `AGENTS.md` and `.cursorrule
> L31: |**Configuration diagnosis (L3)**|Supported instruction, skill, rule, agent, hook and MCP declarations for Claude C

## 星数曲线

```mermaid
xychart-beta
    title "FlorianBruniaux/ctxharness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4cf2301f1bd2` · [字段定义](../../DATASET.md)*
