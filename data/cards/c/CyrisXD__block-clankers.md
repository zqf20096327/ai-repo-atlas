# CyrisXD/block-clankers

⭐ 19 · Shell · MIT · 推送 2026-05-14 · [GitHub](https://github.com/CyrisXD/block-clankers) · 个人维护

**自动从社区黑名单同步封禁 GitHub 垃圾账号的 Action**

面向 GitHub 个人账号与管理员组织的 GitHub Action：从社区维护的 JSON 名单（默认 UnsafeLabs/Bounty-Hunters clankers.json）拉取已知垃圾机器人账号，按计划任务对比当前封禁列表并写入差量封禁。支持 @me、@auto（个人+所有管理组织）或指定组织作为目标，可自定义 source-url、dry-run、移除时解封等输入。含限速节流、重试退避、每运行写入上限等 API 保护机制，稳态运行只读不写、幂等。使用需 Fork 仓库配置 PAT secret 或在自己的 workflow 中引用。

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

- 从社区维护 JSON 名单同步个人账号与组织的封禁列表
- @auto 自动发现所管理的组织并一并同步
- 差量写入、限速节流与每运行写入上限（默认 200）
- 支持 dry-run 与 source-url 固定到指定 commit

## 适用场景

- 我想自动封禁已知的 GitHub 垃圾机器人账号
- 我管理多个组织，想统一同步封禁名单
- 我想先 dry-run 看会封禁哪些账号再实际执行

## 场景标签

 · 领域:开发者工具/平台运维

## 证据(README 行号)

> L5: Auto-block known spam bot accounts from your **personal GitHub account** and/or **every org you admin**. Pulls a com
> L66: 1. Fetches the source JSON (with retries; fails closed if empty).

## 星数曲线

```mermaid
xychart-beta
    title "CyrisXD/block-clankers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `4440a74abaa7` · [字段定义](../../DATASET.md)*
