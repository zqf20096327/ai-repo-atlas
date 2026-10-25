# Sunwood-ai-labs/SourceSage

⭐ 71 · Python · MIT · 推送 2026-03-14 · [GitHub](https://github.com/Sunwood-ai-labs/SourceSage) · [官网](https://sunwood-ai-labs.github.io/SourceSage/) · 组织维护

**把源码仓库转成 AI 友好 Markdown 文档的 CLI 工具**

SourceSage 是一个 Python CLI 工具，面向需要让 AI 助手快速理解代码仓库的开发者：它读取项目结构、Git 上下文、文件统计与文件摘录，合并为一个 Markdown 文档（.SourceSageAssets/Repository_summary.md）。支持 --repo 分析任意本地仓库、--lite 精简模式（跳过逐文件摘录）、语言选项与 .SourceSageignore 忽略规则（不存在时自动生成模板）。提供 uvx 一次性运行、uv tool、pip 与源码四种安装方式。--diff 已被声明为弃用并保留兼容。

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

- 合并项目结构、Git 上下文、文件统计与文件摘录为单一 Markdown 产物
- --repo 支持分析任意本地仓库，--lite 跳过逐文件摘录
- 自动合并 .gitignore 与 .SourceSageignore，缺失时生成默认模板
- 提供 uvx 一次性运行、pip、源码等多种安装途径

## 适用场景

- 生成仓库文档供 AI 编程助手直接阅读
- 为代码仓库做首轮探索时用 --lite 快速摸底
- 为提交给 LLM 的上下文准备结构化仓库摘要

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L9:  Repository analysis CLI that turns source trees into AI-friendly Markdown documentation.
> L34: - Generate repository documentation that an assistant can read immediately.

## 星数曲线

```mermaid
xychart-beta
    title "Sunwood-ai-labs/SourceSage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-25 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `16bf76357391` · [字段定义](../../DATASET.md)*
