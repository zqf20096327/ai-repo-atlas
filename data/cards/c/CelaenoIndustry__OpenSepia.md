# CelaenoIndustry/OpenSepia

⭐ 35 · Python · MIT · 推送 2026-03-18 · [GitHub](https://github.com/CelaenoIndustry/OpenSepia) · 组织维护

**9 个 Claude agent 组成的自主敏捷开发团队，cron 驱动 24/7 运行**

基于 Claude Code CLI 的多 agent 软件开发编排系统：9 个角色化 agent（PO、PM、两名开发者、DevOps、QA 及三人安全团队）按 cron 周期（默认 40 分钟）轮流执行，通过 Markdown inbox 文件与本地看板（sprint.md/backlog.md）通信，产出用户故事、代码、测试、代码评审与合并请求。无需 API key，直接消耗 Claude Pro/Max 订阅额度；依赖 Bash + Python(pyyaml)。支持 GitLab/Github 双向看板同步、MR 自动合并、看板快照与自动恢复；也可在无集成状态下仅用本地文件运行。README 建议在 VM/LXC/Docker 隔离环境运行，因 agent 具有执行 shell 命令的权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个角色化 agent 覆盖敏捷全流程（规划/开发/评审/测试/安全审计/部署）
- cron 驱动的跨周期持续自主运行，状态持久化于 Markdown 看板
- GitLab/GitHub 双向看板同步、MR 自动合并与 stale 分支清理
- 通过 claude --print 逐 agent 调用，无需 API key

## 适用场景

- 给一段需求简报，让 agent 团队过夜自主完成开发与合并
- 按日调度安全团队做 OWASP 审计与渗透测试模拟
- 以 issue/Kanban 形式在 GitLab/GitHub 上跟踪 AI 团队产出

## 场景标签

`多智能体` `编码 Agent` `代码审查` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L5: 9 specialized AI agents collaborate as a real agile team — they plan sprints, write code, do code reviews, test, han
> L83: > **How it works under the hood:** Each agent is executed via `claude --print` with a carefully crafted system prom

## 星数曲线

```mermaid
xychart-beta
    title "CelaenoIndustry/OpenSepia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `05f69a040d36` · [字段定义](../../DATASET.md)*
