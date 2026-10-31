# MiniMax-AI/MiniMax-Coding-Plan-MCP

⭐ 101 · Python · MIT · 推送 2026-08-20 · [GitHub](https://github.com/MiniMax-AI/MiniMax-Coding-Plan-MCP) · [官网](https://www.minimax.io/platform) · 组织维护 · 中文 README

**面向编码用户的 MiniMax MCP 服务器：网页搜索与图像理解工具**

MiniMax 官方维护的专用 Model Context Protocol (MCP) 服务器，面向 coding-plan 订阅用户，提供 web_search 与 understand_image 两个 API 工具，可集成到 Claude Desktop、Cursor、Windsurf、OpenAI Agents 等 MCP 客户端。支持 stdio 与 SSE 两种传输方式，stdio 本地运行可处理本地文件或 URL，SSE 可云端部署。使用需 MiniMax API key，且 API host 与 key 须按区域（Global/Mainland）匹配，否则报 invalid api key 错误。通过 uv 安装运行，图像分析支持 JPEG、PNG、WebP。

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

- web_search 返回有机搜索结果与相关查询
- understand_image 基于文本提示分析图像（JPEG/PNG/WebP）
- 支持 stdio 与 SSE 两种传输，可本地或云端部署
- 兼容 Claude Desktop、Cursor、Windsurf 等 MCP 客户端

## 适用场景

- 在编码 IDE 中通过 MCP 客户端调用 MiniMax 网页搜索
- 对设计图或截图做图像理解辅助开发
- coding-plan 用户以订阅额度使用这些工具（可能产生费用）

## 场景标签

`网页抓取` `图像视频处理` · 领域:效率与自动化

## 证据(README 行号)

> L30:  Specialized MiniMax Model Context Protocol (MCP) server designed for coding-plan users, featuring AI-powered searc
> L65: ## Transport
> L73: ## Available Tools

## 星数曲线

```mermaid
xychart-beta
    title "MiniMax-AI/MiniMax-Coding-Plan-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-31 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3a1bc00344cb` · [字段定义](../../DATASET.md)*
