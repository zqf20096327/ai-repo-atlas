# Marssssss/OneAI

⭐ 41 · Rust · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/Marssssss/OneAI) · 个人维护 · 中文 README

**Rust 跨平台 AI Agent 框架，一套引擎驱动六类官方前端**

基于 Rust（edition 2021，33 个 crate）的跨平台 AI Agent 框架：统一引擎经 Directive/EngineYield 协议对接多种官方前端——WebUI、CLI/TUI、macOS App（SwiftUI）、Windows App（WinUI 3）、VS Code 扩展、浏览器扩展、Android App，iOS/HarmonyOS 在建。引擎特性含动态 AgentLoop、7 层声明式 DomainPack、多角色 GroupChat 预设、ProviderPool 降级链与限流熔断。npm 安装可拉预编译二进制零 Rust 使用，各原生 App 需源码构建。面向做 Agentic 编程与场景化对话的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一引擎总线：一套 Directive/EngineYield 协议供全部前端共用
- 动态 AgentLoop：每轮模型决策直接回答/工具调用/委托子 Agent/切换范式
- DomainPack 7 层声明式配置，一行切换领域
- ProviderPool 降级链 + SmartRouter + 限流/熔断/429 重试

## 适用场景

- 在终端、编辑器或浏览器等多端复用同一套 Agent 引擎
- 通过场景预设（面试演练/辩论赛等）开箱做多角色对话
- 用 CLI/TUI 做通用 Agentic 编程与任务执行

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: > **One AI, Every Platform** —— 跨平台 AI Agent 框架，基于 Rust。一套引擎喂六端前端。
> L24: - **多类官方前端** —— WebUI、CLI/TUI、macOS / Windows App、VS Code 扩展、浏览器扩展、移动 App，一套引擎喂全端，各端用各端的原生 UI。
> L26: - **动态 AgentLoop** —— 每轮模型动态决策（直接回答 / 工具调用 / 委托子 Agent / 切换范式），迭代上限由 Token 预算约束。

## 星数曲线

```mermaid
xychart-beta
    title "Marssssss/OneAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-29 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `da268d2619db` · [字段定义](../../DATASET.md)*
