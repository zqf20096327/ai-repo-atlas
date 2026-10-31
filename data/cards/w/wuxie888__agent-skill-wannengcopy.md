# wuxie888/agent-skill-wannengcopy

⭐ 29 · MIT · 推送 2026-07-11 · [GitHub](https://github.com/wuxie888/agent-skill-wannengcopy) · [官网](https://x.com/sciencedegens) · 个人维护 · 中文 README

**将参考网站混搭重构为原创产品站点的 agent 技能**

面向 Codex 与 Claude Code 的可安装 Agent Skill（SKILL.md 格式），用于把参考网站转化为原创产品网站。默认采用体验混搭工作流：保留参考站的结构、交互手感、动效语言与视觉节奏，替换受保护表面为原创文案、素材与流程；在拥有授权时也支持精确克隆。关键机制包括证据优先侦察（SOURCE/PARTIAL/GUESS 证据标签）、L1-L6 复杂度分级、五种操作模式、交付前审计（参考泄漏、权利风险、动效验证）。git clone 到 skills 目录即可安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 证据标签体系：SOURCE/PARTIAL/GUESS 区分直接证据与推断
- L1-L6 复杂度分级，覆盖静态页到 WebGL/SaaS 场景
- 五种操作模式：授权克隆/体验混搭/产品重构/动效重建/QA 修复
- 权利边界章节：默认替换受保护表面，需明确授权方可精确克隆

## 适用场景

- 把参考落地页混搭成自己产品的网站
- 重建保留交互节奏但产品逻辑不同的站点
- 修复此前克隆后产品逻辑薄弱的成品
- 重建 hero 动效、滚动编排与 Three.js/WebGL 场景

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14:  Agent Skill
> L21: Wannengcopy is a reusable Skill for turning a reference website into an original product website.

## 星数曲线

```mermaid
xychart-beta
    title "wuxie888/agent-skill-wannengcopy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fc9fda35f296` · [字段定义](../../DATASET.md)*
