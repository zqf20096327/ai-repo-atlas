# Enreign/productboard-mcp

⭐ 20 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Enreign/productboard-mcp) · 个人维护

**连接 Productboard API 的 MCP 服务器，供 AI 助手操作工作区**

用 TypeScript 实现的 Model Context Protocol 服务器，将 Productboard API 封装为 20 个 MCP 工具，覆盖特性、产品层级、客户笔记、目标与关键结果、发布与时间线等对象的增删改查。供 Claude Desktop、Cursor 等 MCP 客户端调用，需配置 PRODUCTBOARD_API_TOKEN（Bearer 或 OAuth2）。提供三种安装方式：.mcpb 一键包、本地克隆构建、npx（尚未发布）。可选缓存、限流与重试配置；stdio 客户端需设 LOG_LEVEL=error。

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

- 20 个 MCP 工具覆盖 Productboard 特性/产品/笔记/OKR/发布管理
- 支持 .mcpb 一键安装包与本地构建两种可用安装途径
- Bearer 与 OAuth2 两种认证方式
- 内置限流、重试与可选响应缓存配置

## 适用场景

- 在 Claude Desktop 或 Cursor 中直接读写 Productboard 特性与客户笔记
- 让 AI 助手代为更新发布状态或创建目标/关键结果
- 通过对话查询产品层级与发布时间线

## 场景标签

 · 领域:AI 工具集成/产品管理

## 证据(README 行号)

> L3: An MCP (Model Context Protocol) server for the Productboard API. Enables AI assistants (Claude, Cursor, etc.) to int
> L9: |`pb_feature_list`|List features with filtering|

## 星数曲线

```mermaid
xychart-beta
    title "Enreign/productboard-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `9a06b5a9fdc9` · [字段定义](../../DATASET.md)*
