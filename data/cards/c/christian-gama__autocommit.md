# christian-gama/autocommit

⭐ 46 · Go · MIT · 推送 2026-06-09 · [GitHub](https://github.com/christian-gama/autocommit) · 个人维护

**用 AI 从暂存改动生成 Git 提交信息的 CLI 工具**

Go 编写的命令行工具：读取 staged diff，调用 LLM 生成 commit message，交互式选择提交、复制、按新指令重生成或退出。支持 OpenAI、Ollama、Mistral、Google AI、Groq 五类提供商，通过 `autocommit configure` 本地保存凭据与模型选择；提供可编辑的提示词模板与 Bash/Zsh/Fish/PowerShell 补全脚本。README 提示大 diff 会稀释效果，建议保持提交聚焦并选用推理能力较强的模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 staged diff 生成 commit message，支持提交/复制/重生成/追加指令
- 五种提供商可选（OpenAI、Ollama、Mistral、Google AI、Groq）
- 可编辑的提示词模板与四种 shell 补全脚本
- Ollama 本地通道无需 API key，需本地下载模型

## 适用场景

- 我不想手写 commit message，让 AI 依据 diff 生成
- 团队统一提交信息风格，通过自定义指令模板约束
- 本地 Ollama 模型离线生成提交信息，不外发代码

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: AutoCommit generates git commit messages from your staged changes using AI. It currently supports OpenAI, Ollama 2, 
> L7: - AI-driven commit messages based on diffs

## 星数曲线

```mermaid
xychart-beta
    title "christian-gama/autocommit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b5a2b045f3f6` · [字段定义](../../DATASET.md)*
