# KacemMathlouthi/metis

⭐ 20 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/KacemMathlouthi/metis) · [官网](https://www.getmetis.tech) · 个人维护

**自托管的 GitHub AI 代码审查平台：自动审查 PR、把 issue 变成 PR**

自行托管的 GitHub App：PR 打开或更新时，agent 在隔离的 Daytona 沙箱中克隆分支、读取代码、运行测试与 linter，在 diff 上以严重度和分类标注形式内联发布发现，并生成摘要审查；另一流程由编码 agent 从 issue 出发完成分支、编辑、测试、提交与开 PR，运行过程可回放。通过 LiteLLM 支持任意模型（Gemini、GPT、Claude、Mistral、Azure OpenAI 等）。需 Docker、GitHub App、LLM API key 与 Daytona API key，用 make dev 启动 API、worker、dashboard、PostgreSQL 与 Redis。

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

- agent 在隔离 Daytona 沙箱中克隆分支并运行测试/linter，内联发布带严重度与分类的发现
- 按需把 issue 转为 PR：编码 agent 完成分支、编辑、测试、提交与推送，运行可回放
- 第二个 agent 重写 PR 标题与描述
- 通过 LiteLLM 支持任意模型；每个仓库可配置敏感度、自定义指令与忽略模式

## 适用场景

- 团队为每个 PR 自动获得带严重度标注的 AI 代码审查
- 在 dashboard 中选定 issue，让 agent 直接产出对应 PR
- 在自托管环境接入自有 LLM 做 PR 标题与摘要生成

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: - **Review a pull request (automatic).** When a PR is opened or updated, an agent clones the branch into an isolate
> L11: - **Turn an issue into a PR (on demand).** Pick an issue in the dashboard and a coding agent branches, edits, tests
> L13: It works with any model LiteLLM supports (Gemini, GPT, Claude, Mistral, Azure OpenAI, and more), and every reposito

## 星数曲线

```mermaid
xychart-beta
    title "KacemMathlouthi/metis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8bfd4e2c3cb9` · [字段定义](../../DATASET.md)*
