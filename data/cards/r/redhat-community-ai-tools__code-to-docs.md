# redhat-community-ai-tools/code-to-docs

⭐ 23 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/redhat-community-ai-tools/code-to-docs) · 组织维护

**用 AI 让文档与代码保持同步的 GitHub Action**

在 Pull Request 上以评论命令触发的 GitHub Action：分析 PR 的 git diff，识别受影响的文档文件，生成 AsciiDoc/Markdown/reStructuredText 更新，通过复选框交互式评审后创建文档 PR。支持仓库级风格规则（style.md）与 JSON 配置。可接入任意 OpenAI 兼容 API（vLLM、Gemini、OpenAI、Ollama 等）。另有 spec-vs-code 分析：读取 Jira 工单及关联的 Confluence/Google Docs 规格，比对需求与实现差异。开发需 Python 3.12+ 与 uv。

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

- 评论命令触发：review-docs / update-docs / review-feature
- 支持任意 OpenAI 兼容 API 后端（vLLM/Gemini/OpenAI/Ollama）
- 复选框交互式评审后仅提交被接受的文档更新
- spec-vs-code 分析：比对 Jira 规格与 PR 变更（covered/missing/unplanned）

## 适用场景

- 代码改动后自动找出需要更新的文档并生成更新 PR
- 在评审中逐文件接受或拒绝 AI 生成的文档改动
- 核对 PR 实现是否覆盖 Jira 工单中的需求

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L8: AI-powered GitHub Action that automatically analyzes code changes and updates documentation using any OpenAI-compati
> L143: - 🤖 **AI-Powered Analysis** - Uses any OpenAI-compatible LLM to identify relevant docs

## 星数曲线

```mermaid
xychart-beta
    title "redhat-community-ai-tools/code-to-docs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c129969f2606` · [字段定义](../../DATASET.md)*
