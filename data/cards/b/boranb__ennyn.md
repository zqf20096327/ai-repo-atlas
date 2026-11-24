# boranb/ennyn

⭐ 3 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/boranb/ennyn) · 个人维护

**给 Claude Code 编码代理提供工作流程例行程序的工具**

以 Claude Code 插件与 Node CLI 双形态发行，为代理式编码设定固定例程：写码前填写影响分析表（用 git grep/git log/测试回答五个问题）、两轮代码评审、每次提交经 commit-msg hook 检查重复出现的 bug 类别并转化为门禁（测试或 hook 规则）。每个周期输出五项指标，任务存于 JSON 工作图，每周期取四项。无运行时依赖、无安装脚本，需 Node 22+ 与 git 2.34+，仅在网络查询 npm registry 与 OSV 数据库时发起请求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 写码前影响分析表：用 git grep、git log 或测试回答五问
- 两轮评审与周期指标（评审发现的 bug、修复引入的回归、门禁拦截数等）
- 重复 bug 类别自动转化为测试或 commit-hook 门禁
- 克隆后两条命令可在任意 git 仓库免安装试用

## 适用场景

- 让 Claude Code 代理按固定例程写码并量化其质量指标
- 将重复出现的 bug 固化为提交门禁，替代不断膨胀的 CLAUDE.md 规则
- 在任意 git 仓库测量修复引发回归的比例与代理指令文本体积

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: Ennyn is a Claude Code plugin and Node CLI. It gives the agent a working routine: impact analysis before code is wri
> L80: The cycle skill in `skills/cycle/` follows the Agent Skills format, but it calls the CLI through `${CLAUDE_PLUGIN_R


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `ce9bf26b798e` · [字段定义](../../DATASET.md)*
