# gojue/moling

⭐ 339 · Go · Apache-2.0 · 推送 2026-03-15 · [GitHub](https://github.com/gojue/moling) · [官网](https://gojue.cc) · 组织维护 · 中文 README

**本地办公自动化 MCP 服务器：让 AI 客户端操作文件与浏览器**

基于 Go 编写的 MCP Server，通过操作系统 API 实现文件系统操作（读取、写入、合并、统计、汇总）、系统命令执行，以及基于 chromedp 的浏览器控制（需本机安装 Chrome）。无运行时依赖，提供单一二进制可跨 Windows/Linux/macOS 运行，支持 Stdio 与 SSE 两种模式，可通过 moling client --install 自动为 Claude、Cline、Roo Code 等 MCP 客户端写入配置。限制：目前仅在 macOS 上测试过，Windows 安装脚本未测试；命令行操作存在风险。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 文件系统操作与系统命令执行（读/写/合并/统计/汇总）
- 基于 chromedp 的浏览器控制，需本机 Chrome
- 无依赖单二进制，支持 Windows/Linux/macOS
- moling client --install 自动检测并配置 MCP 客户端

## 适用场景

- 为 Claude/Cline 等支持 MCP 的客户端接入本机办公自动化能力
- 让 AI 客户端代为执行文件整理与浏览器操作
- 在无 Node.js/Python/Docker 环境的机器上部署本地 MCP 工具服务

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: MoLing is a computer-use and browser-use MCP Server that implements system interaction through operating system API
> L39: - Claude
> L81: MoLing will automatically detect the MCP client and install the configuration for you. including: Cline, Claude, Ro

## 星数曲线

```mermaid
xychart-beta
    title "gojue/moling 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 338 --> 340
    line [339, 339]
```

2026-10-18 339 → 2026-10-31 339（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6ac7ec6d7745` · [字段定义](../../DATASET.md)*
