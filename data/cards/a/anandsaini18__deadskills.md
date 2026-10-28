# anandsaini18/deadskills

⭐ 35 · TypeScript · NOASSERTION · 推送 2026-07-14 · [GitHub](https://github.com/anandsaini18/deadskills) · 个人维护

**分析本地会话记录、找出未使用 agent 技能的 CLI 工具**

本地优先的 Node.js 命令行工具，面向 Claude Code 与 Codex 用户：自动发现两个 agent 数据目录（~/.claude、~/.codex）中已安装的技能，解析 SKILL.md 与 JSONL 会话记录，统计每个技能的调用次数与估算 token 成本，并将技能标记为 active/zombie/dead 三种状态，提示可移除的闲置技能。零运行时依赖，无遥测、无网络调用，数据不出本机；通过 npx 一次性运行或 npm 全局安装，支持 --json 与 --since 窗口参数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动检测并读取 Claude Code 与 Codex 的本地技能与会话记录
- 按 active/zombie/dead 三态标记技能使用情况
- 报告每技能的调用次数与估算 token 注入成本（~4字符/token）
- 零运行时依赖、无网络调用，transcript 不出本机

## 适用场景

- 清理长期未调用的 agent 技能以降低每条 prompt 的 token 开销
- 查看已安装技能在真实会话历史中的使用排名
- 用 --json 输出集成到自己的技能管理工作流

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Every installed skill adds its name and description to every prompt you send. That cost is paid on every message, wh
> L89: |Claude Code|`~/.claude`|Supported|

## 星数曲线

```mermaid
xychart-beta
    title "anandsaini18/deadskills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 34 --> 37
    line [36, 35, 35]
```

2026-10-18 36 → 2026-10-28 35（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `109d23423c5a` · [字段定义](../../DATASET.md)*
