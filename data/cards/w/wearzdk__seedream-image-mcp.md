# wearzdk/seedream-image-mcp

⭐ 18 · TypeScript · MIT · 推送 2025-12-06 · [GitHub](https://github.com/wearzdk/seedream-image-mcp) · [官网](https://mcp.pixelark.art/) · 个人维护 · 中文 README

**调用火山引擎 SeeDream 模型生图的 MCP 服务器，供 Cursor/Claude 使用**

基于 MCP 协议的图片生成工具服务器：接入火山引擎 SeeDream 4.0 模型，在 Cursor、Claude Desktop 等支持 MCP 的客户端中以工具形式提供文生图能力，支持自定义尺寸与参考图，由 AI 自动生成生图提示词。用户需自行申请火山引擎 API Key 并通过 npx 本地运行，另提供付费云端版本（免 API key、CDN 永久存储）。限制：本地方式生成的图片链接约 24 小时失效，需及时下载保存。开发使用 Bun。

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

- 接入火山引擎 SeeDream 4.0 模型生成图片
- MCP 协议接入 Cursor、Claude Desktop 等客户端
- AI 自动根据需求生成生图提示词，无需手写复杂提示词
- 提供云端版本（免 API key、图片 CDN 永久存储）

## 适用场景

- 在 Cursor/Claude Code 中让 AI 自动为页面配图
- 通过 MCP 客户端用自然语言生成图片
- 需要快速并发生成多张图片时使用云端版本

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: 基于火山引擎 SeeDream 模型的 MCP (Model Context Protocol) 图片生成工具。
> L10: - 🔌 MCP 协议支持，可在 Cursor、Claude Desktop 等客户端中使用

## 星数曲线

```mermaid
xychart-beta
    title "wearzdk/seedream-image-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `aad371c8d8ae` · [字段定义](../../DATASET.md)*
