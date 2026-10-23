# dkamm/pr-quiz

⭐ 211 · JavaScript · MIT · 推送 2025-11-24 · [GitHub](https://github.com/dkamm/pr-quiz) · 个人维护

**从 PR 变更生成测验的 GitHub Action，考核评审者对 AI 代码的理解**

面向代码评审者的 GitHub Action：读取 pull request 变更，调用 OpenAI 模型（默认 o4-mini，须支持结构化输出）生成选择题测验；在 Actions runner 内启动临时 webserver 并通过 ngrok 隧道对外提供测验页面，配置时限、尝试次数、行数阈值与排除文件模式，未通过可阻断部署。需提供 OpenAI API Key 与 ngrok auth token 作为 secrets；README 说明代码仅发送给模型提供方，且可改造为对接自托管模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 PR 变更用 OpenAI 模型生成结构化选择题测验
- runner 内临时 webserver + ngrok 公网隧道承载测验
- 可配置行数阈值（默认 100 行）、时限、尝试次数与排除文件模式
- 声明可改造为对接自托管模型

## 适用场景

- AI Agent 写代码后，用测验考核我对变更的理解
- 团队在 CI 中强制评审者通过 PR 测验再部署
- 大改动 PR 中自检是否遗漏了关键细节

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: PR Quiz is a GitHub Action that uses AI to generate a quiz based on a pull
> L44: |model|The model to use for generating the quiz. It must be a model that supports structured outputs.|`o4-mini`|No|

## 星数曲线

```mermaid
xychart-beta
    title "dkamm/pr-quiz 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 209 --> 212
    line [210, 211, 211]
```

2026-10-18 210 → 2026-10-23 211（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `000472544f73` · [字段定义](../../DATASET.md)*
