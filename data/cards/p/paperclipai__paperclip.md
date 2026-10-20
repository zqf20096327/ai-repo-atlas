# paperclipai/paperclip

⭐ 103,990 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/paperclipai/paperclip) · [官网](https://paperclip.ing) · 组织维护

**给团队的 AI 代理编排控制台：目标、预算、治理一体化**

一个 Node.js 服务器加 React UI，用于编排一组 AI 代理执行业务工作：用户定义目标、按角色组建代理团队（org chart）、审批与运行任务，并在仪表板中跟踪工作与成本。核心机制包括心跳唤醒、原子任务领取与执行锁、预算阈值与硬停、审批门与配置回滚、技能注入与定时例程。可接入多种代理运行时（Claude Code、Codex、Cursor、Gemini CLI 等），支持多组织隔离与模板导出导入。面向需要协调多个代理并控制成本与权限的团队。

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

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 29,217 位贡献者
- 涨星:近 1 天 **+610**(自 20261016 起算)
- 安装:npm 包 `paperclipai@latest` 月下载无数据
- 平台:— · 协议:MCP

## 能力要点

- 跨运行时接入任意代理：能接收心跳即可入编（适配器/HTTP/自定义进程扩展）
- 组织级治理：审批门、权限边界、配置版本化与回滚
- 预算与成本控制：按公司/代理/项目维度跟踪花费、阈值告警、硬停
- 任务系统：原子任务领取、阻塞依赖、会话持久化、定时例程（cron/webhook/API 触发）

## 适用场景

- 把多个编码/办公代理组编成一个有角色和汇报线的虚拟团队
- 给代理团队设预算并自动在超限时暂停工作
- 用定时例程代替手动触发重复性代理任务
- 从手机或仪表板审批、审计 24/7 自主运行的代理工作

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L23: Open-source orchestration for teams of AI agents.
> L27: Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business. Bring your own 
> L77: |**Agentic OS** — The infrastructure that makes the work run.|IT & platform|Cross-provider runtime: any model, any 

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `a4e05af0e979` · [字段定义](../../DATASET.md)*
