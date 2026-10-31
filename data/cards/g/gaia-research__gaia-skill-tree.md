# gaia-research/gaia-skill-tree

⭐ 23 · Python · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/gaia-research/gaia-skill-tree) · [官网](https://gaiaskilltree.com/) · 组织维护

**AI agent 技能开放注册表：以升级式技能树验证并归属作者**

Gaia 是一个 AI agent 技能的开源注册表，按树状等级结构（0-6★）组织技能，核验技能能力并将命名权归属给人类作者而非模型。采用 9 类证据类型（arxiv 论文、repo、GitHub stars、peer-review、benchmark 等）与 Platinum-Grey 评级计算 Trust Magnitude，提供公开 Trust Ledger。技能可融合（gaia fuse）生成新节点。提供 CLI、TUI、静态 JSON API 与 Claude Code 插件（Skill Heaven，内置 MCP server，按需 /summon 技能）。由小团队维护，治理路线图含 Core Team 分工。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 0-6★ 升级式技能树与作者命名归属机制
- 9 类证据类型 + Platinum-Grey 评级 + 公开 Trust Ledger
- CLI/TUI 工具链：init/scan/push/fuse/appraise 等命令
- 静态只读 JSON API 与 Claude Code Skill Heaven 插件（/summon 按需调用技能）

## 适用场景

- 把自己编写的 AI agent 技能提交注册并获得署名与等级认证
- 查找已验证的技能并通过 CLI 一键安装到 agent 环境
- 通过 API 程序化抓取技能图谱做分析或集成

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L7: Gaia is not a marketplace of skills, or an installer of some sorts. What we do is we verify your skill, check its ca
> L34: **Keywords:** AI Agent Skill registry • Evidence-Backed Skill Graph • Capability Graph • Model Context Protocol • A

## 星数曲线

```mermaid
xychart-beta
    title "gaia-research/gaia-skill-tree 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9ce457948970` · [字段定义](../../DATASET.md)*
