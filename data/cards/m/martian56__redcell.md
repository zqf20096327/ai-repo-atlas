# martian56/redcell

⭐ 347 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/martian56/redcell) · 个人维护

**LLM 多智能体端到端执行渗透测试并生成报告的平台**

面向授权安全测试的 AI 红队平台：编排 LLM 智能体在 Kali 容器内通过 docker exec 运行 nmap、nuclei、Metasploit 等真实工具，支持代理浏览器、反向 Shell 交互终端、网络跳板（chisel SOCKS 隧道）与代码审计会话；操作员通过 React 控制台以聊天驱动运行并审核发现，最终导出 PDF/JSON/SARIF 报告。模型经 LiteLLM 接入 OpenAI、Anthropic、DeepSeek、本地 Ollama 等。技术栈为 FastAPI + React + Postgres + Redis，提供 docker compose 与自托管部署脚本；README 明确限定仅用于教育研究与合法授权测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph plan/act 多智能体引擎，编排器向执行器分发目标
- Kali 容器内运行 nmap/nuclei/Metasploit 等真实工具，支持本地与远程 SSH 执行
- 代理浏览器、反向 Shell 终端与 chisel 反向 SOCKS 隧道网络跳板
- 导出 PDF/JSON/SARIF 报告，运行过程断点续跑

## 适用场景

- 在授权范围内让 AI 智能体执行完整渗透测试并产出报告
- 安全研究人员对靶场（DVWA、Juice Shop 等）做红队演练
- 对公开 git 仓库或本地代码做源码安全审计

## 场景标签

`网络安全` `多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L3:  AI agents that run a penetration test end to end and write the report.
> L20: REDCELL runs a team of LLM agents through a pentest. An orchestrator plans the engagement and hands objectives to e

## 星数曲线

```mermaid
xychart-beta
    title "martian56/redcell 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 342 --> 348
    line [343, 346, 347]
```

2026-10-18 343 → 2026-10-24 347（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6f491ec9c2cf` · [字段定义](../../DATASET.md)*
