# jinzcdev/markmap-mcp-server

⭐ 290 · TypeScript · MIT · 推送 2026-08-04 · [GitHub](https://github.com/jinzcdev/markmap-mcp-server) · [官网](https://www.npmjs.com/package/@jinzcdev/markmap-mcp-server) · 个人维护 · 中文 README

**MCP 服务器：把 Markdown 转成可交互思维导图并导出图片**

基于 Model Context Protocol 的本地服务，向 MCP 客户端（Cursor / Claude Desktop 等）提供 4 个工具：将 Markdown（标题+嵌套列表）转换为可交互 HTML 思维导图，可选经 Playwright + Chromium 在服务端导出 PNG/JPG/SVG，另有列出、读取、清理生成文件的工具及结构化提示词。转换全程本地运行，无需第三方 API key。返回模式（路径/内联内容/两者）、浏览器打开行为、输出目录等在启动时经 CLI/环境变量配置；大于等于 200KB 的内联 HTML 回退为路径返回。需 Node.js v20 以上，图像导出依赖 Playwright（可选）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown → 可交互 HTML 思维导图，服务端可导出 PNG/JPG/SVG
- 4 个 MCP 工具：生成、列出、读取、清理（含路径穿越防护）
- 完全本地生成，无需第三方 API key
- 返回模式与浏览器行为等启动期配置（CLI/环境变量）

## 适用场景

- 让 Agent 把设计文档或笔记整理成思维导图
- 在对话中直接获取 PNG 思维导图用于预览
- 离线环境下生成自包含 HTML 导图（--offline 内联资源）

## 场景标签

 · 领域:开发者工具/文档可视化

## 证据(README 行号)

> L11: Markmap MCP Server is based on the Model Context Protocol (MCP). It converts Markdown into interactive mind maps us
> L68: Add the following configuration to your MCP client (Cursor / Claude Desktop / etc.):
> L110: ### `markdown_to_mindmap`

## 星数曲线

```mermaid
xychart-beta
    title "jinzcdev/markmap-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 288 --> 291
    line [289, 290, 290]
```

2026-10-18 289 → 2026-10-28 290（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a609aea00f7d` · [字段定义](../../DATASET.md)*
