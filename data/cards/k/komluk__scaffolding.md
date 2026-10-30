# komluk/scaffolding

⭐ 15 · Shell · MIT · 推送 2026-10-29 · [GitHub](https://github.com/komluk/scaffolding) · 个人维护

**Claude Code 的纯 markdown 多 agent 编排插件：13 agent+技能+守卫钩子**

面向 Claude Code 用户的插件，以纯 markdown 文件形式提供多 agent 编排：13 个专职 agent（analyst/architect/developer/reviewer 等）、39 个技能、20 个命令与 18+ 个安全/生命周期钩子，支持 spec 驱动工作流、按阶段指定模型层级（sonnet/opus/haiku）与文件式三层 agent 记忆；全部运行在 Claude Code 自带运行时上，无需后端与数据库。跨设备语义记忆为可选，需自建 mem0 后端，缺失时优雅降级。通过 /plugin 命令安装，依赖 git 与 Claude Code CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个专职 agent + 并行多 agent 协调与 peer-to-peer 通信
- 18+ 安全/生命周期钩子：拦截破坏性命令、禁用越权子 agent
- 按阶段模型层级：analyst/architect/reviewer 可声明 opus + effort: high
- 文件式三层 agent 记忆协议，可选 mem0 后端实现跨设备语义记忆

## 适用场景

- 在 Claude Code 中以 spec 驱动方式分解并执行软件工程任务
- 团队仓库通过提交的 CLAUDE.md 让编排协议随代码分发
- 让不同阶段使用不同模型层级并做跨模型代码审查

## 场景标签

`多智能体` `编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Spec-driven multi-agent orchestration for Claude Code — pure markdown, zero backend,
> L11: `claude-scaffolding` is a portable, markdown-only Claude Code configuration. It
> L12: provides multi-agent orchestration, a library of reusable skills, guardrail

## 星数曲线

```mermaid
xychart-beta
    title "komluk/scaffolding 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `72b2d4dffd54` · [字段定义](../../DATASET.md)*
