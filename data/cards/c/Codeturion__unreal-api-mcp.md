# Codeturion/unreal-api-mcp

⭐ 97 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/Codeturion/unreal-api-mcp) · [官网](https://www.fuatcankoseoglu.com/) · 个人维护

**给 AI agent 提供 Unreal Engine C++ API 文档查询的 MCP 服务器**

面向 Claude Code、Cursor 等 MCP 兼容工具的 API 文档查询服务器：按 UE 版本提供 SQLite 数据库，暴露 5 个工具用于查找 API、函数签名、#include 路径、类参考与弃用警告，查询延迟在毫秒级。版本可由环境变量或 .uproject 自动检测，数据库首次运行时从 GitHub 下载，每周一由 CI 自动构建新版本数据库；也可用本地 UE 安装自行构建。不覆盖第三方插件与商城资源。附带 14 题基准测试脚本与延迟测量方法，可复现。

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

- 5 个 MCP 工具：搜索/签名/include 路径/类参考/弃用警告
- 按 UE 版本分库（UE 5.7 库含 114,724 条记录），精确查询 <1ms
- 支持 .uproject EngineAssociation 自动版本检测，每周 CI 自动构建新版本数据库
- 可用本地 UE 安装自行构建数据库

## 适用场景

- 在 Claude Code/Cursor 中写 UE C++ 时核验函数签名与 include 路径
- 检查所用 API 在特定 UE 版本中是否已弃用
- 编写 K2 自定义节点/编辑器工具时查询 Blueprint 内部 API

## 场景标签

 · 领域:游戏开发/开发者工具

## 证据(README 行号)

> L12: **MCP server that gives AI agents accurate Unreal Engine C++ API documentation. Saves tokens, context, and time. Pr
> L14: Works with Claude Code, Cursor, Windsurf, or any MCP-compatible AI tool. No Unreal Engine installation required. Ch
> L48: ## Tools

## 星数曲线

```mermaid
xychart-beta
    title "Codeturion/unreal-api-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 95 --> 98
    line [96, 97, 97]
```

2026-10-18 96 → 2026-10-24 97（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f553398c2ffd` · [字段定义](../../DATASET.md)*
