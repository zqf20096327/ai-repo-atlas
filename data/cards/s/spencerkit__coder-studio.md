# spencerkit/coder-studio

⭐ 37 · TypeScript · MIT · 推送 2026-08-27 · [GitHub](https://github.com/spencerkit/coder-studio) · 组织维护 · 中文 README

**自托管的浏览器 AI 编码 agent 工作台，支持跨设备接续**

面向使用编码 agent 的开发者：把 Claude Code、Codex、Gemini CLI、Cursor Agent、OpenCode 等 CLI agent 会话与编辑器、PTY 终端、Git diff 审查、Supervisor 循环、Work Analysis 和 Skills 管理整合进一个本地运行的浏览器工作台。核心机制是目标驱动的监督循环、可审查的 AI 改动 diff、以及同一工作区 URL 在桌面/平板/手机间接续。声明自身非云端 IDE、非 VS Code 替代、非模型提供方。需 Node.js ≥ 24，agent CLI 为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从同一工作区启动 Claude Code、Codex、Gemini CLI、Cursor Agent、OpenCode 等 agent 会话
- Supervisor 循环对长任务做目标驱动的评估与跟进
- 同一工作区可在桌面、平板、手机间接续访问
- Work Analysis 回顾活动模式、瓶颈与 Skills 候选；Skills 管理安装可复用工作流

## 适用场景

- 在桌面启动 agent 任务，通勤时用手机查看进度与改动
- 让 Supervisor 推进长时间运行的多步 AI 任务
- 在会话旁审查 Git diff 后决定接受或拒绝 AI 改动
- 用 Skills 管理让 agent 复用固定的工作流指令

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: **Self-hosted browser workspace for AI coding agents.**
> L35: Coder Studio is not a cloud IDE, not a VS Code replacement, and not an AI model provider. It is a self-hosted workb
> L117: |**Popular Coding Agents**|Run Claude Code, Codex, Gemini CLI, Cursor Agent, OpenCode, and CLI-style agents from o

## 星数曲线

```mermaid
xychart-beta
    title "spencerkit/coder-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `48ee99292c20` · [字段定义](../../DATASET.md)*
