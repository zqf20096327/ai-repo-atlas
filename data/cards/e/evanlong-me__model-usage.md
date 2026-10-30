# evanlong-me/model-usage

⭐ 21 · TypeScript · MIT · 推送 2026-09-16 · [GitHub](https://github.com/evanlong-me/model-usage) · [官网](https://www.npmjs.com/package/model-usage) · 个人维护

**零配置 CLI：汇总本地各 AI 编码工具的用量与成本**

命令行工具 `mu`，自动检测 pi、Claude Code、Codex、Gemini CLI、OpenCode、Grok CLI 六种本地 TUI 工具的会话数据文件，统计 token 用量并按预置或 LiteLLM 价格计算成本；支持时间/项目/模型过滤、按成本/token/时间排序、聚合或逐条消息视图。仅读取本地磁盘，无需 API key，仅从 LiteLLM 拉取模型价格（缓存 1 小时）。要求 Node.js ≥22（使用内置 node:sqlite）且至少有一个已支持的 TUI 工具历史数据；新增工具支持只需添加一个源文件。

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

- 自动检测六种 TUI 工具的本地数据，零配置运行
- 成本计算支持预置价格或 LiteLLM 价格
- 时间/项目/模型过滤与多维排序、多种视图模式
- 新增 TUI 工具支持仅需一个源文件（自动发现）

## 适用场景

- 一条命令查看我在各 AI 编码工具上的 token 与花费
- 按项目或日期核对不同模型的用量分布
- 在 CI/cron 等非交互环境自动汇总全部来源用量

## 场景标签

 · 领域:开发者工具/AI 用量分析

## 证据(README 行号)

> L3: Zero-config CLI for analyzing AI model usage & costs across all local TUI tools — pi, Claude Code, Codex, Gemini CLI
> L10: - 💰 **Cost Tracking** - Accurate cost calculation (pre-computed or LiteLLM pricing)

## 星数曲线

```mermaid
xychart-beta
    title "evanlong-me/model-usage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0dbab7dd2a06` · [字段定义](../../DATASET.md)*
