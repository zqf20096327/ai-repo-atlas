# luoling8192/ai-coding-principles

⭐ 172 · MIT · 推送 2026-03-26 · [GitHub](https://github.com/luoling8192/ai-coding-principles) · 个人维护 · 中文 README

**Claude Code 编码纪律与系统设计技能集**

面向 Claude Code 用户的技能（skills）集合，包含两个技能：ai-coding-discipline 在代码编写任务中加载 6 条强制规则，用于防止常见 AI 编码反模式（禁止静默回退、catch-all、测试必须可失败等）；ddia-principles 是基于《Designing Data-Intensive Applications》提炼的参考指南，在设计数据库模式、存储引擎选型、复制/分区、批流处理时加载。通过 npx skills add 命令安装，MIT 许可，另提供中文文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 条编码纪律规则在代码任务中强制加载
- DDIA 三大部分（基础/分布式数据/衍生数据）的提炼参考
- npx 单命令安装

## 适用场景

- 给 Claude Code 加载编码纪律规则，减少 AI 编码反模式
- 做数据库与分布式系统设计时加载 DDIA 知识参考

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A collection of Claude Code skills for coding discipline and system design knowledge.
> L11: Mandatory rules loaded during all code writing tasks that prevent common AI coding anti-patterns.

## 星数曲线

```mermaid
xychart-beta
    title "luoling8192/ai-coding-principles 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27", "2026-10-28"]
    y-axis "stars" 170 --> 173
    line [172, 171, 172, 172]
```

2026-10-18 172 → 2026-10-28 172（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2de441535b0f` · [字段定义](../../DATASET.md)*
