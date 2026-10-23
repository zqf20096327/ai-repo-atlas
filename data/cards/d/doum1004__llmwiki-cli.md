# doum1004/llmwiki-cli

⭐ 103 · TypeScript · MIT · 推送 2026-05-01 · [GitHub](https://github.com/doum1004/llmwiki-cli) · 个人维护

**供 LLM Agent 读写维基文件的命令行知识库工具**

npm 安装的 CLI，提供 wiki init/read/write/search/lint/links 等命令，让 Claude Code、Codex 等 LLM Agent 通过 shell 调用来创建和维护本地 markdown 个人知识库：页面含 frontmatter，支持 [[wikilinks]]、孤儿页检测、多 wiki 注册表与跨库搜索。关键机制是 CLI 自身不调用任何 LLM API，只读写磁盘上的 markdown，无内置 Git 同步或云端后端；可选步骤可将脚本复制进 wiki 仓库，通过 GitHub Actions 在 Pages 上发布 d3-force 链接图。要求 Node.js >= 18 或 Bun。

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

- 读写/搜索/lint/链接检查等完整 wiki 文件管理命令集
- CLI 不调用任何 LLM API，仅读写磁盘 markdown
- 全局注册表支持多 wiki 与 --all 跨库搜索
- 可选 GitHub Actions 工作流发布 d3-force 链接图

## 适用场景

- 让 Claude Code / Codex 等 agent 替我维护个人研究笔记维基
- 摄入论文等原始资料并整理为相互链接的概念页
- 用 lint/orphans 保持知识库链接健康

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L11: A CLI tool for LLM agents to build and maintain personal knowledge bases.
> L19: The CLI is the hands -- it reads, writes, searches, and manages wiki files. The LLM is the brain -- it decides what

## 星数曲线

```mermaid
xychart-beta
    title "doum1004/llmwiki-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 102 --> 104
    line [103, 103]
```

2026-10-18 103 → 2026-10-23 103（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `af369b365cb7` · [字段定义](../../DATASET.md)*
