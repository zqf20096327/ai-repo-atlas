# pingta-guangpingwang/claude-harness-desktop

⭐ 29 · TypeScript · 推送 2026-05-31 · [GitHub](https://github.com/pingta-guangpingwang/claude-harness-desktop) · 个人维护 · 中文 README

**指挥多个 Claude Code 实例协同的 Electron 桌面驾驶舱**

基于 Electron 28 + React 19 的多项目管理驾驶舱：通过 node-pty 多终端并行运行多个 Claude Code 实例，内置 LLM 驾驭智能体负责任务拆解、角色分配、进度监督与报告汇总；提供 CEO/Worker/Reviewer/Diagnostician 四角色体系、六步上下文管线、三层记忆与 Token 预算管理、20+ 插件商店、可视化工作流编辑器和三仓库资源市场（深蓝工坊）。AI 引擎为 Claude Code CLI + DeepSeek API。要求 Windows 10/11、Node.js 22+、Claude Code CLI，通过 git clone 源码方式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条指令并行指挥多个 Claude Code 实例，AI 驾驭智能体自动拆解与监督
- 四角色体系与工具权限、评分追踪、自定义角色
- 六步上下文管线 + 三层记忆存储 + Token 预算管理（1M 上下文）+ HITL
- 20+ 插件商店、14 种节点可视化工作流编辑器、三仓库资源市场

## 适用场景

- 同时推进多个项目的 AI 编码任务并统一监控
- 通过广播指令批量调度在线项目
- 用工作流编辑器搭建跨项目自动化管线

## 场景标签

`Agent 框架` `多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L15: - **🤖 AI 驾驭智能体** — 内置 LLM Agent，自动拆解任务、匹配角色、并行分配、监督进度、汇总报告。你只管下指令，它替你指挥舰队
> L45: |AI 引擎|Claude Code CLI + DeepSeek API (1M 上下文)|

## 星数曲线

```mermaid
xychart-beta
    title "pingta-guangpingwang/claude-harness-desktop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f9bf79f9ce02` · [字段定义](../../DATASET.md)*
