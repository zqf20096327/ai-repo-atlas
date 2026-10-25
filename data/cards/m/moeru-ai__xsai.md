# moeru-ai/xsai

⭐ 664 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/moeru-ai/xsai) · [官网](https://xsai.js.org) · 组织维护

**面向 Web 标准的极小型 TypeScript AI SDK**

xsAI 是一个按协议适配的 TypeScript AI SDK：不为每个服务商发单独包，而是为 OpenAI Responses、Chat Completions、Anthropic Messages 三种协议各提供一个适配器，工厂函数返回统一的 LanguageModel，generateText/streamText/工具调用对各协议行为一致。全部包为无副作用 ES 模块，基于 fetch/ReadableStream/AbortSignal 等 Web 标准，可在 Node.js、Deno、Bun、Cloudflare Workers 与浏览器运行。提供文本、语音、嵌入、图像生成等分包，可按需安装或整体安装。

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

- 按协议而非服务商提供适配器，三种协议返回统一 LanguageModel
- 全包为无副作用 ES 模块，摇树优化按需保留代码
- 仅依赖 fetch/ReadableStream 等 Web 标准，多运行时可用
- 分包覆盖文本、语音生成与转录、嵌入、图像生成、评分决策

## 适用场景

- 在前端或边缘运行时中以统一接口调用不同 LLM 服务
- 构建需要摇树优化的小体积 AI 应用
- 更换模型服务时保持业务代码不变

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L41: - **A model belongs to a protocol, not to a provider.** One adapter covers every service that speaks the same proto
> L47: xsAI does not ship a package for each provider. It ships an adapter for each protocol, and many services and gatewa
> L75: xsAI runs on any runtime with `fetch` and web streams: Node.js, Deno, Bun, Cloudflare Workers, and browsers.

## 星数曲线

```mermaid
xychart-beta
    title "moeru-ai/xsai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 663 --> 665
    line [664, 664]
```

2026-10-18 664 → 2026-10-25 664（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0ec3a1b38cac` · [字段定义](../../DATASET.md)*
