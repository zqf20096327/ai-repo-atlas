# joansongjr/investor-harness

⭐ 27 · Shell · MIT · 推送 2026-09-06 · [GitHub](https://github.com/joansongjr/investor-harness) · 个人维护 · 中文 README

**面向二级市场投研人的跨 harness AI 技能规范集（34 个 skill）**

一套开源 MIT 协议的投研任务执行规范（prompt stack）：以 34 个 skill 文件约束 Claude Code / Codex / OpenCode / OpenClaw 等 AI agent 按投研纪律工作——取数前先列计划、每条事实标证据等级、输出归档到固定路径、跨会话断点接续。覆盖公司深度、业绩前瞻、Red Team、估值、行业地图、盯盘复盘、Librarian 记忆、语音监工、自主学习等场景，市场范围含 A 股 / 港股 / 美股 / 公募。安装后通过 onboarding 流程在 CLAUDE.md / AGENTS.md 追加路由块并搭建工作区骨架。

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

- 34 个 skill：公司深度、业绩前瞻、Red Team、估值、行业地图、Librarian 等
- 跨 harness 支持 Claude Code / Codex / OpenCode / OpenClaw，含关键词路由与 onboarding 流程
- 证据等级标注、仍需补的资料段、biases.md 偏差检查等纪律机制
- v0.9.7 起支持提问驱动的自主学习（规则可撤销回滚）

## 适用场景

- 让 AI agent 按可审计纪律产出 coverage 深度报告与业绩前瞻
- 对投资命题做带可观测触发的反方审视（Red Team）
- 维护覆盖池 wiki、每日 feed 与批量刷新等长期投研工作区

## 场景标签

`提示工程` `金融量化` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L52: **Investor Harness 是一套强制 AI 按投研工作纪律执行任务的开源规范**。
> L56: 跨平台开源（Claude Code / Codex / OpenCode / OpenClaw 全部支持），MIT 协议。

## 星数曲线

```mermaid
xychart-beta
    title "joansongjr/investor-harness 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-27 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `fd8d9873d7bc` · [字段定义](../../DATASET.md)*
