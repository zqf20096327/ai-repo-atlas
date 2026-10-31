# tang-vu/ContribAI

⭐ 246 · Rust · AGPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/tang-vu/ContribAI) · [官网](https://contribai-topaz.vercel.app/) · 个人维护

**面向维护者治理的 AI 开源贡献提案工具：证据与准入层**

Rust 实现的 CLI/TUI/MCP 工具，用于分析代码仓库并生成小规模可评审的变更，以 draft PR 形式提交。核心机制是维护者同意协议：需仓库 .github/contribai.yml 清单或 issue 标签授权才可提交；默认只读，写能力需显式开启，每次准入提案记录许可、基线版本、变更范围与校验结果为证据胶囊，并有本地哈希链审计账本。支持 Gemini/OpenAI/Anthropic/Ollama 等多提供商 LLM，Tree-sitter 支持 13 种语言分析。限制：不代签 CLA、不合并代码，PR 始终为 draft。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 维护者同意协议（仓库清单或 issue 标签）+ 准入门控，未授权即拒绝
- 证据胶囊与 SHA-256 哈希链本地审计账本，提案可复现可核查
- 默认只读，提交需 --submit、操作者交互批准，PR 始终为 draft
- 多提供商 LLM 支持（Gemini/OpenAI/Anthropic/Ollama/Vertex/Copilot 路由），Tree-sitter 分析 13 种语言

## 适用场景

- 我想让 AI 帮忙准备可评审的小型开源贡献，但由维护者授权控制准入
- 作为仓库维护者，我希望以清单和标签方式控制外部 AI 贡献的路径与规模
- 离线运行 demo 验证准入与证据链路，无需 token 与 LLM key

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: ContribAI analyzes repositories and prepares small, reviewable changes. It does **not** treat a
> L261: - Multi-provider LLM support: Gemini, OpenAI, Anthropic, Ollama, Vertex AI, and Copilot routing

## 星数曲线

```mermaid
xychart-beta
    title "tang-vu/ContribAI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 244 --> 247
    line [245, 246, 246]
```

2026-10-18 245 → 2026-10-31 246（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `598ef36c97b8` · [字段定义](../../DATASET.md)*
