# mario-andreschak/mcp-veo2

⭐ 34 · TypeScript · MIT · 推送 2026-09-24 · [GitHub](https://github.com/mario-andreschak/mcp-veo2) · 个人维护

**通过 MCP 调用 Google Veo/Gemini 生成视频与图片的服务器**

基于 Node.js 的 MCP 服务器，提供 7 个工具：文本/图片生成视频、生成图片、列出已生成媒体、按 UUID 获取图片等，输出 videos:// 与 images:// 资源链接。需 Google API key 才能生成，发现、模板与已存媒体访问无需 key。支持 stdio、Streamable HTTP（含 MCP 2026-07-28）与旧版 SSE（兼容 LibreChat 等客户端），HTTP 模式需静态 Bearer Token 鉴权。模型 ID 可配置（默认 veo-3.1 与 gemini-3.1-flash-image），限制：单次生成一个视频/图片、输入图片≤10 MiB、资源≤8 MiB，无自动重试付费请求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个 MCP 工具覆盖 Veo 视频生成与 Gemini 图片生成
- stdio / Streamable HTTP / 旧版 SSE 三种传输方式，Bearer Token 静态鉴权
- 模型 ID 可配置，输入支持 base64、MCP image 对象、HTTPS URL 与本地文件路径
- API key 仅在 header 中传输，不写入返回或保存的 URL

## 适用场景

- 在 MCP 客户端（如 Claude 类宿主）中直接调用 Veo/Gemini 生成视频与图片
- 通过 LibreChat 等旧版 SSE 客户端接入生成能力
- 检索与复用已生成媒体（列表、按 UUID 取回）

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L1: # Google Veo and Gemini image MCP server
> L3: Generate videos with Google Veo and images with Gemini. The package name remains
> L17: For an MCP host, launch **node directly** with the absolute `dist/index.js` path.

## 星数曲线

```mermaid
xychart-beta
    title "mario-andreschak/mcp-veo2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c674255a8824` · [字段定义](../../DATASET.md)*
