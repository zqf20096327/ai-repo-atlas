# hypermemory-ai/hypermemory-sdk

⭐ 14 · TypeScript · MIT · 推送 2026-05-14 · [GitHub](https://github.com/hypermemory-ai/hypermemory-sdk) · [官网](https://www.hypermemory.io) · 组织维护

**HyperMemory 长期记忆平台的 TypeScript SDK**

面向 HyperMemory 托管平台的官方 TypeScript 客户端 SDK，含四个包：core 客户端（store/recall/update/forget/ingest/findRelated 等方法）、可视化核心（Cosmograph 2D + Three.js 3D 查看器）、React 18+ 与 Svelte 5 框架绑定。知识以节点-关系-超边图组织，recall() 基于向量相似性做语义检索，findRelated() 做图遍历。所有调用需 hm_* API key 访问 api.hypermemory.io，按套餐限流；框架组件仅客户端渲染，Node.js >= 18 且需原生 fetch。

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

- store/recall/ingest/findRelated 等图记忆操作客户端
- Cosmograph 2D 与 Three.js 3D 图可视化组件
- React/Svelte 框架绑定与无框架 Vanilla JS 使用方式
- 同一 hm_* key 可用于 MCP 服务端点供 AI agent 接入

## 适用场景

- 为 AI agent 应用构建跨会话的长期记忆层
- 在 React/Svelte 应用中可视化展示知识图谱
- 通过 ingest 将非结构化文本解析为图节点

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L3: Official TypeScript SDK for the HyperMemory agentic long-term memory platform. Store, recall, traverse, and visualiz
> L233: The HyperMemory MCP server at `POST https://api.hypermemory.io/mcp` accepts the same `hm_*` Bearer token. This mea

## 星数曲线

```mermaid
xychart-beta
    title "hypermemory-ai/hypermemory-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `58ebc230b188` · [字段定义](../../DATASET.md)*
