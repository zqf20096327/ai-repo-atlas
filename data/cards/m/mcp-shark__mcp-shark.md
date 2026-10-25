# mcp-shark/mcp-shark

⭐ 179 · JavaScript · NOASSERTION · 推送 2026-04-26 · [GitHub](https://github.com/mcp-shark/mcp-shark) · [官网](https://mcpshark.sh/) · 组织维护

**面向安全工程师的 MCP 配置与流量取证扫描器**

运行在本机的 MCP 安全工具：静态 scan 命令读取 15 种 IDE 的 MCP 配置与内嵌工具元数据，用 41 条规则（OWASP MCP Top 10、AAuth 可见性、通用检查）输出 SARIF/JSON/HTML 报告，并做 toxic-flow 跨服务器风险组合推断、Shark Score 评分与 --fix 自动修复。可选 serve 模式启动本地代理，在浏览器仪表盘中捕获 JSON-RPC 实时流量、运行本地分析、YARA 规则检测、AAuth 知识图谱与 MCP Playground。静态扫描无需云端与 API key，AI 驱动的 Smart Scan 为可选功能（需自带 API token）。以 npm 包提供，要求 Node.js 20+，许可为 Non-Commercial。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 41 条安全规则静态扫描 MCP 配置，支持 SARIF/JSON/HTML 四种输出
- 本地代理 + 浏览器仪表盘：实时流量捕获、AAuth 图谱、MCP Playground
- toxic-flow 跨服务器风险组合推断与攻击链叙事
- 规则可扩展：JSON 规则包注册表 + 项目级 YAML 自定义规则

## 适用场景

- 审计 IDE 中 MCP 服务器配置的密钥泄露与危险组合
- 在 CI 中用 --ci 模式对 MCP 配置做门禁检查
- 通过本地代理观察 IDE 与 MCP 服务器间的实时 JSON-RPC 流量

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5:  Security scanner for AI agent tools — built for security and platform engineers working with MCP in the IDE.
> L71: mcp-shark runs on your machine — no API keys or hosted scan backend. Install with `npx` and review findings locally

## 星数曲线

```mermaid
xychart-beta
    title "mcp-shark/mcp-shark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 178 --> 180
    line [179, 179]
```

2026-10-18 179 → 2026-10-25 179（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9d8722be51b8` · [字段定义](../../DATASET.md)*
