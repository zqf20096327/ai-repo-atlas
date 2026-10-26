# beautyfree/skiller

⭐ 47 · TypeScript · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/beautyfree/skiller) · [官网](https://skiller.download) · 个人维护

**桌面端 AI agent 技能管理器：跨 49 个编码 agent 统一安装同步 SKILL.md**

基于 Electron 的跨平台（macOS/Windows/Linux）桌面应用，用于集中管理 Claude Code、Codex、Cursor 等 49 个编码 agent 的 SKILL.md 技能包：统一面板查看已装技能、一键跨 agent 同步、项目级技能作用域、内联编辑 SKILL.md，并可从 skills.sh 与 ClawHub 市场搜索安装。自动检测已安装的 agent，项目技能采用 .agents/skills/ 共享约定，对 Skills CLI 的 .skill-lock.json 只读。安装包由 CI 构建，通过 GitHub Releases 分发并支持自动更新。采用 Sustainable Use License v1.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生支持 49 个编码 agent，安装一次即可同步到全部
- 从 skills.sh 与 ClawHub 市场内搜索并安装社区技能
- 项目级技能作用域（pin 到特定仓库，不污染全局）
- macOS 签名公证，三平台安装包由 CI 自动构建

## 适用场景

- 在多个编码 agent 之间统一安装和同步技能包
- 浏览 skills.sh / ClawHub 发现并安装社区技能
- 为特定仓库配置项目级技能而不影响全局

## 场景标签

 · 领域:开发者工具/agent 技能管理

## 证据(README 行号)

> L5: Skiller is a desktop **AI agent skills manager** for Claude Code, Codex, Cursor and other coding agents. Find, insta
> L21: Skiller supports **49 agents** natively — drop a skill into one place and it propagates to all of them.

## 星数曲线

```mermaid
xychart-beta
    title "beautyfree/skiller 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-26 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a01d46eb2851` · [字段定义](../../DATASET.md)*
