# ArtificialAnalysis/StirrupJS

⭐ 23 · HTML · MIT · 推送 2026-06-21 · [GitHub](https://github.com/ArtificialAnalysis/StirrupJS) · [官网](https://stirrupjs.artificialanalysis.ai) · 组织维护

**TypeScript 轻量级 agent 构建框架（Python Stirrup 的 TS 实现）**

用于在 TypeScript/JavaScript 中构建 agent 的轻量框架或起始模板，可作 npm 包使用或克隆为自定义基础。内置在线搜索/网页抓取、代码执行（本地/Docker/E2B 沙箱）、MCP 客户端、Zod 类型安全工具定义、human-in-the-loop 输入工具、上下文自动摘要去重、多模态输入、运行缓存与恢复、速度指标与事件监控等。预置 OpenAI 兼容（Chat Completions 与 Responses API）、Anthropic、Vercel AI SDK 客户端。是 Python Stirrup 框架的 TypeScript 实现，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预置 OpenAI 兼容/Anthropic/Vercel AI SDK 多客户端支持
- 代码执行支持本地、Docker 与 E2B 沙箱三种环境
- 上下文接近上限时自动摘要并去重，防止摘要累积
- agent 运行状态缓存至 ~/.cache/stirrup/ 并可从断点恢复

## 适用场景

- 在 TypeScript 项目中快速搭建自定义 agent
- 通过 MCP 客户端连接外部工具服务器扩展 agent 能力
- 克隆为起始模板构建完全定制化的 agent 应用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: Stirrup is a lightweight framework, or starting point template, for building agents in TypeScript/JavaScript. It dif
> L26: - 🔁 **Flexible provider support:** Pre-built support for OpenAI-compatible APIs (Chat Completions + Responses API),
> L67: - **`Agent`** - Configures and runs the agent loop until a finish tool is called or max turns reached

## 星数曲线

```mermaid
xychart-beta
    title "ArtificialAnalysis/StirrupJS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `eb7331cb210c` · [字段定义](../../DATASET.md)*
