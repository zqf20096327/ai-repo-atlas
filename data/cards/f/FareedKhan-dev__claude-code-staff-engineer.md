# FareedKhan-dev/claude-code-staff-engineer

⭐ 93 · Shell · MIT · 推送 2026-04-13 · [GitHub](https://github.com/FareedKhan-dev/claude-code-staff-engineer) · [官网](https://medium.com/@fareedkhandev/building-a-senior-staff-engineer-with-sub-agent-teams-in-claude-code-771298151392) · 个人维护

**教程/博文：用 Claude Code 构建带子代理团队的高级工程师代理**

作者 Fareed Khan 撰写的长文教程，讲解如何在 Claude Code 中搭建一个由 Architect、Tech Lead、Manager 等角色子代理组成的工程团队系统。内容包括：目录结构设计（agents/skills/hooks/commands）、会话启动 hooks 跨平台脚本、加载 SKILL.md 到上下文的机制、1% 规则与技能发现流程、指令优先级等组织化设计。产出物为教程文本与配置/脚本示例，覆盖 Claude Code、Cursor、Copilot CLI 三种平台格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定义角色分工的子代理团队结构（架构/计划/执行/评审）
- session-start hook 在每次会话注入核心技能文件
- 1% 规则与红旗表约束代理跳过流程的行为
- 同一脚本适配 Claude Code、Cursor、Copilot CLI 三种上下文格式

## 适用场景

- 学习如何用 hooks/skills/agents 组织 Claude Code 子代理协作
- 为自己的 AI 编码代理搭建会话初始化与技能发现流程
- 参考跨平台（Claude Code/Cursor/Copilot CLI）上下文注入脚本

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: The difference between a Junior and a Senior engineer isn’t syntax, it’s predictability, risk management, and discip
> L16: In this blog we are going to …
> L18: > visually walk through each stage of this workflow, build every component step by step from hooks to skills to age

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/claude-code-staff-engineer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-25 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `4c1b5570f7d6` · [字段定义](../../DATASET.md)*
