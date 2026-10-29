# renatogalera/ai-commit

⭐ 22 · Go · MIT · 推送 2026-03-25 · [GitHub](https://github.com/renatogalera/ai-commit) · [官网](https://renatogalera.github.io/ai-commit/) · 个人维护

**用 AI 生成 Conventional Commits 提交信息的 Git CLI 工具**

Go 编写的终端工具，围绕 Git 工作流提供三项核心功能：生成符合 Conventional Commits 的提交信息、对暂存 diff 做 AI 代码审查、审查/约束提交信息风格。支持 OpenAI（默认）、Google Gemini、Anthropic Claude、DeepSeek、Ollama、OpenRouter 六类提供方，通过 --provider/--model/API key 环境变量配置。附带 TUI 交互界面、非交互模式、变更日志生成、语义化版本辅助、Git hook 集成与按分支名自动提取工单号。限制：diff 与提示词会发送至所配置的提供方；流式提供方在 TUI 内的风格审查尚未实现。

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

- 生成符合 Conventional Commits 的提交信息并支持 TUI 交互精修
- 对暂存 diff 的 AI 代码审查与提交信息风格审查
- 支持 OpenAI/Google/Anthropic/DeepSeek/Ollama/OpenRouter 六类提供方
- Git hook 集成、changelog 生成、语义化版本辅助与工单号自动提取

## 适用场景

- 让 AI 根据暂存改动自动生成规范的提交信息
- 提交前对代码 diff 快速跑一轮 AI 审查
- 在 CI/脚本中非交互地生成提交信息或变更日志

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: * Generate **Conventional Commits**-compliant messages
> L13: * **OpenAI** (default)
> L17: * **Ollama** (local models)

## 星数曲线

```mermaid
xychart-beta
    title "renatogalera/ai-commit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-29 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0ea5a831e10c` · [字段定义](../../DATASET.md)*
