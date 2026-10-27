# 0x7067/claude-jev

⭐ 25 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/0x7067/claude-jev) · 个人维护

**Claude Code 插件：用 Jev 做规则检查、逐行压缩与提示路由**

面向 Claude Code 与 Pi 编码代理的插件，将小型判断类调用发送到 TypeSafe 的 Jev 模型（System One，返回类型化答案）。提供四类钩子：对编辑按 CLAUDE.md/AGENTS.md 等指令文件规则做判定并阻断违规（带 file:line 引用）、以保留原始行替代摘要式上下文压缩（约一秒完成）、为子代理分配模型层级并检查任务简报、为每个提示生成一行路由提示。所有钩子 fail-open，缺 API key 或出错时不阻断。需要 python3 标准库，ast-grep 为可选依赖。

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

- 按指令文件规则判定编辑并阻断违规，输出 file:line 引用
- 以保留原始行的方式替代摘要压缩，压缩耗时约一秒
- 为子代理分配模型层级并退回缺失要素的任务简报
- 所有钩子 fail-open：错误或缺 key 不阻断提示

## 适用场景

- 在 Claude Code 中自动检查编辑是否违反项目指令文件规则
- 长会话中用保留关键行的方式压缩上下文
- 为每个提示获得路由提示与模型分层建议

## 场景标签

`代码审查` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: A coding agent makes dozens of quick calls every turn. What kind of prompt is this? Does it need tools? Does this ed
> L80: |Hook|Job|
> L134: `hooks/register.ts` hooks `session.compact`. On `/compact`, auto-compaction, and `/rewind` summaries, it hands the

## 星数曲线

```mermaid
xychart-beta
    title "0x7067/claude-jev 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `84c8ae428e91` · [字段定义](../../DATASET.md)*
