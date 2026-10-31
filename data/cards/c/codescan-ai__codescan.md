# codescan-ai/codescan

⭐ 68 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/codescan-ai/codescan) · [官网](https://pypi.org/project/codescanai) · 组织维护

**用 LLM 扫描代码库安全漏洞的 CLI/CI 工具**

面向开发者的代码安全扫描工具：调用 OpenAI、Gemini 或自托管 OpenAI 兼容服务（如 Ollama），逐文件扫描安全漏洞并给出修复建议。基于 Pydantic-AI 结构化 agent 输出 FileScanResult；支持全目录扫描、仅扫本地 git 变更（--changes_only）、扫描指定 PR 并将发现以行内评论形式发回 diff。可集成进 GitHub Actions，也提供本地 CLI。限制：大目录可能触发提供商速率限制，目前仅集成 GitHub。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐文件扫描的结构化 Pydantic-AI agent，输出类型化 FileScanResult
- 支持 OpenAI、Gemini 及自托管 OpenAI 兼容服务器（Ollama）
- PR 扫描发现以行内 review 评论回发到 diff 对应行
- diff 感知分析：变更行加 [CHANGED] 标记并保留全文件上下文

## 适用场景

- 在 CI/CD 流水线中自动扫描每个 PR 的安全漏洞
- 本地用 CLI 快速扫描目录或未提交的代码变更
- 用自托管模型在私有环境执行代码安全审查

## 场景标签

`网络安全` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L9: CodeScanAI utilizes a variety of AI models to scan your codebase for security vulnerabilities. It leverages powerful
> L21: - **Pydantic-AI agent scanner:** Files are now scanned one at a time by a structured AI agent, returning typed `Fil

## 星数曲线

```mermaid
xychart-beta
    title "codescan-ai/codescan 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 66 --> 69
    line [67, 68, 68]
```

2026-10-18 67 → 2026-10-31 68（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `66ae0621ebb3` · [字段定义](../../DATASET.md)*
