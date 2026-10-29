# Brain2k-0005/Lumeo

⭐ 22 · C# · MIT · 推送 2026-10-05 · [GitHub](https://github.com/Brain2k-0005/Lumeo) · [官网](https://lumeo.nativ.sh/) · 个人维护

**shadcn 风格的 Blazor 无障碍 UI 组件库（169 个组件）**

面向 Blazor WASM/Server 开发者的 MIT 许可 UI 组件库，提供 169 个组件：DataGrid、Scheduler、Gantt、30+ ECharts 图表、表单源生成器、8 主题与暗色模式、14 语言含 RTL、触摸手势等。采用核心包+可选卫星包的 NuGet 分发模型，另提供 Lumeo.Cli 将组件源码 vendor 到自己仓库（lumeo eject 可完全脱离 NuGet）。AI 相关部分：PromptInput/StreamingText 等 AI 聊天原语组件，以及为 LLM 代码生成服务的 MCP server（13 个工具）和 Agent Skill。需 .NET 8+，9,100+ 测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 169 个组件，支持 NuGet 引用或 CLI 源码 vendor 两种使用方式
- AI 聊天原语组件：PromptInput、StreamingText、AgentMessageList、ToolCallCard、ReasoningDisplay
- @lumeo-ui/mcp-server 提供 13 个工具辅助 LLM 生成正确的 Lumeo 标记
- 9,100+ 测试、14 语言 + RTL、WCAG 2.5.5 44×44px 触控目标

## 适用场景

- 在 Blazor 项目中搭建带 DataGrid/图表/Scheduler 的管理界面
- 快速构建 AI 聊天类界面的流式输出与消息列表
- 通过 CLI 把组件源码复制进项目做深度定制

## 场景标签

 · 领域:前端开发/UI 组件

## 证据(README 行号)

> L3: **169 accessible Blazor components, AI-ready, motion-integrated, shadcn-inspired.**
> L34: - **AI primitives** — `PromptInput`, `StreamingText`, `AgentMessageList`, `ToolCallCard`, `ReasoningDisplay`

## 星数曲线

```mermaid
xychart-beta
    title "Brain2k-0005/Lumeo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2b44ba5986b0` · [字段定义](../../DATASET.md)*
