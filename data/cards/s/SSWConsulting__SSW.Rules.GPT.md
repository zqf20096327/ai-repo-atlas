# SSWConsulting/SSW.Rules.GPT

⭐ 24 · C# · 推送 2026-08-20 · [GitHub](https://github.com/SSWConsulting/SSW.Rules.GPT) · [官网](https://rulesgpt.ssw.com.au) · 组织维护

**基于 OpenAI API 的 SSW Rules 问答机器人（Blazor + ASP.NET Core）**

SSW 公司开发的 GPT 问答机器人：用 OpenAI embeddings 检索匹配的 SSW Rules，将前 10 条结果注入 ChatGPT API 生成回答。前端为 Blazor WASM，后端为 ASP.NET Core WebAPI，使用 EF Core 与数据库连接串。安装需配置 OpenAI API key 与数据库连接，分别运行 WebAPI 与 WebUI 项目（端口 5002，若本地跑 Identity Server 有端口约束）。代码合并到 main 后自动部署到 staging。README 本身由 SSW Rules GPT 生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI embeddings 检索 SSW Rules 并将 top 10 结果注入 ChatGPT API
- Blazor WASM 前端 + ASP.NET Core WebAPI 后端，C# 实现
- 支持 Visual Studio/Rider 多启动项目运行
- 合并 main 后自动部署至 Azure staging 环境

## 适用场景

- 向机器人提问并获取基于 SSW Rules 的回答
- 作为 .NET 技术栈集成 OpenAI API 的参考实现

## 场景标签

`RAG` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L12: Our project is a GPT Bot that uses OpenAI embeddings to search for matching SSW Rules, and then feeding the top 10 

## 星数曲线

```mermaid
xychart-beta
    title "SSWConsulting/SSW.Rules.GPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7e42c2efb104` · [字段定义](../../DATASET.md)*
