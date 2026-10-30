# jdonohoo/vern-bot

⭐ 15 · Go · 推送 2026-05-31 · [GitHub](https://github.com/jdonohoo/vern-bot) · 个人维护

**多 LLM 编排终端工具：用 18 个 AI 人格跑项目发现流水线**

以独立终端应用或 Claude Code 插件形式提供：通过调度本机已安装的 LLM CLI（claude/codex/gemini/copilot），以 18 个人格化 persona 组合执行项目发现流水线（5 步或 7 步），后续可选 VernHole 议会（3-15 个 persona 头脑风暴）与 Oracle 综合，输出 VTS 任务文件并可导入 Beads。支持失败回退、20 分钟超时看门狗、按步恢复与重试。运行前提是本机至少安装一个 LLM CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个 persona 对应不同模型（Sonnet/Opus/Haiku/Gemini/Codex）与分工
- 5/7 步多 LLM 发现流水线，Historian 用 Gemini 2M 上下文索引输入材料
- 失败容忍：超时看门狗、自动回退、--resume-from 按步恢复
- VTS 任务可经 br CLI 导入 Beads 问题跟踪（预校验、可重跑）

## 适用场景

- 对一个新想法做多视角多模型的项目发现与规划
- 让多个 AI persona 议会就架构分歧进行头脑风暴并综合
- 把流水线产出的任务清单导入 Beads 跟踪执行

## 场景标签

`多智能体` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L138: **Required:** At least one LLM CLI installed — `claude`, `codex`, `gemini`, or `copilot`.
> L179: |`mixed_claude_fallback`|Default. Mixed LLMs per step, claude catches failures|
> L230: |`/vern:discovery`|Full pipeline: Default (5-step) or Expanded (7-step) multi-LLM discovery + council + Oracle|

## 星数曲线

```mermaid
xychart-beta
    title "jdonohoo/vern-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `52f389ace2a2` · [字段定义](../../DATASET.md)*
