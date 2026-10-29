# Mattbusel/LLM-Hallucination-Detection-Script

⭐ 19 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Mattbusel/LLM-Hallucination-Detection-Script) · [官网](https://mattbusel.github.io/LLM-Hallucination-Detection-Script/) · 个人维护 · 中文 README

**从 token logprobs 标记 LLM 回答低置信片段的 Rust CLI/库**

Rust 编写的 CLI 与库（crate 名 llm-token-visualizer）：读取模型自身的 token logprobs，将低概率词元标红并显示模型曾考虑的替代候选，输出终端热图、HTML、Markdown、JSON 或 CI 退出码，无需第二次 LLM 调用。支持离线分析保存的响应，或经 --live 对接任意返回 logprobs 的 OpenAI 兼容 API（OpenAI/OpenRouter/Together/vLLM/Ollama），也可解析 Gemini logprobsResult。文档明确局限：模型可能高概率地错（moonwalk 示例），工具用于决定优先核查何处而非认证回答。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于单次响应的 logprobs 标记低置信词元并显示替代候选
- 输出终端/HTML/Markdown/JSON 及 CI 门禁（--fail-on-flag、hallucination-gate 组件）
- Unicode 分词支持任意语言，单个不确定字符可被单独标记
- 可作 Rust 库使用，含 async-openai 互操作 feature

## 适用场景

- 在 CI 中对保存的 LLM 回答做低置信词门禁
- 人工复核 AI 回答前定位需优先核查的片段
- 生成可分享给评审的 HTML/Markdown 置信度报告

## 场景标签

`模型评测` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L13: For anyone who ships or checks LLM answers: developers, evaluators, and CI pipelines. Works with OpenAI, OpenRouter
> L70: There is no other Rust crate for logprob-based confidence checks. In Python, LM-Polygraph and UQLM offer many more 
> L76: 3. **Share or gate it:** `--format html -o report.html` for a page you can send, `--format markdown` for a PR comme

## 星数曲线

```mermaid
xychart-beta
    title "Mattbusel/LLM-Hallucination-Detection-Script 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8244335095b9` · [字段定义](../../DATASET.md)*
