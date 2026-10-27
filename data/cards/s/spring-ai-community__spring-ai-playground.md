# spring-ai-community/spring-ai-playground

⭐ 145 · Java · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/spring-ai-community/spring-ai-playground) · [官网](https://spring-ai-community.github.io/spring-ai-playground/) · 组织维护

**跨平台桌面应用：构建、验证并安全运行 MCP 工具**

基于 Spring AI 的跨平台桌面应用，面向构建 MCP 工具并接入 Claude Desktop、Claude Code、Cursor 等 MCP 兼容环境的开发者和团队。核心机制是「No pass, no run」：新工具以 Draft 状态存在，需通过本地测试运行（Local Pass）后才会发布到内置 MCP server 并可被 Agentic Chat 调用；配合 deny-first 类白名单沙箱与 L0-L5 风险等级。内置可观测面板记录 chat、工具调用、向量查询与 MCP 调用的 trace。限制：进程内沙箱非对抗级隔离，不受信代码需另配容器/microVM。通过 GitHub Releases 分发桌面安装包，也支持 Docker 与 fat JAR 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Local Pass 机制：未通过测试运行的工具不会暴露给 agent
- 内置 MCP server 发布工具，并可代理组合外部 MCP server 的工具
- 内置观测面板覆盖 chat/工具/向量/MCP 调用的 trace 与 token 成本
- 沙箱采用 deny-first 白名单、SSRF 防护与 L0-L5 风险等级

## 适用场景

- 在发布前测试和验证 MCP 工具再接入 Claude Desktop/Cursor 等环境
- 为 agent 调用保留本地的 token 成本、延迟与调用审计记录
- 无需 Java 知识，用小段 JavaScript 构建可复用 MCP 工具

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: Spring AI Playground is a cross-platform desktop app for building, testing, validating, and executing MCP tools in a
> L9: Every tool you build earns a **Local Pass** - a local test-run with your sample arguments. Only passing tools are ad
> L15: In Tool Studio, new or updated built-in tools are test-run before they are published to the built-in MCP server. Yo

## 星数曲线

```mermaid
xychart-beta
    title "spring-ai-community/spring-ai-playground 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 144 --> 146
    line [145, 145]
```

2026-10-18 145 → 2026-10-27 145（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ea5290cfc8b2` · [字段定义](../../DATASET.md)*
