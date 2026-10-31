# sonisoft-cnanda/now-sdk-ext-mcp

⭐ 16 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/sonisoft-cnanda/now-sdk-ext-mcp) · 组织维护

**让 AI 助手直接操作 ServiceNow 实例的 MCP 服务器**

基于 @modelcontextprotocol/sdk 与 @sonisoft/now-sdk-ext-core 构建的 MCP 服务器，通过 stdio 与 JSON-RPC 供 Claude Desktop、VS Code、Cursor、Claude Code、Opencode 等 MCP 客户端调用。工具覆盖后台脚本执行、数据查询、ATF 测试运行、日志跟踪，以及表行为发现（业务规则、UI 动作、客户端脚本、流程、状态模型等 8 类配置的只读盘点）。凭据复用 ServiceNow CLI 的认证存储，可用 NEX_POLICY_DENY 拒绝实例变更操作。需 Node.js ≥ 26 并预先配置 now-sdk 凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 MCP 工具执行 ServiceNow 脚本、查询数据、运行 ATF 测试与跟踪日志
- 表行为发现：8 类配置（业务规则/流程/状态模型等）的只读盘点与依赖检索
- 支持 Claude Desktop、VS Code、Cursor、Claude Code、Opencode 等客户端接入
- NEX_POLICY_DENY 环境变量可拒绝实例变更类工具

## 适用场景

- 在 AI 助手中用自然语言查询和操作 ServiceNow 实例
- 盘点某张表上的业务规则、流程等自动化配置以设计 ATF 测试
- 让 AI 执行服务器端脚本并分析实例日志

## 场景标签

 · 领域:企业 IT 服务管理/开发者工具

## 证据(README 行号)

> L3: An MCP (Model Context Protocol) server that enables AI assistants to interact directly with ServiceNow instances — e
> L5: Built on `@modelcontextprotocol/sdk` and `@sonisoft/now-sdk-ext-core`.
> L74: The server communicates over **stdio** (standard input/output) using the MCP JSON-RPC protocol. It is not meant to 

## 星数曲线

```mermaid
xychart-beta
    title "sonisoft-cnanda/now-sdk-ext-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4d93e15a28c6` · [字段定义](../../DATASET.md)*
