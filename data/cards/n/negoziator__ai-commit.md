# negoziator/ai-commit

⭐ 21 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/negoziator/ai-commit) · 个人维护

**给开发者的 CLI 工具：用 LLM 生成 git 提交信息**

基于 Node.js（v20 以上）的 npm CLI 工具 aicommit，读取已暂存的代码变更，调用 LLM 生成 git 提交信息；支持 OpenAI（默认）、Anthropic、Azure OpenAI、Ollama 本地模型及自定义端点（LM Studio/LocalAI/vLLM 等 OpenAI 兼容 API）。可作为 prepare-commit-msg Git 钩子自动生成；可配置语言、信息数量、长度上限、Conventional Commits 类型、温度等，支持 .env 与项目级 .ai-commit.json 覆盖配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分析暂存变更生成提交信息，可装为 Git 钩子自动运行
- 多 LLM 提供方：OpenAI/Anthropic/Azure OpenAI/Ollama/自定义端点
- Conventional Commits 类型、多语言、信息长度与温度等可配置
- 项目级 .ai-commit.json 提供项目上下文并覆盖全局配置

## 适用场景

- 提交时让 AI 生成符合规范的 commit message
- 通过 Git 钩子在每次 commit 前自动生成提交信息
- 用 Ollama 本地模型离线生成提交信息

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3:  A powerful CLI tool that uses AI to generate meaningful, insightful git commit messages based on your code changes.
> L16: - 🔌 **Multiple LLM Providers**: Choose from OpenAI, Anthropic, Azure OpenAI, Ollama, or custom endpoints

## 星数曲线

```mermaid
xychart-beta
    title "negoziator/ai-commit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `41708f2518e3` · [字段定义](../../DATASET.md)*
