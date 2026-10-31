# hellokaton/game-copycat

⭐ 20 · TypeScript · MIT · 推送 2026-07-17 · [GitHub](https://github.com/hellokaton/game-copycat) · 个人维护 · 中文 README

**复刻休闲小游戏的 Agent Skill：一句 prompt 产出原创 web 游戏**

面向 Claude Code、Codex、Cursor 等支持 SKILL.md 的 agent 的技能包：输入游戏名、推文或截图，agent 执行八阶段流水线——调研原作规则、确认范围、Vite+React+TS 脚手架、纯函数内核与求解器验证关卡、原创品牌 UI、浏览器自验审计、可选部署到 Cloudflare Workers。内核先写求解器再写生成器，不可解关卡构建期拒收；机制复刻但名称、美术、关卡数据保持原创。依赖支持 skills 的 agent 与 Node 18+。

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

- 八阶段流水线，每阶段有出口门禁
- 先写求解器再写生成器，构建期校验关卡可解性与唯一解
- agent 在真实浏览器中自验通关后才交付
- 产物为原创品牌表达，附灵感来源声明与差异清单

## 适用场景

- 用一句话让 agent 复刻 Wordle、2048、消消乐等益智游戏
- 快速产出可玩的原创品牌休闲游戏原型
- 基于求解器保证关卡质量的解谜游戏开发

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: 一个复刻小游戏的 Agent Skill：给它一个名字、一条推文或一张截图，它还你一款精致、完全原创的 web 小游戏。不是 demo，是成品。支持 Claude Code、Codex、Cursor 及一切认 `SKILL.md` 
> L25: ……它会跑完整条流水线：调研原作规则 → 和你确认范围 → 搭脚手架 → 构建**可证明正确的游戏内核** → 做原创品牌的精致 UI 和真实手感 → **在真实浏览器里亲手玩通一局**来验收 →（可选）部署到 Cloudflar
> L81: ## 工作原理

## 星数曲线

```mermaid
xychart-beta
    title "hellokaton/game-copycat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `19c035126fc2` · [字段定义](../../DATASET.md)*
