# ClawSecure/clawsecure-openclaw-security

⭐ 38 · HTML · MIT · 推送 2026-10-05 · [GitHub](https://github.com/ClawSecure/clawsecure-openclaw-security) · [官网](https://www.clawsecure.ai) · 组织维护

**面向 OpenClaw AI 技能的免费安全扫描与审计平台**

ClawSecure 是针对 OpenClaw 生态（AI agent 技能与工作流）的安全扫描与审计平台，已审计 3,000+ 技能。审计采用三层协议：自有威胁情报（55+ 威胁模式）、静态与行为分析、npm/PyPI 供应链依赖扫描，覆盖全部 10 个 OWASP ASI 类别。使用方式为 Web 界面扫描、Security Clearance API 与可检索的 Verified Agent Registry，无需安装本产品。另发布若干免费开发工具（ShutUp Tabs、Railgun、Claude Timestamps）。

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

- 3-Layer Audit Protocol：威胁情报 + 静态/行为分析 + 供应链依赖扫描
- 覆盖 OWASP ASI 全部 10 类，含 ClawHavoc 与 sleeper agent 检测
- Watchtower 24/7 哈希漂移监控，捕捉安装后篡改
- 免费 Web 扫描与 Security Clearance API，无需安装

## 适用场景

- 安装前扫描 OpenClaw 技能确认安全状态
- 通过 API 在授权前程序化校验 agent 完整性
- 在 Registry 中按安全分筛选可信技能

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L17: 🛡️ **ClawSecure is the independent integrity layer for the OpenClaw ecosystem** — a free OpenClaw security scanner 
> L41: ClawSecure provides the only complete security solution covering all 10 OWASP ASI categories for OpenClaw agents. E

## 星数曲线

```mermaid
xychart-beta
    title "ClawSecure/clawsecure-openclaw-security 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-25 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `bb5d51832c66` · [字段定义](../../DATASET.md)*
