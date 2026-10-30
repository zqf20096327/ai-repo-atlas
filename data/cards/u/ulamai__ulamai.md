# ulamai/ulamai

⭐ 162 · Python · 推送 2026-08-09 · [GitHub](https://github.com/ulamai/ulamai) · [官网](https://ulam.ai) · 组织维护

**LLM 引导的 Lean 4 定理证明与形式化 CLI**

开源 Lean 4 定理证明器命令行工具：LLM 提出证明步骤（tactic/lemma/llm 三种模式），由 Lean 验证仅接受通过检查的证明，支持从 mathlib/本地仓库做前提检索与 best-first/beam 搜索加缓存。可将 LaTeX 论文形式化为 Lean，可接入 Codex/Claude Code/Gemini CLI/Ollama。提供 Homebrew、安装脚本与 Colab 教程，Lean 后端可选 dojo/cli/lsp。v0.2.11 明确列出尚未实现项（鲁棒价值模型、完整自动形式化流程）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 提议 + Lean 机器检查，未通过检查的证明不予接受
- tactic/lemma/llm 三种证明模式与 dojo/cli/lsp 三种 Lean 后端
- LaTeX 文档形式化为 Lean，含语义完整性检查与分段选项
- LLM 适配器支持 OpenAI 兼容、Anthropic、Gemini、Ollama 与 CLI 包装

## 适用场景

- 用自然语言指导生成机器检查的 Lean 4 证明
- 把 LaTeX 数学论文或竞赛证明形式化为 Lean 代码
- 运行可复现的 miniF2F 等基准测试与回归对比

## 场景标签

 · 领域:数学/形式化验证

## 证据(README 行号)

> L3: A **truth-first**, reproducible, open-source **Lean 4 theorem prover CLI** that combines:
> L6: - **Lean verification** (zero hallucinations: only accepted if Lean checks)
> L83: - LLM adapters: OpenAI-compatible + Anthropic + Gemini + Ollama + CLI wrappers

## 星数曲线

```mermaid
xychart-beta
    title "ulamai/ulamai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 161 --> 163
    line [162, 162]
```

2026-10-18 162 → 2026-10-30 162（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `14bfe2682d79` · [字段定义](../../DATASET.md)*
