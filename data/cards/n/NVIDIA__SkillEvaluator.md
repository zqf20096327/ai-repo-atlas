# NVIDIA/SkillEvaluator

⭐ 4,551 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/NVIDIA/SkillEvaluator) · [官网](https://docs.nvidia.com/skills/skillevaluator/) · 组织维护

**评估 AI agent 技能与插件质量的 CLI 与 CI 框架**

NVIDIA 出品的命令行工具与可复用 CI 模板集合，用于检查遵循 Agent Skills 规范的技能文件夹：Tier 1 静态验证（质量评分、模式/版本/PII/许可证/脚本检查、SkillSpector/Gitleaks/Bandit 等安全扫描、harness 兼容性检查）、Tier 2 语义重叠去重、Tier 3 沙箱内实测技能对 agent 行为的影响。静态检查无需 LLM key，全量运行需 NVIDIA Build key 与 Docker。通过 pip 或 uv 安装，支持 GitHub/GitLab CI 集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 500+ 静态规则的三层评估：验证、去重、live agent 实测
- harness 兼容性检查判断 Claude Code/Codex 等能否加载技能
- CI 模板自动生成质量与安全门禁（GitHub/GitLab）
- 静态检查无需 LLM key、GPU 或 Docker

## 适用场景

- 技能合并前在 CI 中拦截质量与安全问题
- 检测技能在 agent 间是否存在重复或语义重叠
- 评估某技能对 agent 任务结果的增益

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L17: SkillEvaluator checks AI agent skills and plugins, and measures a skill's effect
> L109: `skillevaluator validate` includes Harness Check in Tier 1 alongside **quality,
> L210: |Tier 3: Live Agent Evaluation|Does the skill help the agent?|`skillevaluator tier3 ./my-skill`|Provider access, a

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/SkillEvaluator 星数(近 27 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 194 --> 4947
    line [590, 593, 595, 597, 600, 606, 609, 612, 616, 617, 618, 595, 657, 683, 830, 1110, 1222, 1549, 2662, 3323, 3679, 4110, 4260, 4324, 4385, 4454, 4551]
```

2026-10-23 590 → 2026-11-26 4,551（+3,961）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `b7b6349e9ab1` · [字段定义](../../DATASET.md)*
