# resume-llm/resume-ai

⭐ 394 · JavaScript · MIT · 推送 2026-09-21 · [GitHub](https://github.com/resume-llm/resume-ai) · 个人维护

**本地优先的求职管理与 AI 简历生成工具**

以 Docker Compose 部署的本地求职工作台：看板跟踪职位申请，粘贴职位描述后由 LLM 生成简历草稿，支持多版本保存到申请卡片，并经 Pandoc 导出 PDF/DOCX（含 ATS 隐藏内容警告）。AI 提供方三选一：本地 Ollama、Ollama Cloud 或任意 OpenAI 兼容端点；提示词以 Markdown 文件存放可直接编辑。附带 AI 看板摘要、申请标签与下一步建议，组件含前端、Node 后端、Kanban API 与 MLflow UI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 看板管理职位申请（CRUD、拖动、行内编辑）
- LLM 生成简历草稿并给出 ATS 隐藏内容警告
- 经 Pandoc 导出 PDF/DOCX，多版本关联申请卡片
- 支持本地 Ollama / Ollama Cloud / OpenAI 兼容端点三种提供方模式

## 适用场景

- 我在找工作时跟踪各职位申请进度
- 针对具体职位描述快速生成并迭代简历草稿
- 把每份工作的简历版本集中保存并导出投递

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L6: - generate and edit resumes for specific roles
> L10: The stack runs entirely in Docker Compose and supports three AI provider modes: local Ollama, Ollama Cloud, or any 
> L66: - Resume generation with ATS hidden-content warnings

## 星数曲线

```mermaid
xychart-beta
    title "resume-llm/resume-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 393 --> 395
    line [394, 394]
```

2026-10-18 394 → 2026-10-24 394（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fb6989baefe5` · [字段定义](../../DATASET.md)*
