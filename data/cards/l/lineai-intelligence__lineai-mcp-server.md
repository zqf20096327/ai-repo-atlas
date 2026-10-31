# lineai-intelligence/lineai-mcp-server

⭐ 37 · Python · MPL-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/lineai-intelligence/lineai-mcp-server) · [官网](https://codelogic.com/) · 组织维护

**让 AI 编程助手调用 Lineai 依赖数据图的 MCP 服务器**

面向 AI 编程助手（VS Code Copilot、Claude Desktop、Cursor、Windsurf）的 MCP 服务器：将 Lineai 服务端的软件依赖数据以 8 个工具暴露给助手，包括方法影响分析、代码-数据库影响分析，以及 6 个图查询工具（节点搜索、影响半径遍历、最短路径解释、变更范围校验、owner 解析等）。通过环境变量配置 Lineai 服务器地址与账号认证，支持缓存 TTL 与超时调优。限制：v0.4.0 起要求 Lineai API 25.10.0 以上；图工具需服务端部署对应端点，否则返回 404；面向 Java/JavaScript/TypeScript/C# 代码库。安装依赖 Astral uv/uvx，macOS 上 uvx 在部分 IDE 存在启动问题需 clone 后改用 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个 MCP 工具：2 个影响分析 + 6 个图查询工具
- 支持 VS Code Copilot / Claude Desktop / Cursor / Windsurf 四种客户端配置
- 环境变量配置工作区、认证与缓存 TTL/超时调优
- 版本兼容性明确：v0.4.0+ 需 Lineai API 25.10.0 以上

## 适用场景

- 在 IDE 中改代码前让 AI 助手评估方法级影响范围
- 分析代码改动与数据库实体之间的依赖影响
- 通过图搜索与路径解释理解代码库依赖关系

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: An MCP Server to utilize Lineai's rich software dependency data in your AI programming assistant.
> L18: The server implements **eight** tools: two impact tools plus six **graph** tools backed by the Lineai graph HTTP AP

## 星数曲线

```mermaid
xychart-beta
    title "lineai-intelligence/lineai-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `dbe77e09e282` · [字段定义](../../DATASET.md)*
