# microsoft/upgrade-agent-plugins

⭐ 44 · PowerShell · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/microsoft/upgrade-agent-plugins) · 组织维护

**GitHub Copilot 的应用升级插件：AI 助手升级语言与框架版本**

微软仓库，提供名为 Upgrade 的 Copilot 代理及插件，用于将应用升级到语言、框架与运行时的新版本：代理评估应用、生成升级计划、应用代码变更并验证结果，通过交互式工作流完成。可从 GitHub Copilot app 的 marketplace 一键安装，也可经 Copilot CLI 用 /plugin 命令安装；另附 Copilot Cloud Agent 的自定义代理定义，可通过 pull request 直接升级项目。示例提示词演示升级到 .NET 10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Upgrade 代理执行评估→计划→代码变更→验证的升级工作流
- 支持 GitHub Copilot app、Copilot CLI 与 Copilot Cloud Agent 三种途径
- Cloud Agent 模式可通过 pull request 直接升级项目

## 适用场景

- 让 Copilot 代理把项目升级到 .NET 10 等新版本
- 通过 pull request 在仓库内完成版本升级
- 在 Copilot CLI 中以插件形式安装并调用升级代理

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: GitHub Copilot upgrade is an AI-powered agent that helps you upgrade applications to newer versions of languages, fr
> L41: /plugin marketplace add microsoft/upgrade-agent-plugins

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/upgrade-agent-plugins 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-28", "2026-10-31"]
    y-axis "stars" 40 --> 45
    line [41, 42, 43, 44, 44]
```

2026-10-18 41 → 2026-10-31 44（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `345ad8dbe1cf` · [字段定义](../../DATASET.md)*
