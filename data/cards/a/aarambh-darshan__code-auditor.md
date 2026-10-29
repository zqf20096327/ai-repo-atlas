# aarambh-darshan/code-auditor

⭐ 20 · Rust · 推送 2026-01-06 · [GitHub](https://github.com/aarambh-darshan/code-auditor) · 个人维护

**用 Rust 与 Ollama 的 agent 化代码审计 CLI，产出 Markdown 报告**

基于 Rust 的命令行代码审计工具：通过 Ollama 的 tool-calling API 让 LLM 以 agent 方式自主探索代码库——调用 list_files、read_file、search_code 等工具发现并分析源码，再经 report_issue 上报问题。检测范围包括安全漏洞、逻辑错误、空指针风险、竞态条件与性能问题，生成带行号的 Markdown 审计报告。前提是需本地安装 Rust 工具链（从源码编译）、Ollama 或 llama.cpp server 后端，且模型必须支持 tool calling。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 化分析：LLM 自主调用 list_files/read_file/search_code 等工具探索代码库
- 检测安全漏洞、逻辑错误、竞态条件与性能问题
- 生成带行号的 Markdown 审计报告
- 支持 .code-auditor.toml 项目级配置

## 适用场景

- 我对 GitHub 仓库做安全与 bug 扫描并拿到可读报告
- 我在本地用 Ollama 模型离线审计代码，不上传代码
- CI 或日常流程中生成结构化的代码审计文档

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L3: AI-powered GitHub repository analyzer that uses **tool-calling agents** with Ollama to analyze source code and gener
> L19: - 🤖 **Agentic Analysis**: LLM autonomously explores and analyzes the codebase
> L20: - 🛠️ **Tool Calling**: Uses Ollama's tool-calling API for structured interactions

## 星数曲线

```mermaid
xychart-beta
    title "aarambh-darshan/code-auditor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7d46e80de2fc` · [字段定义](../../DATASET.md)*
