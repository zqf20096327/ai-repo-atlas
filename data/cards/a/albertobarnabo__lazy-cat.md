# albertobarnabo/lazy-cat

⭐ 51 · JavaScript · MIT · 推送 2026-10-02 · [GitHub](https://github.com/albertobarnabo/lazy-cat) · 个人维护

**Claude Code 技能包：约束 AI 编码代理优先选省 token 的最小方案**

面向使用 Claude Code 等 AI 编码代理的开发者，提供两个技能：think-twice 在动手前检查是否已有 API/包/单行方案可用，surgical 在写每段代码前阻止未被要求的功能扩展，从而减少输出 token。安装方式包括 npx 安装器（同时支持 Gemini CLI 与 Codex）、plugin 系统与 curl 下载 SKILL.md，也可将规则直接写入 CLAUDE.md。附可选的 token 用量统计 hook（数据仅存本地）。README 给出 17 个场景的模拟 token 对比，并注明实测中小编辑场景节省未复现、技能反而增加约 8% 成本；同时列出安全关键代码等应覆盖规则的场景。

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

- think-twice 与 surgical 两个技能分别拦截错误策略与范围蔓延
- npx lazycat-skill 一条命令安装到 Claude Code / Gemini CLI / Codex
- 可选 Stop hook 记录每会话输出 token 到本地 usage.jsonl
- 附 17 场景 token 对比表与'何时不适用'覆盖规则清单

## 适用场景

- 给 Claude Code 会话加规则，减少未被要求的代码生成
- 在多个 AI 编码代理间统一最小实现的行为约束
- 统计安装技能前后的 token 用量变化

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L28: |**think-twice**|Before picking an approach|Implementing from scratch when an API, package, or one-liner already ex
> L29: |**surgical**|Before writing each block|Adding error handling, tests, and abstractions nobody asked for|
> L160: ### Option 2 — Claude Code skills
> L162: Skills load their full rulebook when invoked manually or when Claude judges the context matches. Better for on-dem

## 星数曲线

```mermaid
xychart-beta
    title "albertobarnabo/lazy-cat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-26 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ff3634382b3f` · [字段定义](../../DATASET.md)*
