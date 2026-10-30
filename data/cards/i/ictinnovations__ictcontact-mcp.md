# ictinnovations/ictcontact-mcp

⭐ 16 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ictinnovations/ictcontact-mcp) · [官网](https://ictcontact.com) · 组织维护

**让 AI 助手监控并启停 ICTContact 外呼活动的 MCP 服务器**

面向 ICTContact 及其托管版 ICTDialer 呼叫中心引擎的 Model Context Protocol 服务器：通过环境变量配置服务器地址与 API 账号后，AI 助手可列出外呼活动、查看实时状态、汇总（接听/失败/人机判别）及单通呼叫结果；默认只读，写入工具仅在 ICTCONTACT_MCP_ALLOW_WRITE=true 时注册，用于启动/停止活动。连接方式为 form-encoded RPC API（{base}/rest/<Method>），携带账号密码，无需单独令牌。以 npx 或全局 npm 安装，需 Node.js 18+。

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

- 4 个只读工具：活动列表/状态/汇总/单呼结果
- 写入工具默认不注册，需显式开启写开关
- 直接复用账号密码的 REST RPC 连接，无需单独令牌

## 适用场景

- 让 Claude 等 AI 助手随时查询外呼活动进度与结果
- 在受控授权下通过 AI 助手启停外呼活动
- 呼叫中心运营团队将 ICTContact 接入 MCP 生态

## 场景标签

 · 领域:通信/呼叫中心自动化

## 证据(README 行号)

> L3: A Model Context Protocol server for
> L8: It lets an AI assistant monitor outbound campaigns — list them, check status,

## 星数曲线

```mermaid
xychart-beta
    title "ictinnovations/ictcontact-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8ab9f90bcbe7` · [字段定义](../../DATASET.md)*
