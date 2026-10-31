# ragnarok22/gsmart

⭐ 15 · TypeScript · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/ragnarok22/gsmart) · [官网](https://ragnarok22.github.io/gsmart/) · 个人维护

**用 AI 从 Git diff 生成 Conventional Commit 消息的终端工具**

面向使用 Git 的开发者的 CLI 工具：读取暂存 diff、分支名与项目约定（.gsmartrc.json、可导入 commitlint 规则），调用所选 AI 提供商生成 Conventional Commit 消息，用户可交互审查、编辑、要求修改、恢复历史候选后提交。支持 OpenAI/Anthropic/Gemini/Mistral/Fireworks/PlataformIA 六家托管提供商、ChatGPT 订阅登录，以及通过 OpenAI 兼容端点接入 Ollama/LM Studio 本地模型。提供 dry-run、JSON 输出、提交拆分规划、shell 补全等。需 Node.js 22.12.0+ 与 Git 2.25+，GPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 Git diff 生成 Conventional Commit 消息，支持编辑/优化/恢复候选
- 六家托管提供商 + ChatGPT 订阅登录 + Ollama/LM Studio 本地模型
- 团队约定通过 .gsmartrc.json 共享，兼容 commitlint 规则自动导入
- 提供 dry-run、无提示 JSON 输出与混合变更的提交拆分规划

## 适用场景

- 日常提交时自动生成符合 Conventional Commits 的消息
- 团队统一提交消息的类型、scope 与语言约定
- 在脚本/Git hooks 中以 JSON 输出集成生成流程

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: GSmart turns your Git diff into an AI-generated Conventional Commit. Review the suggestion, edit it, refine it with 
> L18: - **Choose your AI.** Use six hosted providers, ChatGPT subscription login, or local models through Ollama and LM S

## 星数曲线

```mermaid
xychart-beta
    title "ragnarok22/gsmart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4698009cf2ff` · [字段定义](../../DATASET.md)*
