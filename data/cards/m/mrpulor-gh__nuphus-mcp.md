# mrpulor-gh/nuphus-mcp

⭐ 328 · Rust · MIT · 推送 2026-10-20 · [GitHub](https://github.com/mrpulor-gh/nuphus-mcp) · [官网](https://github.com/mrpulor-gh/nuphus-mcp) · 个人维护 · 中文 README

**给 AI agent 用的桌面自动化 MCP 服务器：屏幕/窗口/键鼠/Chrome 控制**

跨平台 Rust 编写的 stdio MCP 服务器，把桌面与浏览器自动化以 45 个标准 MCP 工具（22 桌面 + 23 浏览器）暴露给任意 MCP 客户端（Claude Desktop、Cursor、VS Code、Copilot 等）。桌面侧提供截图、窗口与键鼠控制、基于无障碍树（Windows UIA / macOS AX）的语义化操作；浏览器侧经 CDP 驱动 Chrome/Edge，支持接入外部指纹浏览器并自动重解析调试端口。OCR（PaddleOCR + 可选 YOLO）本地运行、无需 API key；视觉理解工具采用 BYOK，通过 OpenAI 兼容或 Anthropic 原生 API 调用用户自选视觉模型。浏览器工具需 Chrome/Edge，从源码构建需 Rust 工具链；Linux 下桌面能力部分受限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 45 个 MCP 工具：22 桌面 + 23 浏览器（CDP）
- 基于无障碍树的语义化桌面操作（observe→candidate→execute→verify 流程）
- 本地 OCR（PaddleOCR，模型首次运行自动下载）+ BYOK 视觉模型
- 支持外部指纹浏览器接入与调试端口自愈重解析

## 适用场景

- 让 Claude/Cursor 等 MCP 客户端直接控制屏幕、窗口与键鼠
- AI agent 通过 CDP 自动化 Chrome 完成网页操作
- 通过桌面 OCR + 鼠键链路操作无法走 CDP 的真实浏览器窗口

## 场景标签

`GUI 自动化` `浏览器自动化` `OCR` · 领域:效率与自动化

## 证据(README 行号)

> L8: that exposes desktop + browser automation as standard MCP tools. It speaks
> L10: Desktop, Cursor, VS Code, Copilot, or any MCP client can connect and
> L34: - **45 MCP tools** (22 desktop + 23 browser) — screenshots, window control,

## 星数曲线

```mermaid
xychart-beta
    title "mrpulor-gh/nuphus-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 325 --> 329
    line [326, 327, 328]
```

2026-10-18 326 → 2026-10-23 328（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ae4750b19c8a` · [字段定义](../../DATASET.md)*
