# aviadr1/claude-meta

⭐ 26 · MIT · 推送 2025-11-08 · [GitHub](https://github.com/aviadr1/claude-meta) · 个人维护

**把 CLAUDE.md 变成自改进系统的提示词与模板集**

面向 Claude Code 用户的实践手册仓库：核心是一句反思提示词（“反思错误→抽象→泛化→写入 CLAUDE.md”）配合 CLAUDE.md 中的 META 元规则段，使 AI 在每次犯错后按既定格式沉淀规则，形成跨会话的累积学习。README 以长文解释工作原理与人力/AI 认知分工，并提供两个模板文件：CLAUDE_TEMPLATE.md（最小起点）与 CLAUDE_FULL.md（演进后的完整示例）。仓库不提供代码或安装命令，仅含模板与文章。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单句反思提示词触发错误→规则沉淀的改进循环
- META 元规则段规定新规则的书写格式与文档维护方式
- 双层结构：顶部摘要区 + 详细规则区
- 提供最小模板与完整生产示例两个文件

## 适用场景

- 让 Claude Code 从每次错误中沉淀可复用规则
- 为项目搭建带自维护机制的 CLAUDE.md
- 参考元规则写法改进现有 AI 编码规范文档

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: This repository captures a complete playbook for transforming `CLAUDE.md` from static documentation into a self-impr
> L143: ## Getting Started: Two Templates

## 星数曲线

```mermaid
xychart-beta
    title "aviadr1/claude-meta 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2f3216d09803` · [字段定义](../../DATASET.md)*
