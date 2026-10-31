# freakyflow/garminskill

⭐ 19 · Python · 推送 2026-02-11 · [GitHub](https://github.com/freakyflow/garminskill) · 个人维护

**将 Garmin Connect 健康数据同步为 markdown 的 OpenClaw 技能**

面向 OpenClaw agent 框架的技能：通过 garminconnect 库（配合 cloudscraper 绕过 Cloudflare SSO）从 Garmin Connect 拉取睡眠、心率、HRV、SpO2、压力、训练准备度、活动记录等约 12 类数据，按日写入 health/YYYY-MM-DD.md 供 agent 在对话中引用。认证分两阶段：一次性 setup 用 getpass 交互输入密码并缓存约一年有效期的 OAuth token，后续同步仅用缓存 token。限制：不支持 2FA（须在 Garmin 账户上禁用）；Garmin 反爬更新可能导致认证间歇性失效。用 uv 运行，支持 cron 定时同步。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同步睡眠/心率/HRV/SpO2/压力/训练准备度/活动等 12 类 Garmin 数据
- 一次性 OAuth setup，token 缓存约一年，后续同步无需凭据
- 输出按日 markdown 文件，无数据段自动省略
- 通过符号链接安装为 OpenClaw 技能，支持 cron 定时同步

## 适用场景

- 让我的 OpenClaw agent 在对话中引用每日健康与运动数据
- 每天早上自动同步 Garmin 数据生成健康摘要
- 把训练负荷、HRV、睡眠等指标纳入 AI 助手的上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: An OpenClaw skill that syncs your daily health data from Garmin Connect into markdown files. OpenClaw can then refer
> L65: ln -s /path/to/garminskill ~/.openclaw/skills/garmin-connect

## 星数曲线

```mermaid
xychart-beta
    title "freakyflow/garminskill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3d659f3baa46` · [字段定义](../../DATASET.md)*
