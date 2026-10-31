# misospace/pr-reviewer-action

⭐ 20 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/misospace/pr-reviewer-action) · 个人维护

**AI 辅助 GitHub PR 审查 Action：接入任意 OpenAI/Anthropic 兼容模型**

可复用的 GitHub Action，在每个 pull request 上运行模型审查：收集 diff、关联 issue、CI 结果与仓库规范，通过有界的只读工具循环让模型读取检出代码、检索 git 历史并调用 GitHub API/MCP，最终以原生 review 或置顶评论发布结构化结论。后端支持 ollama、llama.cpp、vLLM、LiteLLM 或任何 OpenAI/Anthropic 兼容端点（含可选回退模型），可配置正确性/安全/测试三类专业模型角色与独立的置信度评分调用。运行于 GitHub 与 Forgejo，Forgejo 部分功能经 REST 降级。作为 JavaScript Action（node24）由 runner 提供 Node，无需额外安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地模型优先：ollama/llama.cpp/vLLM/LiteLLM 或任意 OpenAI/Anthropic 兼容端点，可选回退模型
- 原生工具循环自行取证：读文件、grep、追 git 历史、调 GitHub API/MCP，预算随 PR 规模伸缩
- 规则化风险分类与确定性上限；未读完代码的 review 会声明且从不批准
- diff 未变时跳过模型调用并沿用先前结论；可选独立置信度评分（0–5）为附加建议不改判定

## 适用场景

- 在 CI 中对每个 PR 自动获得带证据的模型审查
- 用自托管 llama.cpp/ollama 端点做不外发代码的 PR 审查
- 为正确性/安全/测试角色配置不同的专用模型

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: **AI pull request reviews with any OpenAI- or Anthropic-compatible model — cloud or self-hosted.**
> L13: The action reviews each pull request with the model you point it at. It collects the diff, linked issues, CI result
> L17: - 🏠 **Local-model-first**: ollama, llama.cpp, vLLM, LiteLLM, or any OpenAI/Anthropic-compatible endpoint, with an o

## 星数曲线

```mermaid
xychart-beta
    title "misospace/pr-reviewer-action 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fff209d3a637` · [字段定义](../../DATASET.md)*
