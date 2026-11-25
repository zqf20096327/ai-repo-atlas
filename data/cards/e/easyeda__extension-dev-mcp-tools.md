# easyeda/extension-dev-mcp-tools

⭐ 10 · TypeScript · 推送 2026-03-26 · [GitHub](https://github.com/easyeda/extension-dev-mcp-tools) · 组织维护 · 中文 README

**让 AI Agent 自动导入与调试嘉立创EDA扩展的MCP服务**

面向嘉立创EDA（EasyEDA）专业版扩展开发的 MCP 服务，提供三个工具：import_plugin 自动导入 eext 扩展、dev_plugin 导入并持续监听控制台错误、get_console_logs 拉取浏览器控制台日志（支持过滤、分页、清空，缓存上限 500 条）。工作原理为通过 Playwright 启动或连接 Chrome/Edge（远程调试端口 9222-9231），打开 EDA 调试模式并上传插件，AI Agent 据日志分析插件运行状态。需 Node.js 20.17.0+ 与 Chrome/Edge，从源码构建，可生成适配多款 AI Agent 的 MCP 配置文件。

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

- import_plugin / dev_plugin / get_console_logs 三个 MCP 工具
- 基于 Playwright 自动化插件上传与控制台日志监听
- 支持指定 Chrome 或 Edge 浏览器，登录状态可缓存
- 一条命令生成适配 QwenCode/OpenCode/Kiro/Trae 等的 MCP 配置

## 适用场景

- 让 AI Agent 自动把插件导入嘉立创EDA专业版
- 采集浏览器控制台日志交给 AI 分析插件报错
- 多款 AI Agent 环境下统一接入 EDA 扩展调试流程

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: 用于 嘉立创EDA & EasyEDA 专业版 扩展调试的 MCP 服务。使用此MCP可以实现通过 AI Agent 自动完成插件导入、浏览器控制台日志采集等操作，由AI自动导入、调试插件。
> L64: 1. 未指定浏览器下默认启动 Chrome（开启远程调试端口 9222-9231），或连接已运行的实例
> L67: 4. 通过 Playwright 操作浏览器完成插件上传流程

## 星数曲线

```mermaid
xychart-beta
    title "easyeda/extension-dev-mcp-tools 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `f08f7be82d64` · [字段定义](../../DATASET.md)*
