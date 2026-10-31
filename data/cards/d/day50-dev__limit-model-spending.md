# day50-dev/limit-model-spending

⭐ 21 · Python · MIT · 推送 2026-09-23 · [GitHub](https://github.com/day50-dev/limit-model-spending) · 组织维护

**给 LLM agent 配置限额 API key 的成本封顶工具**

DAY50 开源套件中的 capit：为各类编码/agent 客户端（Claude Code、Cursor、Windsurf、OpenClaw 等 7 种）管理带花费上限的 API key。机制是调用平台（OpenRouter、aihubmix、concentrate）API 创建带金额 guardrail 的新 key 并写入 agent 配置文件，上限由平台强制执行；旧配置自动备份，支持自定义 agent 与平台扩展。提供 GUI（uvx capit serve）与 TUI，密钥列表/删除等管理命令；数据仅本地存储，无自有服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 agent、按 provider 设置花费上限，上限由平台侧 guardrail 强制执行
- 支持 7 种 agent（Claude Code、Cursor、Windsurf、OpenClaw 等），旧配置自动备份
- 内置 openrouter、aihubmix、concentrate 三个平台，可通过 skill 扩展新平台
- 提供 GUI、TUI 与 key 管理命令（list/delete）

## 适用场景

- 给失控循环烧钱的 agent 设硬性花费上限
- 为多个 agent 分别配置独立限额 API key
- 统一列出和清理各 provider 的已花费 key

## 场景标签

 · 领域:AI 工作流/成本管理

## 证据(README 行号)

> L9: **capit**, part of the DAY50 suite of open-source tools for AI workflows, allows for managing application-based key 
> L95: 3. capit creates a **guardrail** with $5 cap
> L96: 4. capit creates an **API key** with that guardrail

## 星数曲线

```mermaid
xychart-beta
    title "day50-dev/limit-model-spending 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b0fc76d052f7` · [字段定义](../../DATASET.md)*
