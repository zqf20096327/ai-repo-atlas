# RedHat-UX/next-gen-ui-agent

⭐ 27 · Python · Apache-2.0 · 推送 2026-03-18 · [GitHub](https://github.com/RedHat-UX/next-gen-ui-agent) · [官网](https://redhat-ux.github.io/next-gen-ui-agent/) · 组织维护

**为 AI 助手生成个性化富 UI 组件（卡片/表格/图表等）的 agent**

以 Python/TypeScript 模块形式提供的生成式 UI agent：根据用户提示、聊天历史和其他 agent 提供的后端数据，输出结构化的 UI 组件定义（如 video-player、card、table、chart），可在服务端渲染 web component 或客户端以 React/PatternFly 渲染。面向在自有 AI 应用中集成富 UI 的开发者，支持 LangGraph、Llama Stack、BeeAI 框架接入及 MCP、A2A 协议，可自插自定义组件。README 标注 UI 状态维护等功能为未来计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按提示/聊天历史/后端数据生成富 UI 组件（card、table、chart、video-player 等）
- 支持接入 LangGraph、Llama Stack、BeeAI（Tech Preview）三种 AI 框架
- 提供 MCP 与 A2A 协议模块及容器镜像运行方式
- 服务端 web component 渲染与客户端 React/PatternFly 渲染两种模式

## 适用场景

- 为自己的 LLM 助手扩展文本之外的富 GUI 输出
- 通过 MCP/A2A 协议把 UI 渲染作为服务接入多 agent 系统
- 用自有 UI 组件库替换默认渲染组件

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: The goal of this AI agent is to generate personalised and rich UI components based on
> L13: * `Extensible architecture` - Developer's choice to which AI framework to plug and which UI component framework to 
> L57: 1. LangGraph

## 星数曲线

```mermaid
xychart-beta
    title "RedHat-UX/next-gen-ui-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `10280ad9cab7` · [字段定义](../../DATASET.md)*
