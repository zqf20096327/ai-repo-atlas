# XenoXilus/outlook-mcp

⭐ 30 · JavaScript · 推送 2026-09-04 · [GitHub](https://github.com/XenoXilus/outlook-mcp) · 个人维护

**让 AI 助手经 Microsoft Graph 读写 Outlook 邮件日历的 MCP 服务器**

面向 MCP 客户端（Claude Desktop、Claude Code、mcp CLI 等）的 Microsoft Outlook/Office 365 集成服务器，通过 Microsoft Graph API 提供邮件读写搜索发送、日历管理、SharePoint 文件访问、Office 文档解析及 PDF/Word/PPT/Excel 文本提取。含五个收据/发票自动归集工具（附件/账单链接/无头 Chrome 渲染三级回退，按供应商规则命名并生成清单），支持共享邮箱与无浏览器 headless 定时运行。使用前需在 Azure 注册应用获取 Client/Tenant ID，采用 PKCE 流程无需 client secret。安装方式为 DXT 扩展下载或 git clone 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 邮件读写/搜索/回复 + 日历管理 + SharePoint 文件访问
- 收据/发票自动归集：附件→账单链接→headless Chrome 渲染 PDF 三级回退，幂等重跑
- 支持共享邮箱（per-call mailbox 参数）与 headless 定时任务（加密 refresh token）
- Office 文档解析（PDF/Word/PPT/Excel）与大文件自动处理

## 适用场景

- 让 Claude 等 AI 助手代为读取、搜索和回复我的邮件
- 每月定时自动收集邮箱收据与发票 PDF 并规范命名
- 通过 AI 助手查看和管理日历事件、下载邮件附件

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that enables AI assistants to interact with Microsoft Outlook email and calend
> L24: |CLI Configuration|Claude Code, mcp CLI, other MCP clients|

## 星数曲线

```mermaid
xychart-beta
    title "XenoXilus/outlook-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b09cbfb49200` · [字段定义](../../DATASET.md)*
