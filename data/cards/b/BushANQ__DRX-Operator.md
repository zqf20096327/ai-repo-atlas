# BushANQ/DRX-Operator

⭐ 59 · Python · GPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/BushANQ/DRX-Operator) · 个人维护 · 中文 README

**LLM 驱动的自主红队渗透测试系统（Agent-First）**

以 LLM 驱动的 Master Agent 为核心的自主渗透测试系统，通过 ReAct 循环（Plan/Think/Act/Observe/Reflect）自主决策并调用 30+ 内置工具执行安全测试。提供 Python/Bash 沙箱、持久 Shell 会话、OOB 回调监听、MCP 协议扩展、声明式权限引擎与五级安全门控，以及七层上下文压缩管道支持超长会话。支持 Anthropic/OpenAI/DeepSeek 等多 Provider 及回退链。README 声明当前 Python 版本仅为早期概念验证（Alpha）。仅限授权安全测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- ReAct 五阶段自主决策循环，全程通过 LLM 工具调用执行
- 五级安全门控（L0 自动批准到 L4 需确认短语）与声明式 PermissionEngine
- 七层上下文压缩管道，单会话支持数万轮交互
- Provider 回退链：429/5xx 自动重试并切换下一 Provider

## 适用场景

- 在获得书面授权的前提下执行自动化渗透测试
- 让 Agent 自主执行侦察、漏洞发现与结果分析的长会话任务
- 通过 MCP 协议接入外部工具服务器扩展测试能力

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: DRX-Operator is an autonomous penetration testing system built around an **Agent-First architecture**. Unlike tradi
> L17: The terminal interface (TUI) is merely a thin presentation layer. The Agent is a first-class citizen of the system 

## 星数曲线

```mermaid
xychart-beta
    title "BushANQ/DRX-Operator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-25 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e264670ffd0b` · [字段定义](../../DATASET.md)*
