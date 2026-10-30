# hanishrao/context-kit

⭐ 15 · TypeScript · AGPL-3.0 · 推送 2026-03-22 · [GitHub](https://github.com/hanishrao/context-kit) · [官网](https://ck.collectiveai.tools) · 个人维护

**为开发技术栈生成 AI 助手配置文件与 ADR 的 Web 工具**

面向使用 AI 编程助手的开发者：在网页上选择所用技术栈与助手（Claude Code、Cursor、Windsurf、GitHub Copilot、Gemini CLI），下载 zip 包，内含主配置文件（CLAUDE.md、.cursorrules 等）、每工具的技能文件、预写好的架构决策记录（ADR）、.env.example 与 /plan、/adr 等 slash 命令文件。也可用 README 提供的提示词或手动步骤为既有项目生成。本地开发用 npm，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按所选技术栈与助手生成主配置文件、技能文件与 ADR
- 生成 /plan、/adr、/architecture、/code-review 等 slash 命令文件
- /architecture 命令可重复运行以更新 ARCHITECTURE.md
- 提供即贴提示词与手动分步设置两种替代路径

## 适用场景

- 为新项目快速生成 AI 助手的上下文配置
- 为既有代码库补齐 AI 配置文件与架构决策记录
- 让团队通过 ADR 保留技术选型的决策上下文

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: > Generate AI context for your dev stack — works with Claude Code, Cursor, Windsurf, GitHub Copilot, Gemini CLI, or 
> L11: Pick your tools. Pick your AI assistant. Download a zip with:
> L23: # 1. Go to context-kit, pick your stack and assistant, download the zip

## 星数曲线

```mermaid
xychart-beta
    title "hanishrao/context-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1d6b645fd75c` · [字段定义](../../DATASET.md)*
