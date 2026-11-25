# coleleavitt/ida-mcp-server

⭐ 14 · C++ · MIT · 推送 2026-11-12 · [GitHub](https://github.com/coleleavitt/ida-mcp-server) · 个人维护

**IDA Pro 的 MCP 插件：让 AI 代理操作反汇编与反编译**

以 IDA SDK 编写的原生 C++ 插件，在 IDA Pro 9.x 内启动 HTTP MCP 服务器（127.0.0.1:7777/mcp），供 Claude Code、Claude Desktop、Cursor 等 MCP 客户端调用；共 249 个工具，覆盖反汇编、Hex-Rays 反编译、微码、类型、交叉引用、补丁、调试器与 IDAPython/IDC 脚本执行。默认仅启用 141 个工具以控制代理上下文，可用环境变量开启全部。需 IDA Pro 9.x 正版许可；服务器无身份认证，仅绑定本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 249 个工具覆盖反汇编、反编译、微码、补丁与调试
- 原生 C++ 实现，无 Python 桥接、无额外进程
- 默认 141 个工具的工具配置文件（profile）机制控制上下文大小
- 兼容 ida-pro-mcp 1.4 的 10 个只读工具

## 适用场景

- 让 AI 代理在打开的 IDA 数据库中做逆向分析
- 通过自然语言客户端批量反编译与导出函数
- 在代理流程中执行 IDAPython/IDC 脚本与补丁操作

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A native C++ plugin for IDA Pro that lets AI agents and LLM clients (Claude Code, Claude Desktop, Cursor, Codex, or 
> L9: - **MCP over HTTP.** Protocol versions 2024-11-05 through 2025-11-25 are supported, and the server answers on
> L16: ## Install

## 星数曲线

```mermaid
xychart-beta
    title "coleleavitt/ida-mcp-server 星数(近 3 点)"
    x-axis ["2026-11-12", "2026-11-18", "2026-11-25"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-11-12 13 → 2026-11-25 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `8b958e2f2953` · [字段定义](../../DATASET.md)*
