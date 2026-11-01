# deepseek-ai/dsh-superagent-prototype

⭐ 1,741 · TypeScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/deepseek-ai/dsh-superagent-prototype) · 组织维护

**面向单仓库的主动编码 agent 原型，打包为 DeepSeek Harness bundle**

DeepSeek 团队发布的研究原型：dsh-superagent 是针对单个 GitHub 仓库的主动编码 agent，以 DeepSeek Harness bundle 形式打包。它监听 GitHub（可选 Feishu），在获授权者提出工作请求后开启工作项、在独立 agent 会话与目录中执行，并以 pull request 等形式回到原对话回复；配套 Web 面板提示需人工处理的事项。仅在被请求或命中团队规则时行动。README 声明为研究代码，非官方产品、非生产就绪。安装由 coding agent 引导按 SETUP.md 分步完成；开发用 pnpm check。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 监听 GitHub/Feishu，在独立会话与目录中执行工作项并以 PR 回复
- 仅在被人请求或命中团队编写的规则时行动
- Web 面板展示需人工介入的事项
- 安装流程由 coding agent 按 SETUP.md 引导完成

## 适用场景

- 让 agent 在获授权后代为处理仓库内的编码任务
- 团队以规则约束 agent 的触发与发言，减少注意力消耗
- 通过 Web 面板跟进需要人工决策的工作项

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness. It 
> L9: It is also a way of working with an agent: **take as little human attention as possible, and give as much value as p


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a98ec95e2159` · [字段定义](../../DATASET.md)*
