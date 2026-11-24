# sam-ash-cy/sams-agentic-workflow

⭐ 4 · TypeScript · MIT · 推送 2026-11-12 · [GitHub](https://github.com/sam-ash-cy/sams-agentic-workflow) · 个人维护

**给 Claude Code 加验证门与护栏的开发工作流插件**

以 Claude Code 插件形式分发、运行在 bun 上的 agent 工作流系统：按风险给任务分级（trivial→critical）并匹配 playbook，Stop hook 依据实际记录的检查结果放行 "done"，push/删除/部署/密钥等操作先经 hook 校验。配置分四层（内置默认→全局→项目→本地），45+ 功能均可全局或按项目开关，提供 dashboard pane、token 预算、任务日志与 retro 复盘、计划队列与 headless autopilot。

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

- 按风险分级的 Router 与对应 tier 的检查 Gate（tests/lint/reviews 记录通过才放行）
- Guard hook 在 shell 命令与编辑执行前校验安全与自治规则
- 四层配置（global/project/local TOML）与逐功能开关、profile 预设
- 任务结果日志与 `saw retro` 从反复失败的检查生成修复提案

## 适用场景

- 让编码 agent 在声称完成前必须跑过并记录测试、lint、review
- 限制 agent 的 push、删除、部署与新增依赖等危险操作
- 按项目或个人自定义 agent 工作流的严格程度与功能开关

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: **Make your coding agent prove it's done.** A Claude Code plugin that sizes every task by risk, blocks "done" until
> L69: The `router` skill picks the tier and playbook, and `saw task start` prints the steps and required checks. The agen

## 星数曲线

```mermaid
xychart-beta
    title "sam-ash-cy/sams-agentic-workflow 星数(近 2 点)"
    x-axis ["2026-11-11", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-11 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `6d622e57495f` · [字段定义](../../DATASET.md)*
