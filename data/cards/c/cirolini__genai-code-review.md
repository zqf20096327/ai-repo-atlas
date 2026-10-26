# cirolini/genai-code-review

⭐ 372 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/cirolini/genai-code-review) · 个人维护

**用 LLM 审查 PR diff 并在 PR 上发内联评论的 GitHub Action**

面向使用 GitHub 的开发团队的代码审查 Action：读取 pull request 的 diff，交给 LLM（Gemini/OpenAI/Anthropic 或任意 OpenAI 兼容服务）分析，把符合 JSON schema 的 findings 按严重度排序，受 max_comments 评论预算限制（默认 5 条）以内联评论形式贴出，未贴出的在置顶汇总中列出。支持增量审查、双模型 panel 实验模式、.genai-review.yml 仓库配置、每轮 JSON 运行日志，并将 diff 视为不可信数据做提示注入防护。仅需一个 workflow 文件即可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 评论预算机制：按严重度/置信度排序，默认只贴 5 条，被扣下的 findings 在汇总中列明
- 支持 gemini/openai/anthropic/openai-compatible（覆盖 Ollama、vLLM、Azure OpenAI 等）
- diff 以随机哨兵围栏与指令后置方式防护提示注入，模型输出经 schema 校验并对齐 diff
- 每轮运行输出含 token、成本、延迟、贴出/扣下数量的 JSON 运行日志

## 适用场景

- 在 CI 里让 LLM 自动审查 pull request 并贴出内联评论
- 团队希望 AI 审查只报最值得人看的少数问题，避免评论噪音
- 用本地或自托管模型（Ollama/vLLM）做代码审查，diff 不外发

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: A GitHub Action that reviews pull request diffs with an LLM and posts inline
> L4: comments. It works with OpenAI, Anthropic, Google Gemini, or any
> L66: |`provider`|Default model|Key read from|

## 星数曲线

```mermaid
xychart-beta
    title "cirolini/genai-code-review 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 370 --> 373
    line [371, 372, 372]
```

2026-10-18 371 → 2026-10-26 372（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `14da82a809ba` · [字段定义](../../DATASET.md)*
