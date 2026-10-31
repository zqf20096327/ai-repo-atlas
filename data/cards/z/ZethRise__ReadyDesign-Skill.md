# ZethRise/ReadyDesign-Skill

⭐ 14 · JavaScript · MIT · 推送 2026-08-18 · [GitHub](https://github.com/ZethRise/ReadyDesign-Skill) · 个人维护

**约束 AI 编码代理只用六大官方组件源构建 UI 的技能包**

面向 AI 编码代理（Claude Code、Codex、Antigravity 2.0、Grok）的 Agent Skills 包：强制代理仅从 shadcn/ui、Ant Design、Kokonut UI、Motion、Bklit、sashimi UI 六个官方源逐页 web-fetch 并安装真实组件，禁止凭记忆或猜测重建。规则（抓取协议、色彩锁定、提问清单）集中写在 SKILL.md。通过 npx 或 npm install 安装，postinstall 将 SKILL.md 写入各代理的技能目录，需 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 限定六个官方组件源，禁止记忆式或模仿式重建
- 要求逐 URL 抓取页面后再安装组件，失败两次即停止
- 新项目保留各库原始颜色与 token 不改动
- 工作中向用户提问 2–4 次确认设计决策

## 适用场景

- 让 AI 编码代理生成 UI 时只安装真实官方组件
- 避免代理编造或不一致地重写组件库样式
- 在 Claude Code / Codex / Grok / Antigravity 中统一 UI 构建规范

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: An Agent Skills package that forces AI coding agents to build UI from **six official component sources only**. The 
> L15: **v1.0.1** on npm. Works with **Claude Code**, **Codex**, **Antigravity 2.0**, and **Grok**. Requires Node.js 18+.

## 星数曲线

```mermaid
xychart-beta
    title "ZethRise/ReadyDesign-Skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `60e6b2428561` · [字段定义](../../DATASET.md)*
