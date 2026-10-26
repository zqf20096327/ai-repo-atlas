# interfluve-wav/andrej-karpathy-skills-hermes

⭐ 29 · MIT · 推送 2026-06-17 · [GitHub](https://github.com/interfluve-wav/andrej-karpathy-skills-hermes) · [官网](https://x.com/karpathy/status/2015883857489522876) · 个人维护

**给 Hermes agent 的 Karpathy LLM 编码准则技能包**

将 multica-ai/andrej-karpathy-skills（MIT）中的行为准则适配为 Hermes 的 SKILL.md 格式技能包，内容源自 Andrej Karpathy 对 LLM 编码常见问题的观察，包含四条原则与前置 YAML 元数据，另附长篇前后对照示例文件。安装方式为 git clone 后将目录复制到 ~/.hermes/skills/ 下；含到相关技能的 wikilinks。沿用上游 MIT 许可证。

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

- SKILL.md 主文件含 YAML frontmatter 与四条编码原则
- 附 references/EXAMPLES.md 前后对照示例
- 提供复制到 ~/.hermes/skills/ 的安装步骤

## 适用场景

- 为 Hermes agent 安装 LLM 编码行为准则技能
- 参考 Karpathy 总结的 LLM 编码陷阱规避原则

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: This repository contains a **Hermes**-formatted skill adapted from multica-ai/andrej-karpathy-skills (MIT): behavior
> L31: cp -R Karpathy-Hermes-Skill ~/.hermes/skills/software-development/karpathy-guidelines

## 星数曲线

```mermaid
xychart-beta
    title "interfluve-wav/andrej-karpathy-skills-hermes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-26 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0454a26b531b` · [字段定义](../../DATASET.md)*
