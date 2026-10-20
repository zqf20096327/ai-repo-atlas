# ghbalf/freecad-ai

⭐ 577 · Python · LGPL-2.1 · 推送 2026-10-16 · [GitHub](https://github.com/ghbalf/freecad-ai) · 个人维护

**FreeCAD 的 AI 助手工作台：用自然语言生成并执行 3D 建模代码**

作为 FreeCAD 工作台安装的 AI 助手插件：通过聊天界面接收自然语言描述，由 LLM 生成 Python 代码在 FreeCAD 中执行以创建 3D 模型。提供 Plan/Act 两种模式、50 个结构化 FreeCAD 工具调用、技能系统、视觉路由与上下文压缩；支持 24 个 LLM 提供商（含本地 Ollama 与任意 OpenAI 兼容端点），仅依赖 Python 标准库。声明为 Alpha 阶段，可能出现破坏性变更与 LLM 代码导致的 FreeCAD 崩溃；需 FreeCAD 1.0+，通过克隆仓库至 Mod 目录（符号链接）安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言生成并执行 Python 代码创建 3D 模型，Plan 模式可在执行前审查代码
- 24 个 LLM 提供商 + 任意 OpenAI 兼容端点，含本地 Ollama
- 50 个结构化 FreeCAD 工具调用与技能系统（含技能自动优化循环）
- 仅依赖 Python 标准库，零外部依赖

## 适用场景

- 用自然语言描述需求让 AI 在 FreeCAD 中生成 3D 模型
- 通过工具调用模式进行更可控的结构化建模操作
- 在断网或敏感场景下接本地 Ollama 模型使用

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: An AI-powered assistant workbench for FreeCAD that generates and executes Python code to create 3D models from natur
> L24: - **24 LLM providers** — Anthropic, OpenAI, Ollama, Gemini, OpenRouter, Requesty, Cloudflare Workers AI, Moonshot, 

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `ddd9199c2b74` · [字段定义](../../DATASET.md)*
