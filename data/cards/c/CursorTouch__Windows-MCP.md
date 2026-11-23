# CursorTouch/Windows-MCP

⭐ 12,014 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/CursorTouch/Windows-MCP) · 组织维护

**连接 AI agent 与 Windows 系统的 MCP 服务器，提供系统操作工具**

Windows-MCP 是一个开源 MCP 服务器，作为 LLM 与 Windows 操作系统之间的桥接层，向接入的 MCP 客户端暴露文件导航、应用控制、UI 交互、键鼠模拟、QA 测试等工具。不依赖传统计算机视觉技术或微调模型，可配合任意 LLM 使用；提供 DOM 模式用于浏览器页面内容自动化，支持 Chrome/Edge/Firefox。通过 uvx 从 PyPI 运行或源码运行，支持 stdio/SSE/Streamable HTTP 传输，提供登录时后台任务安装，可配置进 Claude Desktop、Perplexity Desktop、多款 CLI 客户端。仅支持 Windows 10/11，需 Python 3.14+。

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

- 以 MCP 服务器形式向客户端暴露 Windows UI 自动化工具集
- 配合任意 LLM 使用，不依赖计算机视觉或微调模型
- 支持 stdio/SSE/Streamable HTTP 传输与登录时后台任务安装
- DOM 模式过滤浏览器 UI，聚焦网页内容自动化

## 适用场景

- 让 AI agent 操作 Windows 完成文件与应用管理任务
- 对 Windows 应用做 UI 自动化 QA 测试
- 通过 MCP 客户端实现浏览器网页内容自动化

## 场景标签

`GUI 自动化` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L22: **Windows-MCP** is a lightweight, open-source project that enables seamless integration between AI agents and the W
> L29: - Windows-MCP is now available on PyPI (thus supports `uvx windows-mcp`)
> L83: uvx windows-mcp serve

## 星数曲线

```mermaid
xychart-beta
    title "CursorTouch/Windows-MCP 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 9321 --> 12258
    line [9565, 9792, 9999, 10132, 10225, 10317, 10432, 10524, 10633, 10710, 10779, 10847, 10911, 10225, 11340, 11480, 11520, 11575, 11625, 11670, 11717, 11763, 11834, 11871, 11904, 11949, 11986, 12014]
```

2026-10-21 9,565 → 2026-11-23 12,014（+2,449）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `88c06be4fe68` · [字段定义](../../DATASET.md)*
