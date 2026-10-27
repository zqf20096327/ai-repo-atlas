# Dwsy/agent

⭐ 24 · TypeScript · 推送 2026-09-21 · [GitHub](https://github.com/Dwsy/agent) · [官网](https://dwsy.github.io/agent/) · 个人维护 · 中文 README

**面向软件开发的自主 AI 编排系统（monorepo：网关+技能+子代理）**

Pi Agent 是一个 monorepo 形态的 AI 编码代理系统，包含代理核心、单端口 HTTP+WS 多通道网关（Telegram/Discord/WebChat）、40+ 技能（SKILL.md 注入系统提示词）、30+ 运行时扩展与 20+ 子代理。核心为 5 阶段工作流：上下文检索→分析→原型（Unified Diff）→实现→审计，采用 Claude/Gemini 多模型分工路由。设计上强调沙箱安全（外部模型不可直接写文件）与 SSOT 文档原则。需 Bun>=1.1.0，通过 git clone 子模块与逐目录 bun install 组装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 阶段工作流：检索→分析→原型→实现→审计，多模型分工路由
- 单端口网关接入 Telegram/Discord/WebChat，RPC 进程池与插件生命周期钩子
- 40+ SKILL.md 技能、30+ 扩展、20+ 子代理的插件化架构
- 沙箱安全：外部模型仅输出 Unified Diff，修改需人工介入

## 适用场景

- 通过 Telegram/Discord/WebChat 多通道驱动 AI 编码代理
- 用 /scout、/analyze 等命令做代码侦察、分析与多代理协作
- 以技能/扩展/子代理插件机制扩展代理能力

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: Pi Agent is an autonomous AI orchestrator for software development — a monorepo containing the agent core, a multi-c
> L12: - **Multi-Model Orchestration**: Claude, Gemini, and specialized tool routing
> L195: |4. Implementation|Mandatory|Claude|Production code, minimal scope|

## 星数曲线

```mermaid
xychart-beta
    title "Dwsy/agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `529c5ca8b836` · [字段定义](../../DATASET.md)*
