# Shijou87/Brow

⭐ 20 · JavaScript · Apache-2.0 · 推送 2026-05-18 · [GitHub](https://github.com/Shijou87/Brow) · 个人维护

**实验性 Chrome 侧面板 AI 浏览器代理，供构建者做语义化浏览器自动化**

Brow 是一个开源的 Manifest V3 Chrome 扩展，以侧面板形式运行基于 LangGraph.js 的 AI agent，直接在用户的真实 Chrome 会话中操作网页。它通过 Browser Snapshots、表单语义与结构化 ref 提供语义化浏览器上下文，汇聚内置浏览器工具、页面级 WebMCP 工具与远程 MCP 服务器工具三类工具，支持 OpenAI 兼容 API 配置模型（可选 VLM 端点、本地模型），并提供工作流演示、技能与领域记忆。当前为实验状态，需以开发者模式加载未打包扩展，自行构建运行，面向构建者与早期采用者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 在用户真实 Chrome 会话中运行的侧面板 AI agent（Manifest V3 扩展）
- 基于 ref 的 Browser Snapshots 与整表单语义快照
- 聚合内置工具、页面级 WebMCP 工具与远程 MCP 服务器工具
- OpenAI 兼容端点配置，支持本地模型与 VLM 端点

## 适用场景

- 在真实浏览器会话中让 AI agent 执行语义化网页操作与表单批处理
- 通过 MCP/WebMCP 接入页面级与远程工具做浏览器自动化
- 作为浏览器 agent 框架进行二次开发与贡献

## 场景标签

`浏览器自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Brow is an experimental Chrome side-panel AI browser agent for builders who want LangGraph.js , MCP , WebMCP , and 
> L17: - It runs inside the user's live Chrome session instead of spinning up a detached automation browser.
> L19: - It combines three tool worlds in one side panel: built-in browser tools, page-local **WebMCP** tools, and remote 

## 星数曲线

```mermaid
xychart-beta
    title "Shijou87/Brow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-30 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `47709e12564b` · [字段定义](../../DATASET.md)*
