# Sagargupta16/claude-cost-optimizer

⭐ 41 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Sagargupta16/claude-cost-optimizer) · [官网](https://sagargupta.online/claude-cost-optimizer/) · 个人维护

**降低 Claude Code 使用成本的技能与工具箱：定价杠杆、成本计算与项目评分**

面向 Claude Code 用户的成本优化工具集：可安装的 cost-mode 技能（通过官方 plugin 系统或 npx skills 装入 40+ agent），在会话中压缩冗余输出、提示切换更廉价模型、提醒压缩上下文；claude-rate 以单个 stdlib Python 脚本流式运行，读取本地仓库、~/.claude 设置与近 30 天使用记录，输出 A+ 到 F 评分与修复建议；另有浏览器端 Repo Analyzer、Cost Calculator、Badge Checker 网页工具与 12 篇深度指南。所有省钱主张要求附来源或公式，定价数据在六处代码副本间由 CI 校验一致。

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

- cost-mode 技能：剥离填充语、提示换廉价模型、会话感知的 /compact 提醒，安全警告时自动停用
- claude-rate 单文件 stdlib Python，零安装流式运行，本地读取设置与转录记录
- 浏览器端 Repo Analyzer / Cost Calculator / Badge Checker 网页工具
- 每个省钱主张附来源或公式，六份定价副本由 CI 强制同步

## 适用场景

- 给 Claude Code 项目与用户配置做成本评分并按建议修复
- 估算每月 token 花费与各优化杠杆的节省空间
- 在会话中自动启用简洁模式减少输出 token

## 场景标签

 · 领域:AI 开发工具/成本优化

## 证据(README 行号)

> L33: /plugin marketplace add Sagargupta16/claude-cost-optimizer
> L40: npx skills add Sagargupta16/claude-cost-optimizer
> L103:  How the toolkit fits together, in three rows. Top row, what the tools read: any public repo, your repo (CLAUDE.md

## 星数曲线

```mermaid
xychart-beta
    title "Sagargupta16/claude-cost-optimizer 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-26", "2026-10-29"]
    y-axis "stars" 37 --> 42
    line [38, 39, 40, 41, 41]
```

2026-10-18 38 → 2026-10-29 41（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `534be082b393` · [字段定义](../../DATASET.md)*
