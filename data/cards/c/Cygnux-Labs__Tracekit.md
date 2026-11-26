# Cygnux-Labs/Tracekit

⭐ 914 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/Cygnux-Labs/Tracekit) · [官网](https://cygnuxlabs.com/tracekit) · 组织维护

**为 AI agent 工具调用提供事前拦截与可离线验证签名审计记录**

Tracekit 嵌入 agent 的工具调用路径：每次调用执行前判定允许/拒绝/等待人工批准，批准与具体参数一次性绑定；调用、判定与结果由 agent 无法触及的 signer 进程签名写入 append-only 哈希链，每次运行导出为 .tkb 文件，任何人在浏览器中即可离线核验。参照 Certificate Transparency 机制，提供 Python/TypeScript/Go 验证器，兼容 42 个 agent 框架与编码代理（如 Claude Code、LangChain/LangGraph、OpenAI Agents SDK、MCP），覆盖 shell、SQL、HTTP、邮件、支付等策略包。Python 3.9–3.13，TypeScript 需 Node 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每次工具调用执行前做 allow/deny/人工批准判定，批准绑定确切参数
- 独立 signer 签名写入 append-only 哈希链，导出 .tkb 文件可离线核验
- 宣称 8/8 篡改攻击检出、1073/1073 有害调用被拦截、每次调用开销约 0.91ms p99
- 兼容 Claude Code、LangChain/LangGraph、OpenAI Agents SDK、MCP 等 42 个框架

## 适用场景

- 编码代理上生产前审查它实际改了什么、是否尝试过危险命令
- 向企业客户交付每次运行的核验文件以通过安全审查
- 安全团队建立统一控制点并保留事后审计证据
- 审计/GRC 人员离线自行核验 AI 运行记录并映射合规框架

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L36: Tracekit sits in the tool-call path, the way a flight recorder sits in a plane:
> L135:  Works with Claude Code, Codex CLI, Cursor and Gemini CLI; the Python and TypeScript SDKs; the OpenAI Agents SDK, 
> L130: `tracekit.instrument()` starts a dev signer (or reuses the running one) and gates and records every tool and model

## 星数曲线

```mermaid
xychart-beta
    title "Cygnux-Labs/Tracekit 星数(近 24 点)"
    x-axis ["2026-10-24", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 74 --> 990
    line [150, 173, 250, 259, 353, 355, 357, 358, 359, 150, 603, 605, 646, 687, 726, 727, 728, 772, 734, 760, 799, 841, 837, 914]
```

2026-10-24 150 → 2026-11-26 914（+764）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `f5c3e4c16003` · [字段定义](../../DATASET.md)*
