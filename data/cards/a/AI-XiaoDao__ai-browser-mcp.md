# AI-XiaoDao/ai-browser-mcp

⭐ 53 · C++ · MIT · 推送 2026-09-13 · [GitHub](https://github.com/AI-XiaoDao/ai-browser-mcp) · [官网](https://github.com/AI-XiaoDao/ai-browser-mcp#readme) · 个人维护 · 中文 README

**Windows 本地浏览器自动化 MCP 服务端，向 AI 助手暴露 334 个工具**

运行 FBrowser CEF（Chromium）内核的 Windows 本地 MCP 服务端，通过 stdio/HTTP/WebSocket JSON-RPC 向 Cursor、Claude、Cline、Trae 等 MCP 客户端暴露 334 个浏览器自动化工具，覆盖网页抓取、JS 逆向、CDP 断点调试、指纹反检测、网络拦截、填表 RPA 与工作流编排。下载解压后双击 exe 即用，监听 127.0.0.1:9222，数据不出本机。源码以火山视窗中文编程语言编写，MIT 开源，仅支持 Windows（64/32 位）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 334 个浏览器自动化工具（官方称全量真机核验）
- 运行真实 FBrowser CEF 内核，无需 Node 驱动或脚本
- 原生 stdio 直连 Cursor/Claude/Cline/Trae，支持 auto_install_agents 自动写入配置
- 纯本地 127.0.0.1:9222，提供 HTTP/WebSocket/健康检查端点

## 适用场景

- 让 AI 编程助手直接操作浏览器完成抓取与填表
- 逆向分析网页 JS 逻辑与 CDP 断点调试
- 需要指纹反检测的网络抓包与拦截任务

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L11: **AI浏览器 MCP Server** 运行真实的 **FBrowser CEF（Chromium）浏览器内核**，通过 **Model Context Protocol（MCP）** 向 AI 编程助手（Cursor / Cl
> L97: |`POST http://127.0.0.1:9222/mcp`|HTTP JSON-RPC 主通道|

## 星数曲线

```mermaid
xychart-beta
    title "AI-XiaoDao/ai-browser-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c89e53f58742` · [字段定义](../../DATASET.md)*
