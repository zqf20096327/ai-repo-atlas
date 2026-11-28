# CalebLiu/job-hunt-skill

⭐ 10 · Shell · MIT · 推送 2026-05-07 · [GitHub](https://github.com/CalebLiu/job-hunt-skill) · 个人维护 · 中文 README

**求职者的 Claude Code 技能：从主 CV 生成整套定制求职材料**

一个面向 Claude Code 的端到端求职流水线技能：粘贴职位描述后，从经验库中选取匹配的简历要点，生成一页定制 CV、求职信、LinkedIn 冷私信、申请表要点，并逐步引导提交、记录到 tracker、根据反馈迭代。包含 8 个阶段与 job-hunt（编排）+ cv-tailor（单岗位出材料）两个子技能，输出存放于 applications/ 目录且主 CV 永不被修改。内置硬性规则：绝不自动提交、不虚构数据、CV 一页限制。默认 LaTeX 输出，面向初级求职者，需自行准备主 CV 与经验库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 阶段编排 + job-hunt/cv-tailor 双子技能架构
- 主 CV 永不被修改，每岗位输出独立目录
- 硬性规则：不自动提交、不虚构指标、签证问题如实回答
- 研究阶段用并行子代理应对 Glassdoor/LinkedIn 反爬

## 适用场景

- 用一份主 CV 批量投递 10+ 家初创公司并逐岗位定制材料
- 求职过程中用 tracker 追踪所有投递记录
- 根据上一次投递反馈改进下一次申请

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: > An end-to-end Claude Code skill pipeline that turns one master CV + an experience bank into tailored applications,
> L12: You paste a job description URL or text. Claude:
> L94: - Claude Code — Claude as a CLI agent


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `915c0b085fc9` · [字段定义](../../DATASET.md)*
