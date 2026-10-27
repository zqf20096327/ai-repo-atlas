# microsoft/Agent365-Samples

⭐ 112 · C# · MIT · 推送 2026-10-23 · [GitHub](https://github.com/microsoft/Agent365-Samples) · 组织维护

**微软 Agent 365 SDK 的示例 agent 与提示词集合**

微软官方维护的样例仓库：提供 C#/.NET、Python、Node.js/TypeScript、Salesforce/Apex 四种语言的示例 agent，演示可观测性、通知、工具与托管模式，目标平台包括 M365、Teams、Copilot Studio 与 Webchat；另附面向 Cursor IDE 等 AI 开发工具的提示词。README 详细记录 S2S 可观测性导出到 /otlp 路由的 token 契约与配置限制（如 Python/Node 样例仅含 client-secret 流程、无托管标识选项）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种语言的生产就绪示例 agent（可观测性/通知/工具/托管）
- S2S 可观测性导出到 /otlp 路由的 token 契约与验证记录
- 面向 Cursor IDE 等 AI 开发工具的提示词
- E2E 工作流记录各样例使用的 SDK 版本

## 适用场景

- 学习 Agent 365 SDK 的 agent 构建模式
- 参考 S2S 可观测性导出的认证配置
- 配合 Cursor IDE 加速 agent 开发

## 场景标签

`提示工程` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L3: This repository contains sample agents and prompts for building with the Microsoft Agent 365 SDK. The Microsoft Agen
> L42: - **Sample Agents**: Production-ready examples in C#/.NET, Python, Node.js/TypeScript, and Salesforce/Apex demonstr

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Agent365-Samples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 111 --> 113
    line [112, 112]
```

2026-10-18 112 → 2026-10-27 112（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2c4f262e8108` · [字段定义](../../DATASET.md)*
