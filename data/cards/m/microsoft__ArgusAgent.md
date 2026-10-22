# microsoft/ArgusAgent

⭐ 142 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/microsoft/ArgusAgent) · [官网](https://argusbot.cn) · 组织维护 · 中文 README

**面向长周期研究与工程的多智能体持久运行时**

Argus 是一个由 Manager/Planner/Engineer/Reviewer 四角色分工的多智能体运行时：Manager 管理阶段流转，Planner 规划任务与验证证据，Engineer 执行实现与实验，Reviewer 只读裁决并可返回 blocked。系统复用已认证的 Agent CLI（GitHub Copilot CLI、OpenAI Codex CLI、Claude Code、Cursor CLI、Pi、OpenCode、Grok Build、Qoder、DeepSeek Harness）作为执行后端，无需单独账号。面向需要跨多个模型回合持续推进并带审查机制的研究与工程任务的开发者/科研用户。安装需 Python 3.11+ 与 Node.js 22.12+，Windows 提供桌面 EXE 渠道，源码分支从 GitHub 安装而非 PyPI；提供 arXiv 技术报告与微信社区。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Manager/Planner/Engineer/Reviewer 四角色分工，Reviewer 只读运行
- 复用 9 种已认证 Agent CLI 作为原生后端，无需单独账号
- 凭据、支付、不可逆操作与发布始终暂停等待人类确认
- Skills 与 Wiki 发现按 project→vertical→global 作用域累积，无需再训练

## 适用场景

- 让长周期研究或工程项目在无人值守时持续推进并自动审查
- 在多个已有 Agent CLI 后端之上统一调度与分配任务
- 跨模型回合的任务暂停、恢复与验证管理

## 场景标签

`多智能体` `编码 Agent` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L37: **Argus takes the Driver's seat**, splitting it across four roles deliberately not allowed
> L60: **Native backends:** `GitHub Copilot CLI` · `Pi` · `OpenAI Codex CLI` · `Claude Code` · `Cursor CLI` · `OpenCode` ·
> L68: Argus remains the Driver for scheduling, role assignment, and task lifecycle;

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/ArgusAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 139 --> 141
    line [140, 140]
```

2026-10-18 140 → 2026-10-22 140（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `91adb247a16f` · [字段定义](../../DATASET.md)*
