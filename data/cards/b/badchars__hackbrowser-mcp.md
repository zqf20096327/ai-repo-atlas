# badchars/hackbrowser-mcp

⭐ 25 · TypeScript · MIT · 推送 2026-03-14 · [GitHub](https://github.com/badchars/hackbrowser-mcp) · [官网](https://github.com/badchars/hackbrowser-mcp#quick-start) · 个人维护

**面向安全测试的浏览器 MCP 服务器：给 AI agent 一台 Firefox 做渗透测试**

基于 Model Context Protocol 的 MCP 服务器，为 AI agent 提供真实 Firefox 浏览器与 39 个工具：2-4 个 Cookie/存储/认证相互隔离的容器会话（基于 Firefox Multi-Account Containers）、全量 HAR 流量捕获与改包重放、注入测试（7 类 60+ payload）、IDOR/访问矩阵等越权检测、爬虫与报告生成。面向渗透测试与漏洞赏金场景，可接入 Claude Desktop/Claude Code、Cursor 等 MCP 客户端，也可独立运行或作为 TypeScript 库使用。限制：仅支持 Firefox、macOS/Linux（Windows 未测试）、仅限授权测试。

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

- 2-4 个状态完全隔离的浏览器容器会话，支持跨角色 IDOR/越权检测
- 全量 HAR 1.2 流量捕获、导入导出与改包重放
- 7 类注入测试共 60+ 内置 payload，可由 agent 分析 WAF 响应构造绕过
- 39 个工具覆盖导航、抓包、爬虫、CSRF/限流测试与报告生成

## 适用场景

- 授权渗透测试中用自然语言指挥 AI agent 扫描并测试目标站点
- 用管理员与普通用户双会话对比做 IDOR/访问控制审计
- 离线分析 HAR 文件并复测其中的注入点
- 自动化生成带证据的安全测试报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L24: **hackbrowser-mcp** gives your AI agent a real Firefox browser and 39 security testing tools via the Model Context 
> L141:  Claude Desktop / Claude Code


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0f35d97dd888` · [字段定义](../../DATASET.md)*
