# g4sk0/mergen-mcp

⭐ 16 · Python · MIT · 推送 2026-02-26 · [GitHub](https://github.com/g4sk0/mergen-mcp) · 个人维护

**面向渗透测试人员的 MCP 服务器：让 AI 代理调度 44+ 安全工具**

Mergen 是一个基于 FastAPI 与 MCP 协议的渗透测试服务器：Claude、Cursor、Antigravity 等 MCP 兼容代理通过 stdio 或 SSE 接入后，可调用其暴露的 44 个安全工具插件（nmap、nuclei、sqlmap 等）。核心机制包括 TargetProfiler 目标分类、KillChainBuilder 从 41 条预定义攻击链中选择、AdaptiveExecutionEngine 动态执行并随结果更新计划、关联引擎统一风险评分，结果存入 SQLite 并导出 HTML/JSON/CSV。另提供 Claude Skill（Ouroboros Pentest Skill）与 Antigravity User Rule 实现自主循环执行。标注为 BETA；推荐运行环境为 Kali Linux，安装脚本经 apt 安装 36+ 安全工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 44 个安全工具插件按 MCP 协议暴露给 AI 代理
- 41 条预定义攻击链与自适应执行引擎，结果动态更新计划
- Ouroboros Skill/Rule 实现 RECON→POST_EXPLOIT 五阶段自主循环
- 发现关联引擎统一风险评分，报告导出 HTML/JSON/CSV 并支持 SQLite 持久化

## 适用场景

- 我在授权渗透测试或 CTF 中让 AI 代理自主执行侦察到报告的完整流程
- 我在漏洞赏金项目中通过单一触发词驱动多工具链式扫描
- 我在安全评估中生成结构化的会话报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L12: **AI-native MCP server that gives Claude, Cursor, Antigravity and any MCP-compatible agent full penetration testing
> L29: 1. **Agent Connection** — Claude, Cursor, or any MCP-compatible agent connects via the stdio or SSE transport.

## 星数曲线

```mermaid
xychart-beta
    title "g4sk0/mergen-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `27a85350e75e` · [字段定义](../../DATASET.md)*
