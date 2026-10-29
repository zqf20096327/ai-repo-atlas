# microsoft/copilot-sdk-samples

⭐ 25 · TypeScript · 推送 2026-09-12 · [GitHub](https://github.com/microsoft/copilot-sdk-samples) · [官网](https://copilot-sdk-samples.coreai.diy) · 组织维护

**GitHub Copilot SDK 官方示例集：演示 agent 应用开发**

微软维护的 GitHub Copilot SDK 示例仓库，包含 9 个示例应用，覆盖 GitHub issue 自动打标、漏洞优先级排序、MCP 编排、agent 技能测试、递归 LLM 模式、EDA PCB 设计分析等场景。提供 mock-first 的连接器实现（GitHub/PagerDuty/Datadog/Teams/EDA/MS Learn），默认无需凭据即可运行开发。仓库标注为进行中（Work in Progress），API 与示例可能随时变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 9 个示例应用覆盖 issue 分诊、安全告警、MCP 编排等场景
- 6 种连接器均支持 mock 模式，无凭据即可开发
- pnpm <sample-name> 单命令运行任一示例

## 适用场景

- 学习 GitHub Copilot SDK 的用法与 TypeScript 模式
- 参考连接器实现与 ConnectorResult 约定开发自己的 agent
- 在无凭据环境下快速跑通 agent 示例

## 场景标签

`Agent 框架` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L6: Sample applications demonstrating the GitHub Copilot SDK.
> L4: > **Work in Progress** — This repository is under active development. APIs and samples may change without notice.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/copilot-sdk-samples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d661c79ae6cf` · [字段定义](../../DATASET.md)*
