# NoobyGains/godmode

⭐ 114 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/NoobyGains/godmode) · 个人维护

**给 AI 编程 agent 注入工程纪律的技能包（33 个 skills，多 harness 通用）**

面向 AI 编程 agent（Claude Code、Antigravity、Codex、Cursor、OpenCode 等）的 Markdown 技能集与两个 hook，通过会话启动 bootstrap 与每条提示的一行提醒注入。核心机制是门控流水线：质疑需求（rationale）、对照当前文档核验事实（grounding）、在能胜任的最廉价模型上按测试先行开发、跨模型家族评审（cross-model-review）、凭新鲜命令输出才能宣称完成（completion-gate）。零依赖、不调用网络服务、不收集遥测。各 harness 的安装方式与验证状态以表格列出，部分为 untested。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 33 个技能组成 define/plan/execute/review/ship 门控流水线
- grounding 技能拒绝凭记忆编码，核验当前文档并记录出处
- cross-model-review 要求另一模型家族（Codex/Gemini/Claude）评审后才落地
- 零依赖、无网络调用、无遥测，覆盖 6 类 harness

## 适用场景

- 让 Claude Code/Codex/Cursor 等 agent 遵循测试先行与文档核验的流程
- 在宣称任务完成前强制执行验证输出
- 控制 agent 的模型与执行模式路由以降低成本

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Your coding agent questions the request, verifies against current docs instead of its memory, plans, builds test-fi
> L60: > Nothing to configure. GodMode is Markdown skills plus two small hooks (a session-start bootstrap and a one-line r
> L86:  🧩 One repo, every harness

## 星数曲线

```mermaid
xychart-beta
    title "NoobyGains/godmode 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-27"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-26 114 → 2026-10-27 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0b8d0d470282` · [字段定义](../../DATASET.md)*
