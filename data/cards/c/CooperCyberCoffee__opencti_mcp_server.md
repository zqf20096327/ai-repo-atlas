# CooperCyberCoffee/opencti_mcp_server

⭐ 29 · Python · NOASSERTION · 推送 2026-10-05 · [GitHub](https://github.com/CooperCyberCoffee/opencti_mcp_server) · [官网](https://coopercybercoffee.com) · 个人维护

**把 Claude Desktop 接入 OpenCTI 的 MCP 服务器，自然语言查威胁情报**

基于 Model Context Protocol 的服务器，将 Claude Desktop 连接到自托管的 OpenCTI 威胁情报平台，面向资源受限的安全团队与关键供应链中小企业。提供 13 个工具：IOC 搜索（自动识别 IPv4/IPv6/域名/URL/邮箱/文件哈希 6 种类型）、威胁行为体 TTP 查询、恶意软件与战役详情、实体关系分析等。含服务端 TLP 过滤（默认仅 TLP:CLEAR）、速率限制、审计日志，并文档化本地 LLM/离线部署路径以处理敏感数据。要求 OpenCTI 6.x 与 Claude Pro 或本地 LLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个威胁情报工具，含多类型 IOC 自动识别搜索
- 服务端 TLP 过滤（默认仅放行 TLP:CLEAR），防止敏感数据进入 LLM 上下文
- 速率限制、ISO 8601 审计日志（SIEM 兼容 JSON）、操作取消
- 文档化本地 LLM 与离线（air-gapped）部署路径

## 适用场景

- 用自然语言查询 OpenCTI 中的威胁行为体 TTP 与 IOC，替代手工查询
- 小安全团队低成本获得 AI 辅助的威胁情报分析
- 合规敏感环境下以本地 LLM 离线部署处理 TLP:RED/CUI 数据

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: **Connect Claude Desktop to OpenCTI for AI-augmented threat intelligence analysis**
> L99: An open-source educational project demonstrating how to bridge Claude Desktop with OpenCTI's threat intelligence pl
> L135: This MCP server connects Claude Desktop to your OpenCTI threat intelligence platform, enabling you to:

## 星数曲线

```mermaid
xychart-beta
    title "CooperCyberCoffee/opencti_mcp_server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `5a1757e092fe` · [字段定义](../../DATASET.md)*
