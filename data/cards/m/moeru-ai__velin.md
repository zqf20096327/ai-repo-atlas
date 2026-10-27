# moeru-ai/velin

⭐ 78 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/moeru-ai/velin) · [官网](https://velin.dev) · 组织维护

**用 Vue/React 组件开发与编排 LLM 提示词的库**

面向在 Node.js 或浏览器运行时开发 agent 与 MCP 服务器提示词的开发者：用 Vue SFC、React 组件、TSX/JSX 源或 Markdown 编写提示词，替代自造模板 DSL；支持 Vue 模板指令（v-if 等）与 Node.js/浏览器双端入口。提供 defineTool 将组件属性推导为参数 schema，使同一组件可作为 LLM 工具交给模型调用，并可与 OpenAI SDK、@xsai 等配合。Svelte 支持标注为进行中；componentFromSource 非沙箱，仅限受信源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 Vue SFC / React 组件 / TSX / Markdown 编写提示词
- 兼容任意 Node.js/浏览器运行时
- defineTool 从组件 props 推导参数 schema，组件可交给模型作为工具
- Vue/React 支持，Svelte 进行中

## 适用场景

- 用熟悉的 Vue/React 写法替代模板 DSL 编写提示词
- 开发 agent 与 MCP 服务器的提示词与工具
- 将提示词组件直接注册为 LLM 可调用工具

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: > Have you wondered how it feels if you can develop the prompts of agents and MCP servers with the power of Vue or 
> L131: A prompt component is already most of a tool: its props are the arguments, its script does the work, and what it r

## 星数曲线

```mermaid
xychart-beta
    title "moeru-ai/velin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-27 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `50fcdf9a5862` · [字段定义](../../DATASET.md)*
