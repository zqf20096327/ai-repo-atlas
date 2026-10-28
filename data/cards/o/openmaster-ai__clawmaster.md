# openmaster-ai/clawmaster

⭐ 19 · TypeScript · NOASSERTION · 推送 2026-07-28 · [GitHub](https://github.com/openmaster-ai/clawmaster) · 组织维护 · 中文 README

**OpenClaw 的安装配置与管理控制台，面向日常可用**

ClawMaster 是 OpenClaw 引擎的配套管理工具：提供 CLI 与 Web 控制台（含安装向导、运行时健康总览、多模型 Provider 配置与密钥校验、6 个消息渠道接入引导、基于 ClawProbe 的成本/Token/会话观测、MCP 服务器与技能市场管理），并集成 PowerMem 记忆运行时（seekdb 或 SQLite 回退），支持按用户/agent/工作区隔离。另有 Tauri 桌面应用（beta）。适合想让 OpenClaw 在团队或家庭日常使用的用户，要求 Node.js 20+。当前 v0.3.1，采用 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CLI + Web 控制台：安装向导自动检测 OpenClaw 引擎并配置 LLM Provider
- 基于 ClawProbe 的成本、Token 与会话健康观测
- PowerMem 记忆运行时，seekdb 向量+全文+SQL 混合检索，SQLite 回退
- 技能市场 ClawHub 与 MCP 服务器管理

## 适用场景

- 非技术用户通过向导完成 OpenClaw 安装与模型配置，无需编辑 JSON
- 团队/家庭统一管理 OpenClaw 的渠道、运行状态与成员接入
- 查看 agent 会话成本、Token 消耗与运行时健康

## 场景标签

`LLM 可观测性` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L39: Open http://localhost:16223 — the setup wizard walks you through OpenClaw engine detection and LLM provider configu
> L80: 3. Add channels, plugins, skills, or MCP servers as needed.
> L90: Most OpenClaw tooling stops at configuration. ClawMaster is your **OpenClaw companion for real life** — a bridge be

## 星数曲线

```mermaid
xychart-beta
    title "openmaster-ai/clawmaster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ac42ca7842a4` · [字段定义](../../DATASET.md)*
