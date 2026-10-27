# armanzeroeight/fastagent-plugins

⭐ 29 · MIT · 推送 2026-07-27 · [GitHub](https://github.com/armanzeroeight/fastagent-plugins) · 个人维护

**Claude Code 插件集市：28 个面向开发/DevOps/云的子代理与技能包**

面向 Claude Code 用户的插件集合（marketplace），按 Essential/Role/Tech 三层组织 28 个插件，覆盖代码审查、测试、安全、文档以及 Docker、Terraform、Kubernetes、AWS/Azure/GCP 等技术栈。每个插件含策略层 agent、战术层 skill 与斜杠命令，agent 可自动委派 skill；采用按需安装与渐进式披露（SKILL.md 常驻、references 按需加载）以控制 token 消耗。安装依赖 Claude Code 的 /plugin 命令，支持团队配置自动分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 28 个插件按 Essential(6)/Tech(18)/Role(4) 三层组织
- agent(策略)→skill(战术)→command(快捷动作) 三层结构，支持自动委派
- 按需安装与渐进式披露设计以节省 token
- 通过 .claude/settings.json 支持团队自动安装插件

## 适用场景

- 为 Claude Code 添加 Terraform/K8s/云平台等专项开发技能
- 团队统一分发和启用编码助手插件
- 按当前技术栈挑选插件避免上下文膨胀

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L16: FastAgent is a curated collection of professional plugins for Claude Code that extend your AI coding assistant with
> L47: ### 1. Install Claude Code
> L49: Make sure you have Claude Code installed.

## 星数曲线

```mermaid
xychart-beta
    title "armanzeroeight/fastagent-plugins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `4c2fc63fe4b9` · [字段定义](../../DATASET.md)*
