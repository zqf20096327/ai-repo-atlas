# brave/pull-merge

⭐ 23 · JavaScript · MPL-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/brave/pull-merge) · 组织维护

**为 GitHub pull request 添加 LLM 能力的 GitHub Action**

puLL-Merge 是一个 GitHub Action，在 pull request 工作流中调用 LLM 对补丁进行解释等处理。使用方式为在 .github/workflow/security-action.yml 中添加该 Action 并配置触发 pull_request 事件。README 另提供本地测试路径：通过 ./run.js 分别运行 openaiExplainPatch.js 与 anthropicExplainPatch.js 脚本，传入 API key、仓库属主、仓库名与补丁内容进行调试。维护方为 brave 组织。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 GitHub Action 形式在 pull request 流程中调用 LLM
- 提供 OpenAI 与 Anthropic 两条本地调试脚本路径
- 通过 --apiKey/--owner/--repo/--patchBody 参数运行

## 适用场景

- 在 PR 流程中自动获得 LLM 对补丁的解释
- 开发者本地调试不同 LLM 提供方的集成效果

## 场景标签

 · 领域:开发工具/CI

## 证据(README 行号)

> L3: puLL-Merge is a `github-action` to add LLM capabilities to pull-requests in `github`
> L21: $ ./run.js ./src/openaiExplainPatch.js --apiKey=<OPENAI_KEY> --owner=<GITHUB_OWNER e.g. brave> --repo=<REPO> --patc
> L27: $ ./run.js ./src/anthropicExplainPatch.js --apiKey=<ANTHROPIC_API_KEY> --owner=<GITHUB_OWNER e.g. brave> --repo=<RE

## 星数曲线

```mermaid
xychart-beta
    title "brave/pull-merge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `7ef586e42aaf` · [字段定义](../../DATASET.md)*
