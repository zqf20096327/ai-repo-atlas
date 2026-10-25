# massimodeluisa/recursive-decomposition-skill

⭐ 53 · HTML · MIT · 推送 2026-09-11 · [GitHub](https://github.com/massimodeluisa/recursive-decomposition-skill) · [官网](https://arxiv.org/abs/2512.24601) · 个人维护

**让 Claude Code 等 agent 递归分解长上下文任务的 Agent Skill**

基于 Recursive Language Models 研究的 Agent Skill，面向 Claude Code、Codex、Cursor 及兼容 agent：将代码库级、多文档、PDF 堆等长上下文任务按 size→filter→chunk→递归子代理→验证→合成的协议处理，每批次由一个子代理携带独立简报执行，子代理不再派生。PDF 先经 anydoc 转为 markdown 再 grep。通过 skills CLI、Claude Code 插件命令或手动复制安装；附带基于 131 份公开领域房贷 PDF 语料的评测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 步协议：sizing、搜索过滤、分批、单层子代理递归、验证、带文件行号引用的程序化合成
- PDF 经 anydoc 本地转换，扫描件走 firecrawl OCR
- 10+ 文件或 50k+ tokens 场景自动触发分解
- 附 131 份房贷 PDF 语料（git submodule）的评测脚本

## 适用场景

- 让 agent 分析整个代码库的错误处理模式或安全问题
- 汇总大量文档、会议记录或 PDF 报告的关键信息
- 多跳问答与跨分散文件的推理任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6:  An Agent Skill for Claude Code, Codex, Cursor and compatible agents, based on the Recursive Language Models researc
> L28: When a task is codebase-wide, multi-document, a pile of PDFs, or a dense aggregate, even if it fits the window, the

## 星数曲线

```mermaid
xychart-beta
    title "massimodeluisa/recursive-decomposition-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-25 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7163c5db38f1` · [字段定义](../../DATASET.md)*
