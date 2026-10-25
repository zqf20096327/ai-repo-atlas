# wan-huiyan/agent-review-panel

⭐ 37 · JavaScript · MIT · 推送 2026-09-22 · [GitHub](https://github.com/wan-huiyan/agent-review-panel) · 个人维护

**Claude Code 插件：4–6 个 AI 评审员对抗式审查代码与方案**

以 Claude Code 插件形式提供的多智能体评审工具：4–6 个评审员从 Correctness Hawk、Security Auditor、Devil's Advocate 等指定立场独立评审代码、方案或文档，经 1–3 轮对抗辩论、盲评打分与命令验证后，由 judge 裁决分歧，输出 Markdown 报告与交互式 HTML 仪表盘。运行于 Claude Code CLI/IDE 扩展/Desktop Code 标签页及 Claude Agent SDK，不在 claude.ai 网页聊天或裸 Anthropic API 上运行；单次约花费 $3–$20 Opus token、耗时 6–15 分钟。可自动接入 VoltAgent 专家 agent 替换通用角色。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 阶段流水线：独立评审→辩论→盲评→验证→裁决
- 内置反群体思维机制（盲评、谄媚检测、相关偏差警告）
- 输出 Markdown 报告与可交互 HTML 仪表盘（含辩论转录与裁决）
- 自动检测 9 组信号并按内容选择评审角色，可选升级 VoltAgent 专家

## 适用场景

- 高风险实现方案在拍板前做多视角压力测试
- 安全敏感代码或难以逆转的架构决策收集多份独立意见
- 对必须正确的文档做对抗式评审

## 场景标签

 · 领域:开发工具/代码评审

## 证据(README 行号)

> L5: **4–6 AI reviewers independently evaluate your code, plan, or docs, debate each other's findings, then a judge resol
> L11: > Runs only on Claude Code surfaces (CLI, IDE extension, Desktop "Code" tab) and the Claude Agent SDK. Does not wor

## 星数曲线

```mermaid
xychart-beta
    title "wan-huiyan/agent-review-panel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `607d28a696cd` · [字段定义](../../DATASET.md)*
