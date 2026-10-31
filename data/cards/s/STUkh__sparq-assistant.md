# STUkh/sparq-assistant

⭐ 30 · JavaScript · MIT · 推送 2026-03-23 · [GitHub](https://github.com/STUkh/sparq-assistant) · 个人维护

**为 QA 工程师与开发者生成手工测试与 E2E 自动化测试的 AI 助手**

SparQ 安装在 AI 编码助手（Claude Code/Cursor/Codex）中的测试生成流水线：通过 npx init 安装 5 个 AI agent 与 20 个技能，由编排 agent 从 Jira/Confluence/Figma 拉取需求，分阶段生成 HP/VE/SEC/EC/A11Y 五类手工测试用例与 Playwright/Cypress 页面对象代码，每阶段需人工审批；测试用例可导出至 TestRail/Qase/Zephyr。另含 18 条无 AI 推理的 lint 规则用于 CI 质量门禁。要求 Node.js >= 22 与一个 AI 编码助手，纯 Node 内置模块零依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个专职 agent 分阶段流水线：需求分析→测试生成→DOM 验证
- 生成 5 类手工测试（HP/VE/SEC/EC/A11Y）与匹配现有代码模式的 E2E 代码
- 18 条纯 JavaScript lint 规则，零 AI 推理，SARIF 输出接入 GitHub Code Scanning
- 上下文预算控制：agent 间 3,000 token 结构化交接，150K token 硬停

## 适用场景

- 从 Jira 工单批量生成手工测试用例与 E2E 自动化代码
- 把测试用例导出到 TestRail/Qase/Zephyr 并保持需求追溯
- 在 CI 中用确定性 lint 规则做测试质量门禁
- 缺陷工单一键追加 REG- 编号的回归测试

## 场景标签

`编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L34: SparQ reads your requirements, generates both manual test cases and E2E automation code that matches your existing 
> L203: **5 specialized AI agents** in a phased pipeline — orchestrator classifies your request into one of 6 scenarios, d

## 星数曲线

```mermaid
xychart-beta
    title "STUkh/sparq-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `909020e1effa` · [字段定义](../../DATASET.md)*
