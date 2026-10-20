# greenthree/ProbHub-skill

⭐ 11 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/greenthree/ProbHub-skill) · 个人维护 · 中文 README

**算法竞赛出题工作流：题面、数据、验证到 DOMjudge 打包一站式完成**

面向 ACM/ICPC 出题人的本地工作流：以 Workspace Schema v1 组织题面、标程、Validator、暴力和错解源码及数据，提供 lint、无缓存 Judge、stress 差分测试、Judge QA、mutation 探测等验证手段，用 Typst 生成单题与整卷 PDF，构建 DOMjudge ZIP 与 Manifest。可通过 CLI、WebUI 或让 Codex、Claude Code 等 Agent 读取同一套 Skill 规则协作出题，提供快速/普通/完整三种验证模式。限定本地单用户可信环境，非安全沙箱；依赖 Python 3.10–3.12、Node.js 18+、g++(C++17) 和 Typst 0.14.2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- lint / Judge / stress / Judge QA / mutation 多层题目验证链
- Typst 生成单题与整卷 PDF，构建 DOMjudge ZIP 与 Manifest，含 ZIP 深度验包
- Codex、Claude Code 等 Agent 按同一 Skill 规则协作，含盲审 Agent 独立证明机制
- seal 冻结可复现版本，checkpoint 发布不可变草稿支持并行出题

## 适用场景

- 从零设计算法竞赛题并生成可判定的完整交付物
- 批量维护已有题库的题面、数据与验证
- 让 Agent 参与出题同时保留可审查、可复现的验证结果
- 组卷并用 Typst 排版 PDF、导出 DOMjudge 题目包

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L22: ProbHub 是一套面向 ACM/ICPC 出题人的本地工作流。它把题面、代码、数据、评测、排版和 DOMjudge 打包连接起来；你可以自己使用，也可以让 Codex、Claude Code 等 Agent 按同一套规则协作。
> L24: 它适合从零设题、批量维护题面与数据，或希望让 Agent 参与出题而仍保留可审查、可复现交付结果的队伍。ProbHub 面向本地单用户、可信环境，会控制时间、内存、输出和进程树，但不是运行敌意代码的安全容器。
> L94: 在比赛目录中打开 Codex、Claude Code 或其他兼容 Agent，直接描述目标：

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `d564ad6c7126` · [字段定义](../../DATASET.md)*
