# altmbr/claude-research-skill

⭐ 21 · MIT · 推送 2026-03-06 · [GitHub](https://github.com/altmbr/claude-research-skill) · 个人维护

**Claude Code 技能：把研究问题分解为并行 agent 并综合成文档**

以 SKILL.md 形式提供的 Claude Code 技能：/research 命令将任意研究问题分解为 2-4 个不重叠的并行研究工作流，经用户批准后启动多个子 agent，各 agent 按严格写后即搜协议向独立 markdown 文件实时写入带内联引用的研究内容；编排器按递增间隔（30s/2min/5min）监控进度，自动杀死并预加载数据重启卡住的 agent；最后由综合 agent 生成含执行摘要、跨主题发现、矛盾点与置信度评估的统一文档。安装方式为复制 SKILL.md 到 Claude Code 命令目录，需 Claude Code CLI，无需 API key 或外部依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 问题分解为 2-4 个并行研究工作流，启动前需用户批准计划
- 写后即搜协议强制 agent 每次搜索后写入文件，防止循环
- 卡住 agent 自动杀死并以已获数据预加载重启
- 综合 agent 产出跨主题发现、矛盾点与置信度评估的统一文档

## 适用场景

- 在 Claude Code 中用一条命令发起多来源深度研究
- 自动监控并恢复卡住的研究子 agent
- 把多份研究产出综合为带内联引用的统一文档

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Claude Code skill that decomposes any research question into parallel agent workstreams, launches them simultaneou
> L46: The skill uses Claude Code's built-in Task tool to launch multiple `general-purpose` subagents in parallel. Each ag
> L83: - Claude Code (CLI)

## 星数曲线

```mermaid
xychart-beta
    title "altmbr/claude-research-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `10b569a35e63` · [字段定义](../../DATASET.md)*
