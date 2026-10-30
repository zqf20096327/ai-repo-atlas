# allemaar/open-skills

⭐ 15 · JavaScript · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/allemaar/open-skills) · [官网](https://allemaar.com) · 个人维护

**面向 AI 编程 agent 的个人技能包（70 个可读技能）**

个人维护、经实际工作使用的 agent 技能包：70 个技能均为可读 Markdown，其中 40 个附带可校验的声明式 YON 协议文件（protocol.yon，声明步骤、MUST/MUST_NOT 规则与 ABORT/WARN 门槛）。技能覆盖计划制定、调查取证、冷评审、输出综合、技能审计、agent 间通信（agent-mailbox）与知识地图（MYK）等。安装方式包括 git clone、Node 安装脚本 install.mjs 与 Claude Code 插件市场。README 明确说明：协议校验只证明结构有效，不强制运行时行为，不替代人工检查。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 70 个可读 Markdown 技能，其中 40 个带声明式 YON 协议
- install.mjs 单文件安装器（Node 内置模块，无本地 npm 依赖）
- agent-mailbox：基于共享文件夹的 append-only agent 间通信
- Map Your Knowledge（MYK）：使 markdown 文件夹可导航的协议族

## 适用场景

- 为 Claude Code / Codex 等 agent 添加计划、调查、评审等技能
- 安装前阅读并校验技能的协议声明
- 通过共享文件夹协调多个 agent 协作
- 整理和导航个人 markdown 知识库

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L4:  A personal, field-used pack of reusable skills for AI coding agents.
> L18: These skills came from repeated work with Claude Code, Codex, and other runtimes that read the open Agent Skills fo

## 星数曲线

```mermaid
xychart-beta
    title "allemaar/open-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `8ee0a60e955d` · [字段定义](../../DATASET.md)*
