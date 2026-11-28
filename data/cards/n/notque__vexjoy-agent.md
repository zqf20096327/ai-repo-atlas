# notque/vexjoy-agent

⭐ 452 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/notque/vexjoy-agent) · [官网](https://vexjoy.com) · 个人维护

**给 Claude Code 等 agent CLI 提供技能/流水线/钩子的开发工具包**

面向开发者的 agent 工作流工具包：通过 `/do` 等入口把自然语言请求路由到 46 个技能与 26 条流水线，65 个钩子在提交、推送、PR 合并、破坏性命令等节点执行拦截与校验，160 个脚本处理可重复工作。可选的 `/d` 路由依赖 TypeSafe Jev 做意图对齐判定。安装脚本会写入 `~/.claude/settings.json` 并在所有仓库生效，提供 `--dry-run`、`--uninstall` 等退出选项。

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

- 46 技能、26 流水线、65 钩子、160 脚本的四层结构
- 跨 Claude Code、Codex、Factory、Reasonix、Antigravity CLI 多运行时安装
- 可选 Jev 意图对齐路由 `/d`，带 intent 保留校验与 learning.db 记录
- 反合理化机制：技能退出关卡要求测试输出等证据

## 适用场景

- 给 Claude Code 里的编码 agent 补充领域知识与流程约束
- 在团队仓库中用钩子强制 CI 通过后才能合并 PR
- 用流水线管理调试、内容写作等多阶段开发任务

## 场景标签

`工作流自动化` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: VexJoy Agent connects plain-English requests to skills and workflows. `/do` selects the knowledge and tools needed f
> L11: 46 skills, 26 pipelines, 65 hooks, 160 scripts. Skills carry domain knowledge and reusable methods, pipelines hold 
> L113: Installs into `~/.claude/`, and into `~/.codex/`, `~/.factory/`, `~/.hermes/`, `~/.reasonix/`, `~/.gemini/` (Antig

## 星数曲线

```mermaid
xychart-beta
    title "notque/vexjoy-agent 星数(近 9 点)"
    x-axis ["2026-10-26", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-14", "2026-11-18", "2026-11-26", "2026-11-28"]
    y-axis "stars" 442 --> 453
    line [443, 444, 443, 448, 449, 450, 451, 452, 452]
```

2026-10-26 443 → 2026-11-28 452（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `81359dcb6799` · [字段定义](../../DATASET.md)*
