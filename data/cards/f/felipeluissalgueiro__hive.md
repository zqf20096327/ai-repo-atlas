# felipeluissalgueiro/hive

⭐ 22 · HTML · MIT · 推送 2026-06-03 · [GitHub](https://github.com/felipeluissalgueiro/hive) · [官网](https://hive.cadencia.ia.br) · 个人维护

**在 Claude Code 内以 11 个专业 AI 小队运营公司的开源脚手架**

面向创业者/小团队的开源 harness：以 Markdown 文件与 Python 脚本组织 11 个领域小队（销售/客服/营销/财务/开发等），每个小队有 persona、context、记忆（L1/L2/L3 状态架构）与技能，由编排者 Stamper 路由分派。5 个 hooks 自动管理会话分支与提交，50 个技能命令，workers 目录的纯 Python 脚本经 cron/systemd 调度独立于 AI 运行。默认搭载 Linear 作 PM 工具，可选经 OpenRouter 查询任意模型做第二意见/共识面板等。要求 Claude Code、Git、Python 3.8+，无框架与 Docker 依赖。

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

- 11 个领域小队 + Stamper 编排者，各带 persona/记忆/决策日志
- 5 个 hooks 自动处理会话分支、提交合并与敏感操作前知识查询
- 50 个可复用技能命令（/skill-name 调用）
- workers 纯 Python 脚本由 OS 调度器执行，AI 不在环

## 适用场景

- 用一组专业 AI agent 分工处理公司各部门事务
- 聚合查看所有小队的公司级状态（/status）
- 在 Claude Code 内跨模型做第二意见与共识校验

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L25: HIVE is an open-source harness for running a full company with AI agents inside **Claude Code**.
> L27: You get 11 specialized squads — each a domain expert AI with its own persona, memory, and decision log — plus an or
> L221: - Git

## 星数曲线

```mermaid
xychart-beta
    title "felipeluissalgueiro/hive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `14ac93084419` · [字段定义](../../DATASET.md)*
