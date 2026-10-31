# microsoft/vscode-websearchforcopilot

⭐ 64 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/microsoft/vscode-websearchforcopilot) · 组织维护

**为 GitHub Copilot 提供网页搜索能力的 VS Code 扩展示例**

微软发布的 VS Code 扩展示例，演示 Chat Participant 与 Tool API、prompt-tsx、调用 GitHub Copilot 提供的语言模型，以及用 VS Code 认证与 Secret Storage API 管理用户 API key。扩展贡献 @websearch 聊天参与者和 #websearch 聊天工具，通过 Tavily 搜索引擎获取网络实时信息；需用户自备 Tavily API key，首次使用时录入并安全存储。支持意图检测自动触发，其他参与者也可通过 vscode.lm.invokeTool API 调用该工具。

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

- 贡献 @websearch 聊天参与者与 #websearch 聊天工具
- 由 Tavily 搜索引擎驱动，需用户 API key
- 演示 Secret Storage API 安全存储密钥与 prompt-tsx
- 可通过 vscode.lm.invokeTool 被其他 Chat Participant/Tool 调用

## 适用场景

- 在 Copilot 对话中直接查询需要实时网络信息的问题
- 为其他聊天参与者提供网页上下文
- 学习 VS Code Chat Participant 与 Tool API 的实现方式

## 场景标签

`语义搜索` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L5: * Chat Participant & Tool APIs
> L7: * How to leverage the language models provided by GitHub Copilot

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/vscode-websearchforcopilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-31 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e12045422949` · [字段定义](../../DATASET.md)*
