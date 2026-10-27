# NPC-Worldwide/incognide

⭐ 477 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/NPC-Worldwide/incognide) · [官网](https://incognide.com) · 组织维护

**聚合聊天/代码/文档/浏览的本地优先 AI 工作台，可接本地或云端模型**

Electron 桌面应用，将聊天、代码编辑与执行、终端、PDF 阅读批注、浏览器、Office 文档编辑、STL 查看等组织为可平铺的工作区，每个标签页保持独立状态，并自动保存工作区。AI 部分包括：NPC agent 编辑与定时任务、记忆管理、知识图谱演化、结合自然语言与代码的 Jinx 自动化模板，以及基于对话数据的文本模型微调。模型接入提供三种路径：无 AI 纯工作区、云端 API key、本地运行时（Ollama/LM Studio/llama.cpp/oMLX，内置探测端口与二进制检测、Start/Stop 管理）；微调需指定外部 Python venv 安装 torch 等重依赖。Linux/macOS/Windows 提供安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天/代码/终端/PDF/浏览器/Office 的平铺工作区，标签页独立状态并自动保存
- 本地运行时探测与管理（Ollama/LM Studio/llama.cpp/oMLX 端口与二进制检测、启停按钮）
- NPC agent 编辑、定时任务、记忆 CRUD 与知识图谱演化
- Jinx 自动化：自然语言提示与可模板化代码（jinja）链接执行

## 适用场景

- 在一个工作区内完成编码、文档编辑、PDF 批注与网页浏览而不切换应用
- 管理本地模型运行时并让 agent 在定时任务中调用
- 用对话和记忆数据在本地微调文本模型

## 场景标签

`知识图谱` `微调` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L42:  - **No AI** — workspace only (files, code, browsers, terminals, docs, maps). No model calls.
> L44:  - **Local AI** — Ollama / LM Studio / llama.cpp / oMLX running on your machine.

## 星数曲线

```mermaid
xychart-beta
    title "NPC-Worldwide/incognide 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 475 --> 478
    line [476, 477, 477]
```

2026-10-18 476 → 2026-10-27 477（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `298a80e0bfd6` · [字段定义](../../DATASET.md)*
