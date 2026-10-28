# Xsxdot/handoff

⭐ 25 · Go · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/Xsxdot/handoff) · [官网](https://handoff.gosuper.dev) · 个人维护 · 中文 README

**CLI 两角色协作工具：把实现计划派给其他 AI 执行，人只负责审**

Go 编写的纯 CLI 协调者/执行者协作工具：协调者（人或 Claude Code/opencode/grok/codex 任一会话）写计划并 handoff dispatch 派发，执行者在独立会话与独立分支/worktree 中工作；危险操作在权限门被拦截并交回复审，状态由执行机的 agentd 常驻服务（SQLite）持久化，断线后两条命令接管。支持远程执行机（LAN/覆盖网络/云端中继，单一 WebSocket 直连），另含浏览器控制台（一次性 ticket 换 cookie 会话）与节点化看板工作流（dispatch/verdict/carry_card_context 等开关组合，版本不可变）。macOS/Linux/Windows 提供安装脚本二进制，也可 Go 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 执行与审阅分离：执行者独立会话/分支/worktree，权限门逐步放行
- agentd 常驻服务持久化状态（SQLite），断线/换机两条命令接管全量状态
- 远程执行机：LAN/覆盖网络/云端中继，单一直连 WebSocket，无中央服务器
- 为四类 agent 预装 handoff skill，AI 会话可驱动整个循环

## 适用场景

- 本地或远程把编码任务派发给 Claude Code/opencode/grok/codex 执行并审阅
- 笔记本写计划、派发到常驻工作站执行，代码经 git 往返
- 多会话依赖某任务归档时用 wait --until-done 阻塞等待
- 用节点化看板把派发、裁决、人工兜底组成流水线

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: handoff is a CLI-only, two-role collaboration tool. You — or any coding-agent session: Claude Code, opencode, grok,
> L22: - **Execution is separated from review**: the executor works in its own session, on its own branch (optionally its 
> L169: > When the coordinator is an AI session, none of this needs memorizing: installation

## 星数曲线

```mermaid
xychart-beta
    title "Xsxdot/handoff 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-28 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0a68d3738b2b` · [字段定义](../../DATASET.md)*
