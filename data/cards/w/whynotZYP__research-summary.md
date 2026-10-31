# whynotZYP/research-summary

⭐ 31 · JavaScript · 推送 2026-05-25 · [GitHub](https://github.com/whynotZYP/research-summary) · 个人维护 · 中文 README

**面向 Claude Code/Codex CLI 的科研项目技术总结文档生成 Skill**

跨平台 AI Agent Skill，安装到 Claude Code 或 OpenAI Codex CLI 后使用。通过主动提问的工作流引导学生逐步整理课题项目信息，产出技术总结笔记、过程记录文档、可选录屏与项目文件压缩包共 4 件交付物，内置统一排版的 .docx 模板与 pack.py 一键打包脚本。宣称适用于所有专业（机械、化学、计算机、社科等），验收标准为他人仅凭文档可完整复现项目。需先安装 Claude Code 或 Codex CLI 之一方可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模板填空式提问工作流，产出 4 件套技术文档
- 统一 .docx 模板输出（预设字体、配色、封面、页眉页脚）
- pack.py 自动打包项目文件并跳过 .git、node_modules 等
- 双平台兼容：Claude Code 与 Codex CLI 功能一致

## 适用场景

- 毕业设计或课题结束后按导师要求整理可复现的技术文档
- 实验报告、课程设计文档的结构化整理
- 为代码项目、数据分析项目产出交接文档与过程记录

## 场景标签

`科研工具` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: 一个跨平台 AI Agent Skill（支持 **Claude Code** 和 **OpenAI Codex CLI**），**适用于所有专业**。帮助你在课题项目完成后，按导师要求产出**别人可以完整复现**的技术文档包。
> L24: - **双平台兼容** — Claude Code 和 Codex CLI 都能用，`agents/openai.yaml` 已包含触发示例和行为约束
> L31: 任选其一即可，Skill 在两个平台上功能一致。

## 星数曲线

```mermaid
xychart-beta
    title "whynotZYP/research-summary 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `50ec1a7a46ee` · [字段定义](../../DATASET.md)*
