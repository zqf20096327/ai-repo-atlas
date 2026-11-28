# EliHei2/scicraft

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/EliHei2/scicraft) · 个人维护

**面向科研人员的 40 个 Claude Code 研究技能注册表**

以 Claude Code 插件形式分发的科研技能注册表，含两个插件：scicraft（31 个技能，任意领域）与 scicraft-ml（9 个技能，机器学习研究），覆盖项目组织、实验设计、结果分析、图表制作、论文写作、提交前审查、审稿回复与 agent 协作八个阶段。每个技能由 SKILL.md 规则、参考文件、脚本与测试用例组成，按需加载；带 grader 检查的构建门禁，无遥测。通过 claude plugin marketplace 命令或 install.sh 脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 个技能、267 个参考文件、238 个脚本、121 个测试用例（887 项分级检查）
- 技能按需加载：平时仅保留一段描述，匹配请求时才读取规则
- 每个技能附脚本与测试，tools/check.py 门禁检查链接、编译与机器腔文本
- 支持 LSF/SLURM 集群作业、LaTeX 排版、TikZ/HTML canvas 图表等具体脚本

## 适用场景

- 为论文从结果数据生成符合印刷尺寸的多面板图表
- 在投稿前做 QC 与论文-代码一致性审查
- 起草 rebuttal、海报与学术幻灯片
- 将个人的 Claude Code 使用历史蒸馏成可安装技能

## 场景标签

`科研工具` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A registry of 40 hard skills for research with Claude Code.
> L29: **40 skills, 267 reference files, 238 scripts, 121 test cases with 887 graded checks.** They come as two plugins: `


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `5f6928887693` · [字段定义](../../DATASET.md)*
