# TashanGKD/tashan-research-skills

⭐ 19 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/TashanGKD/tashan-research-skills) · 组织维护 · 中文 README

**面向科研场景的中英双语 agent 技能库（19 个自研 skills）**

包含 19 个自研科研 agent 技能，按文献证据、研究构思、成果表达、协作沉淀、工具测评五类组织，每个技能为独立文件夹、以 SKILL.md 为入口，复制进兼容 SKILL.md 的 agent 运行环境（Codex/Claude Code/Cursor 等）即可使用。核心技能 find-science-skills 提供从 1,391 个 Skill 与 5,643 个科研 MCP 的静态目录中按领域/阶段/功能筛选，筛选器仅依赖 Python 标准库，无需后端与 API 密钥。部分技能需环境变量凭证（Giiisp/阿里云百炼/MinerU），未配置时可转 dry-run 或本地回退。项目由磐石 AI4Science 生态与应用模式研究项目支持，MIT 许可。

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

- 19 个自研技能覆盖论文检索/审查、假设生成、实验设计、统计分析、学术写作、PPT、绘图、视频等科研流程
- find-science-skills 从 1,391 个 Skill 与 5,643 个 MCP 的静态目录做确定性筛选，仅依赖 Python 标准库
- 技能自包含、无相互依赖，可按需安装子集
- 无凭证时转 dry-run 或本地回退，不伪造结果

## 适用场景

- 把文献综述、引用合规、论文审查等环节做成 agent 可执行的技能
- 为研究选题生成带证据追踪的假设并设计实验与统计方案
- 把论文/报告整理成演示文稿、科研图像或讲解视频
- 在安装 agent 技能或 MCP 前做规范与安全测评

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L18: 仓库里是我们自己开发的 19 个科研 agent skills，按文献证据、研究构思、成果表达、协作沉淀、工具测评五类整理。每个技能是一个独立文件夹，入口是 `SKILL.md`，配套的脚本、模板和测试放在同一目录，复制进 age
> L24: `find-science-skills` 用于从科研目录中查找适合当前任务的 Skill 或 MCP。宿主模型先判断“资源类型 × 研究领域 × 研究阶段 × 功能分工”，再调用仅依赖 Python 标准库的确定性筛选器缩小范围
> L45: |Skill / MCP 发现|`skills/find-science-skills`|按研究领域、研究阶段和功能分工筛选 1,391 个科研 Skill 与 5,643 个活动科研 MCP，并保留来源与可信状态供宿主模型复核。

## 星数曲线

```mermaid
xychart-beta
    title "TashanGKD/tashan-research-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f406a972b749` · [字段定义](../../DATASET.md)*
