# spectral-mcp/spectral

⭐ 121 · Python · MIT · 推送 2026-03-31 · [GitHub](https://github.com/spectral-mcp/spectral) · [官网](https://www.getspectral.sh/) · 组织维护

**捕获应用流量并生成 MCP 工具，让 AI agent 直接调用私有 API**

面向 AI agent 开发者的流量逆向工具：通过 Chrome 扩展或 MITM 代理记录网页、移动（Android）、桌面应用与 CLI 的 HTTPS 流量，在构建期用 LLM 将用户操作与 API 调用关联、推断各端点的业务含义，据此生成 MCP 工具供任意 AI agent 直接调用；工具运行时失败时由 LLM 自动修补，运行期本身不调用 LLM。附带认证流程检测与登录脚本生成，另可从 REST 流量产出 OpenAPI 3.1 规范、从 GraphQL 流量产出 SDL schema。提供安装脚本与 pip/uv 安装方式。

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

- 通过 Chrome 扩展或 MITM 代理捕获 web/移动/桌面应用的 HTTPS 流量
- LLM 在构建期推断端点业务含义并生成 MCP 工具，运行期为直接 HTTP 调用
- 生成的工具运行失败时由 LLM 自动修补
- 可产出 OpenAPI 3.1 规范与 GraphQL SDL schema

## 适用场景

- 让 AI agent 绕过浏览器自动化直接调用应用的未文档化 API
- 逆向整理某应用的接口并生成 OpenAPI/GraphQL 规范用于文档或代码生成
- 为无公开 API 的应用快速构建 agent 可调用的工具集

## 场景标签

 · 领域:AI agent 基础设施/API 逆向工程

## 证据(README 行号)

> L20: Most apps — web, mobile, desktop — sit on top of undocumented HTTP APIs. Spectral records the traffic while you bro
> L59: 4. **Use** — Start the MCP server. AI agents call the API directly

## 星数曲线

```mermaid
xychart-beta
    title "spectral-mcp/spectral 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-23 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b59de277d304` · [字段定义](../../DATASET.md)*
