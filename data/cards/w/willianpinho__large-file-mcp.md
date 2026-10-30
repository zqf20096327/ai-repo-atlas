# willianpinho/large-file-mcp

⭐ 18 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/willianpinho/large-file-mcp) · [官网](https://large-file-mcp.dev.willianpinho.com) · 个人维护

**给 AI 客户端处理大文件的 MCP 服务器：分块/搜索/流式读取**

TypeScript 编写的 MCP 服务器，向 Claude Code、Claude Desktop、Cursor、Gemini CLI 等 AI 客户端提供 6 个大文件操作工具：按文件类型自适应分块读取、带上下文的正则搜索、跳转指定行、文件结构与统计摘要、按字节偏移流式读取。流式架构逐行读取不整载入内存，支持 LRU 缓存与 TTL 过期，分块大小/缓存/最大文件尺寸（默认 10GB 上限）经环境变量配置。经 npm 全局安装或 npx 直接运行，源码构建用 pnpm。

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

- 按文件类型自适应分块（文本 500 行/代码 300 行/CSV 1000 行等）
- 流式逐行读取，不将文件整体载入内存
- LRU 缓存（默认 100MB、TTL 5 分钟）加速重复访问
- 6 个工具：分块读取/正则搜索/行导航/结构分析/摘要/流式处理

## 适用场景

- 让 AI 客户端搜索和分析多 GB 日志文件
- 在不整载入内存的前提下读取大型 CSV/JSON 数据
- 在大代码库中按行导航与定位函数定义

## 场景标签

 · 领域:AI 客户端工具/文件处理

## 证据(README 行号)

> L3: MCP server for intelligent handling of large files — smart chunking, search, navigation, and streaming.
> L414: Compatible with Claude Code, Cursor, and Gemini CLI. Available on npm and the Glama.ai registry, and listed in com

## 星数曲线

```mermaid
xychart-beta
    title "willianpinho/large-file-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `11a7e3eb29dd` · [字段定义](../../DATASET.md)*
