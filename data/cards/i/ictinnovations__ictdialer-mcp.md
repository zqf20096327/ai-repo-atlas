# ictinnovations/ictdialer-mcp

⭐ 16 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ictinnovations/ictdialer-mcp) · [官网](https://ictdialer.com) · 组织维护

**ICTDialer 云外呼平台的 MCP 服务器，供 AI 助手监控与启停外呼活动**

面向 ICTDialer（ICT Innovations 的云自动外呼/预测式外呼平台，与 ICTContact 同引擎）的 Model Context Protocol 服务器。AI 助手可列出外呼活动、查看实时状态、汇总数据与逐通结果；写操作（启动/停止活动）默认不注册，需设置 ICTDIALER_MCP_ALLOW_WRITE=true 才开启。通过环境变量配置服务器地址与账号，调用平台的 form-encoded RPC API。以 npx 直接运行或 npm 全局安装，需 Node.js 18+。

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

- 只读工具默认启用：活动列表、状态、汇总、逐通结果
- 写操作（启动/停止外呼）需显式开启环境变量才注册
- 通过账号密码直连 {base}/rest RPC API，无需单独令牌

## 适用场景

- 让 AI 助手查看外呼活动的运行状态与结果统计
- 在确认风险后由 AI 启动或停止外呼活动
- 接入 Claude Desktop 等 MCP 客户端管理 ICTDialer

## 场景标签

 · 领域:呼叫中心/VoIP 自动化

## 证据(README 行号)

> L3: A Model Context Protocol server for
> L8: It lets an AI assistant monitor outbound campaigns — list them, check status, read

## 星数曲线

```mermaid
xychart-beta
    title "ictinnovations/ictdialer-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5be00e6113e9` · [字段定义](../../DATASET.md)*
