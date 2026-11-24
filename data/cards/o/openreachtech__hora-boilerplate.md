# openreachtech/hora-boilerplate

⭐ 62 · JavaScript · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/openreachtech/hora-boilerplate) · [官网](https://openreach.tech/#hora) · 组织维护

**给开发者的 Claude Code 规格驱动 Web 应用模板**

一个模板仓库：不包含应用代码，而是承载规格文档与 /hora Claude Code 技能。运行时由 /hora 从 renchan 与 furo 模板克隆嵌套的前后端仓库，读取规格并逐功能实现，每个功能经过 18 个检查点（规格→后端→前端→验收）。/hora 可重入，中断后自行续跑，遇到未决问题会停下询问。要求 Claude Code、Node>=20.19、npm>=10 及 POSIX shell（Windows 需 WSL 2）。规格编写 /hora-spec 走七阶段对话，逐节经用户批准后写入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /hora 编排 5 个技能：spec/setup/plan/build/accept，规格驱动逐功能构建
- 每功能 18 个检查点，通过验收才进入下一功能
- /hora 可重入：自动判断上次中断位置并续跑，无人可答的问题写入 .hora/questions/
- 规格编写为七阶段对话，每节展示全文并经批准后写入一次

## 适用场景

- 从规格出发用 Claude Code 搭建全栈 Web 应用
- 把已有的 renchan/furo 项目纳入规格驱动工作流（as-built 或 to-spec）
- 以模板仓库方式初始化 <myproject>-app 项目骨架

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: A template repository for building an application from a spec, driven by the `/hora` Claude Code skill.
> L11: A project built from this template is made of several git repositories, nested inside one another. The outer reposi
> L148: `/hora` is an orchestrator. Five skills do the work:

## 星数曲线

```mermaid
xychart-beta
    title "openreachtech/hora-boilerplate 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-11-08 62 → 2026-11-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `02f2d9a3b699` · [字段定义](../../DATASET.md)*
