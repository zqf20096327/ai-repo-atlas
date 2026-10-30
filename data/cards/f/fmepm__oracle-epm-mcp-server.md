# fmepm/oracle-epm-mcp-server

⭐ 17 · JavaScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/fmepm/oracle-epm-mcp-server) · [官网](https://fmepm.com) · 个人维护

**连接 Claude 与 Oracle EPM Cloud 的 MCP 服务器**

通过 MCP 协议将 Claude Desktop 等 MCP 客户端接入 Oracle EPM Cloud REST API，把自然语言请求转换为 API 调用。提供 7 个工具：列出应用、读取/更新替代变量、执行业务规则、查询任务状态、按维度成员导出数据切片等，可用于月末结账流程自动化。内置 Mock 模式，无需凭据即可用示例数据试用；Live 模式使用 Basic Auth，MFA 账户暂不支持（OAuth 2.0 列在后续计划）。由 Oracle ACE Pro 个人开发者维护，附托管版产品 FMEPM Connect 与教程系列。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个 MCP 工具覆盖 EPM 应用查询、业务规则执行、数据导出与替代变量管理
- 内置 Mock 模式，无凭据即可测试全部功能
- 提供 .mcpb 桌面扩展一键安装与源码手动安装两种方式
- README 给出月末结账自动化的完整工具调用序列示例

## 适用场景

- 用自然语言查询 EPM 应用与替代变量
- 让 AI agent 执行业务规则并轮询任务状态
- 按维度成员导出财务数据用于验证
- 自动化月末结账流程（聚合、验证、滚动期间）

## 场景标签

 · 领域:企业财务系统/AI 接入工具

## 证据(README 行号)

> L3: Connect Claude AI (or any MCP-compatible client) to Oracle EPM Cloud via REST APIs.
> L19: This MCP server gives AI agents the ability to interact with Oracle EPM Cloud. Instead of manually running Postman 
> L44: You (natural language) → Claude Desktop → MCP Protocol → This Server → Oracle EPM REST APIs → Your EPM Cloud

## 星数曲线

```mermaid
xychart-beta
    title "fmepm/oracle-epm-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `932e859d3201` · [字段定义](../../DATASET.md)*
