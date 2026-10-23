# crabbuild/compass

⭐ 174 · Rust · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/crabbuild/compass) · [官网](https://compass.crab.build) · 组织维护

**本地优先的代码知识图谱引擎：为人和编码助手提供代码库结构地图**

用 Rust 编写的本地优先工具，把源码与项目工件抽取为有向可查询的知识图谱，覆盖符号、文件、社区与关系。提供架构报告、调用图、反向依赖影响分析、版本间拓扑 diff、基于精确 Git 提交的历史图，以及确定性的只读查询语言 CompassQL 和自然语言 query。通过 MCP 服务、Agent Skills 与平台适配器接入 Claude Code、Codex、Gemini CLI、Copilot 等编码助手，作为本地上下文层；结构抽取无需 Python、嵌入模型或向量库。提供安装脚本、cargo 源码构建与 VS Code 扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 源码与工件抽取为有向可查询知识图谱，本地运行无需嵌入/向量库/模型凭据
- 反向依赖遍历、影响分析与基于精确 Git 提交的不可变历史图
- 确定性只读 CompassQL 与带证据分页的自然语言 query（--evidence 溯源）
- 通过 MCP、Agent Skills 与平台适配器接入多种编码助手；导出 HTML/GraphML/Neo4j 等格式

## 适用场景

- 接手陌生仓库时先看架构图、社区与 god-node 检测
- 为 Claude Code/Codex 等编码助手提供有据可查的本地代码上下文
- 评估一次改动会影响哪些符号与文件
- 对比两个 Git 提交之间的结构差异

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L38: |Give assistants focused context|Native skills, hooks, MCP serving, and compact graph queries|
> L152: Use Compass as a local context layer for coding assistants. The complete loop is:
> L248: Inside a Git repository, `compass install` detects supported coding agents at the repository root and always inclu

## 星数曲线

```mermaid
xychart-beta
    title "crabbuild/compass 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 172 --> 175
    line [173, 174, 174]
```

2026-10-18 173 → 2026-10-23 174（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e61bdf88523d` · [字段定义](../../DATASET.md)*
