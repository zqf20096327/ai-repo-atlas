# RyanKramer/pixelpanda-mcp

⭐ 21 · Python · 推送 2026-08-27 · [GitHub](https://github.com/RyanKramer/pixelpanda-mcp) · [官网](https://pypi.org/project/pixelpanda-mcp/) · 个人维护

**为 MCP 客户端提供 38 个图像处理工具的 PixelPanda 服务端**

基于 Model Context Protocol 的图像工具服务端，面向 Claude Desktop、Cursor、VS Code 等 MCP 客户端用户。分三层提供 38 个工具：本地免费工具（缩放/裁剪/水印等，离线运行基于 Pillow）、AI 工具（抠图、Real-ESRGAN 放大、OCR 除水印、图像分析，每日免费 3 次）、付费 Pro 工具（商品图生成、试穿、文生图编辑、Grok Imagine 视频生成，按 credit 计费，需 API token）。通过 uvx 或 pip 安装，本地与免费工具无需账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 38 个工具分三层：本地免费 / AI 免费（3 次/天）/ Pro 按积分付费
- 本地工具离线运行，无需账号与 API token
- AI 能力含背景移除、Real-ESRGAN 放大、FLUX Kontext 文生图编辑、Grok Imagine 视频生成
- 支持 Claude Desktop、Cursor、VS Code 等 MCP 客户端接入

## 适用场景

- 在 Claude 或 Cursor 中直接对图片做裁剪、压缩、加水印等处理
- 对话式生成商品图、模特试穿与产品场景图
- 批量去除图片背景或文字水印并放大图片

## 场景标签

`图像视频处理` `图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L1: # PixelPanda MCP Server
> L3: AI image processing tools for Claude Desktop, Cursor, VS Code, and other MCP-compatible clients.

## 星数曲线

```mermaid
xychart-beta
    title "RyanKramer/pixelpanda-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b371db97dfe7` · [字段定义](../../DATASET.md)*
