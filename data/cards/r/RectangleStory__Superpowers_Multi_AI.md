# RectangleStory/Superpowers_Multi_AI

⭐ 76 · BSD-3-Clause · 推送 2026-09-14 · [GitHub](https://github.com/RectangleStory/Superpowers_Multi_AI) · 个人维护

**给 AI 编程助手的模块化提示词纪律框架，含 Windows 启动器**

面向使用 Cursor、Claude Code、GitHub Copilot 等编程助手的开发者的提示词工程框架：通过 skills/ 目录下的模块化提示文件（头脑风暴冻结架构、线性执行计划、隔离子代理、四步调试流程），约束 AI 按结构化 SDLC 流程工作。分发形式为 Dropbox 下载的 Superpowers.zip，解压到项目根目录后运行 Windows 可执行文件 run_launcher.exe，按目标环境生成 .cursorrules、.ai-skills.md/CLAUDE.md 或 copilot-instructions.md 配置。启动器本地运行、不联网传输数据；提供 FORCE_RAW_MODE 关键字临时绕过规则。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- skills/ 模块（头脑风暴/计划/子代理/调试）注入行为约束门
- run_launcher.exe 聚合技能为统一系统提示矩阵并按环境生成配置
- 支持 Cursor / Claude Code / GitHub Copilot / 本地模型（Ollama Modelfile）
- 启动器为本地独立可执行文件，不联网不回传遥测

## 适用场景

- 让 Cursor/Claude Code 等助手在写代码前先完成架构确认与计划
- 通过子代理隔离长上下文任务，控制上下文窗口污染
- 为本地 Ollama 模型配置结构化系统提示

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: Stop "vibe coding" and shifting your AI into chaotic, hallucinating loops. Superpowers AI is a production-grade, mod
> L68: ## Ecosystem Target Mapping
> L72: * **Cursor Editor:** Generates a project-level `.cursorrules` configuration file that forces the `Composer` and `Ch

## 星数曲线

```mermaid
xychart-beta
    title "RectangleStory/Superpowers_Multi_AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 74 --> 77
    line [75, 76, 76]
```

2026-10-18 75 → 2026-10-25 76（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `76d73a0a113c` · [字段定义](../../DATASET.md)*
