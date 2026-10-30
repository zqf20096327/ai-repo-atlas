# go-appsec/toolbox

⭐ 43 · Go · MIT · 推送 2026-10-26 · [GitHub](https://github.com/go-appsec/toolbox) · 组织维护

**人机协作应用安全测试工具集：CLI 与 MCP 服务器加内置代理**

面向渗透测试者的协作式测试工作台：单个二进制提供 MCP 服务器、HTTP/1.1/HTTP/2/WebSocket MITM 代理与 CLI，三者共享状态。测试人员负责浏览器认证与 UI 交互，编码 agent（如 Claude Code、Codex）通过 MCP 查询代理历史、重放并篡改请求、检测反射、执行 OAST 带外测试与爬取。可选对接 Burp Suite，支持工作流模式与自定义协议的 sidecar 适配器。通过 go install 安装或下载预编译二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一二进制包含 MCP 服务器、原生 wire-fidelity 代理与共享状态的 CLI
- Agent 可查询流量、重放/篡改请求、检测反射、OAST 带外测试与爬取
- 可选 Burp Suite MCP 扩展前端，或完全无头运行
- 通过 JSON-RPC sidecar 适配器支持自定义与二进制协议

## 适用场景

- 渗透测试中与编码 agent 协作分析已认证流量
- 验证漏洞报告时对流量做结构化 diff 与重放测试
- 从 JS 包中提取端点、路由与密钥以扩展攻击面

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: **MCP-based application security testing tools for your coding agent.**
> L23: ### 2. Start the MCP (Model Context Protocol) server
> L41: **Claude Code:**

## 星数曲线

```mermaid
xychart-beta
    title "go-appsec/toolbox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-30 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d226431b3e87` · [字段定义](../../DATASET.md)*
