# attalla1/photopea-mcp-server

⭐ 45 · TypeScript · MIT · 推送 2026-04-05 · [GitHub](https://github.com/attalla1/photopea-mcp-server) · 个人维护

**让 AI agent 通过 MCP 操控 Photopea 编辑图片的 TypeScript 服务器**

基于 Model Context Protocol 的服务器，把 AI agent 的编辑指令翻译为 Photopea JavaScript API 调用，经 WebSocket 桥接到浏览器中运行的 Photopea（iframe 内），实现海报设计、照片调整、图层管理、文字形状添加与图片导出等 34 个工具操作。面向使用 Claude Code、Claude Desktop、Cursor、Copilot、Windsurf 等 MCP 客户端的开发者。限制：需 Node.js ≥18 与现代浏览器，仅支持单浏览器标签页，刷新页面会丢失未保存工作，reorder_layer 等操作可能使 UI 短暂无响应。

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

- 34 个 MCP 工具覆盖文档、图层、文字形状、图像效果与导出（PNG/JPG/WebP/PSD/SVG）
- Agent↔MCP(stdio)↔WebSocket↔浏览器 Photopea 的四组件架构
- 提供 Claude Code/Claude Desktop/Cursor/Copilot/Windsurf 的配置方式，支持 npx 一键接入
- photopea_run_script 可执行任意 Photopea JavaScript（标记为破坏性、需用户批准）

## 适用场景

- 用自然语言让 agent 生成海报并导出为 PNG
- 批量对照片做亮度、模糊、锐化等调整后导出
- 在终端 AI 助手中合成多图层图片

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L24:     A[Agent] <-->|stdio| B[MCP Server]
> L29: Your agent sends editing commands through the MCP protocol. The server translates these into Photopea JavaScript AP
> L201: **MCP Server** (`src/server.ts`) -- Registers all 34 tools with the MCP SDK and connects via stdio transport.

## 星数曲线

```mermaid
xychart-beta
    title "attalla1/photopea-mcp-server 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26", "2026-10-27"]
    y-axis "stars" 42 --> 46
    line [43, 44, 45, 45]
```

2026-10-18 43 → 2026-10-27 45（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6d47dbec1883` · [字段定义](../../DATASET.md)*
