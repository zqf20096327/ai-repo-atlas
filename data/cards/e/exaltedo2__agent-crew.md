# exaltedo2/agent-crew

⭐ 3 · PowerShell · MIT · 推送 2026-11-23 · [GitHub](https://github.com/exaltedo2/agent-crew) · 个人维护

**为 Claude Code 提供可复用的多智能体协作团队与成本账本**

面向 Claude Code 的领域无关多智能体配置集合：内置 lead/thinker/architect/coder/reviewer/scout 六个固定角色，附带 cost ledger 按模型家族计价、12 个 hooks、bootstrap/hire/retire/retro 等技能，以及可选的自主雇人/裁人机制（默认 ask，需用户逐条确认）。每个项目通过 .claude/team/PROJECT.md 描述自身，安装脚本将 agent 与 hooks 复制到用户级 ~/.claude/ 目录并合并 settings.json，支持更新与卸载。依赖 Claude Code、PowerShell 与 git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六个默认角色分工固定：编排者不直接改文件，coder 负责实现并跑全部检查
- cost ledger 按模型家族（match 词 + 价格表）计费，未知家族降级到 default 条目并告警
- install.ps1 合并 hooks 到 settings.json，重复运行不重复写入，支持 -Update/-Uninstall
- 自主团队机制：trial 角色限定 sonnet/medium，用量超 10% 自动退役

## 适用场景

- 给多个项目套用同一套 Claude Code 子智能体分工与交接规则
- 追踪团队中各模型调用的花费并控制编排者成本
- 按失败模式增减审阅/测试等扩展角色并保留退役记录

## 场景标签

`多智能体` `编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: A reusable, domain-free multi-agent team for Claude Code.
> L77: Requirements: Claude Code, Windows PowerShell 5.1 or PowerShell 7, git.
> L105: Then, in a project: start Claude Code with `claude --agent lead` (the bootstrap also proposes


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `0d5f8ca761d3` · [字段定义](../../DATASET.md)*
