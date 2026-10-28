# huangzt/my-agent-skills

⭐ 20 · Python · MIT · 推送 2025-12-21 · [GitHub](https://github.com/huangzt/my-agent-skills) · 个人维护 · 中文 README

**为 AI 代理提供数据库操作技能集，兼容 Openskills**

面向 AI 代理的数据库工具技能集合，兼容 OpenSkills 系统。包含四组技能：mysql-tools（MySQL）、mssql-tools（SQL Server）、dm8-tools（达梦 DM8）、sqlite-tools（SQLite 内置）。每个技能由 SKILL.md 使用说明与 Python 工具脚本目录组成。使用方式有两种：通过 npm 安装 OpenSkills 后配合使用，或直接 git clone 仓库运行脚本。各技能依赖通过 pip 安装（pymssql、pymssql、jaydebeapi/JPype1），支持 Windows/macOS/Linux。

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

- 四组数据库技能：MySQL / SQL Server / 达梦 DM8 / SQLite
- 每个技能含 SKILL.md 说明与 Python 工具脚本
- 兼容 OpenSkills，也可直接克隆仓库运行脚本

## 适用场景

- 让 AI 代理查询或操作 MySQL、SQL Server 等数据库
- 在 OpenSkills 体系中扩展数据库能力
- 直接复用 Python 脚本做数据库操作

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: 为 AI 代理提供的数据库工具技能集，兼容 OpenSkills 系统。
> L14: |技能|数据库|依赖|

## 星数曲线

```mermaid
xychart-beta
    title "huangzt/my-agent-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8a3060162b33` · [字段定义](../../DATASET.md)*
