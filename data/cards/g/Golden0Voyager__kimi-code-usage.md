# Golden0Voyager/kimi-code-usage

⭐ 15 · Python · 推送 2026-10-22 · [GitHub](https://github.com/Golden0Voyager/kimi-code-usage) · 个人维护 · 中文 README

**Kimi Coding Plan 用量配额追踪工具链：CLI + MCP 服务器 + VS Code 扩展**

面向 Kimi Code（Coding Plan 会员）用户的用量配额追踪工具链，含三个组件：Python CLI（Rich 面板、JSON/纯文本输出、交互模式）、向 MCP 兼容 Agent 暴露 get_kimi_usage 的 MCP 服务器、以及 VS Code 状态栏扩展（周/5 小时配额百分比、低额度阈值告警、速率指示）。需 sk-kimi-xxx 格式的 Kimi Code 控制台 API Key，与 Kimi 开放平台 Key 不互通。另支持读取本地 Codex 认证文件查询 ChatGPT Plus 用量，附 5 个月实测数据的成本分析文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI 提供 Rich 面板、JSON、纯文本与交互模式
- MCP 服务器向 Claude Code、Cursor、Windsurf 等 Agent 暴露 get_kimi_usage
- VS Code 状态栏显示周/5 小时配额与低额度阈值告警、速率指示
- 附 5 个月重度使用的 token 构成与包月/按量计费对比分析

## 适用场景

- 在终端查看 Kimi Coding Plan 的剩余配额
- 让 Claude Code / Cursor 等 Agent 通过 MCP 查询我的 Kimi 配额
- 在 VS Code 状态栏实时监控配额消耗并在低额度时告警

## 场景标签

 · 领域:LLM 基础设施/用量监控

## 证据(README 行号)

> L14: **Manifesting your AI quota with aesthetic precision across CLI, MCP, and VS Code.**
> L86: |`kimiCodeUsage.apiKey`|API key (or reads `KIMI_CODING_API_KEY`/`KIMI_API_KEY` env)|`""`|

## 星数曲线

```mermaid
xychart-beta
    title "Golden0Voyager/kimi-code-usage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bff3f9e24689` · [字段定义](../../DATASET.md)*
