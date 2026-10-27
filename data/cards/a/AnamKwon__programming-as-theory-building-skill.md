# AnamKwon/programming-as-theory-building-skill

⭐ 30 · Python · MIT · 推送 2026-06-11 · [GitHub](https://github.com/AnamKwon/programming-as-theory-building-skill) · 个人维护

**将 Naur 理论构建思想转化为 Claude Code 编码规则技能**

面向 Claude Code 的插件与可复用编码代理技能：基于 Peter Naur《Programming as Theory Building》(1985)，在编码代理做非平凡改动前要求其重建程序理论、按相似性放置改动、保持改动最小、避免投机抽象并验证领域行为。包含一个技能文件与项目级 CLAUDE.md 规则文件，支持手动安装到其他 CLI（Codex/Gemini 需转换格式）。附三组对照基准（Claude Haiku 生成、Opus 评审），theory_only 组加权均分 81.0，高于对照组 77.7 与 74.8。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 Naur 理论构建思想转化为五项代理前置检查（重建理论/按相似性放置/外科手术式改动/避免投机抽象/验证理论）
- 提供 Claude Code 插件、手动技能安装、CLAUDE.md 三种安装方式
- 三组对照代码生成基准（Claude Haiku 生成 + Opus 评审）含复现脚本
- 附 Codex CLI / Gemini CLI 的规则迁移说明

## 适用场景

- 让编码代理在改动前先推断程序的领域不变量
- 减少代理产出边界错位的 helper 与投机抽象
- 在 Claude Code 中以插件形式启用该编码规则

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Claude Code plugin and reusable coding-agent skill that turns code generation from prompt completion into theory-p
> L22: The plugin packages one Claude Code skill and one project-level `CLAUDE.md` guideline file. The skill asks the agen

## 星数曲线

```mermaid
xychart-beta
    title "AnamKwon/programming-as-theory-building-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bce3fbc3f987` · [字段定义](../../DATASET.md)*
