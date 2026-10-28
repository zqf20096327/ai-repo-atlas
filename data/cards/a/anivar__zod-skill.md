# anivar/zod-skill

⭐ 23 · MIT · 推送 2026-10-18 · [GitHub](https://github.com/anivar/zod-skill) · [官网](https://skills.sh/anivar/zod-skill) · 个人维护

**教 AI agent 正确使用 Zod v4 的技能包（27 条规则）**

面向 Claude Code、Cursor、Codex、Windsurf 等 coding agent 的技能（skill）包，提供 27 条 incorrect→correct 对照规则与 9 篇深度参考，覆盖 Zod v4 的 schema 设计、解析（parse/safeParse/parseAsync）、错误处理、类型推断、性能与 v3→v4 迁移等内容。规则基于 Zod 官方文档而非 release notes 校准（基线 zod ^4.6.0、TypeScript ^5.5）。通过 npx skills add 安装，测试规则由原 zod-testing 技能合并而来。

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

- 27 条 incorrect→correct 规则，分 9 类覆盖解析/设计/错误处理/迁移等
- 9 篇深度参考含反模式清单（14 个常见错误）与边界架构（Express/tRPC/Next.js 等）
- 以 zod.dev 官方文档为校准基线（zod ^4.6.0，2026 年 10 月审计）
- npx skills add 一条命令安装，兼容多家 coding agent

## 适用场景

- 让 Claude Code/Cursor 等 agent 写出符合 Zod v4 API 的 schema
- 修正 agent 生成的 Zod v3 过时写法与解析陷阱
- 查阅 Zod 在 Express/tRPC/Next.js 等边界的架构位置

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: An AI agent skill for writing, validating, and debugging Zod v4 schemas with modern best practices.
> L13: 27 rules with incorrect→correct code examples that teach agents Zod v4's actual API behavior, schema design pattern

## 星数曲线

```mermaid
xychart-beta
    title "anivar/zod-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c6782d8952a3` · [字段定义](../../DATASET.md)*
