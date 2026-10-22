# MemTensor/skills-vote

⭐ 304 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/MemTensor/skills-vote) · [官网](https://skills.vote) · 组织维护 · 中文 README

**Agent 技能全生命周期治理系统：采集、推荐到进化**

由 MemTensor 构建的 agent 技能治理系统：从开源 GitHub 仓库中发现 168 万个 SKILL.md 文件（79 万经 Anthropic 官方验证器校验格式有效），将技能采集、画像分析、任务前即时推荐、基于轨迹的归因与反馈驱动的技能库进化连为一个循环。提供托管云端服务（需 API key）与本地私有库两种集成，通过 npx 以 agent 技能形式安装，兼容 Codex、Claude Code、OpenClaw 等 agent。在 Terminal-Bench Pro、SWE-Bench Pro 等 benchmark 上评测；本地归因与进化部分仍在路线图中未完成。

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

- 168 万 SKILL.md 发现、79 万格式有效（官方验证器校验）
- 任务前即时技能推荐，替代加载静态技能清单
- 基于执行轨迹与验证信号的成果归因
- 托管云服务与本地私有库（skills-vote-local）两种集成

## 适用场景

- 让编码/研究 agent 在任务前自动检索相关技能
- 从本地或私有技能库做技能推荐
- 用执行轨迹反馈归因并进化可复用技能

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L31: SkillsVote treats skills as lifecycle-managed artifacts. It connects collection, profiling, just-in-time recommenda
> L67: |`skills-vote`|Using the hosted SkillsVote service for cloud-based skill recommendation and attribution-grounded fe
> L76: Supercharge your agents (Codex, Claude Code, OpenClaw) by integrating SkillsVote directly! Just drop this prompt in

## 星数曲线

```mermaid
xychart-beta
    title "MemTensor/skills-vote 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 303 --> 305
    line [304, 304]
```

2026-10-18 304 → 2026-10-22 304（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4a00357d2996` · [字段定义](../../DATASET.md)*
