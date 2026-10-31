# Ddhjx-code/writeAgent

⭐ 16 · 推送 2026-05-18 · [GitHub](https://github.com/Ddhjx-code/writeAgent) · 个人维护 · 中文 README

**基于 Claude Code 的多 Agent 协作长篇小说创作框架**

运行于 Claude Code 之上的小说创作工作流框架：主 Agent（编剧）协调 planner/writer/reviewer/polisher 四个子 Agent，按 规划→写作→审查→润色→归档 流程逐章创作。信息通过技能包与故事圣经（bible）文件持久化，不依赖对话上下文，支持中断恢复。reviewer 按十维度打分（满分 50），设五个人类确认节点。依赖 Claude Code 的 Task 工具与技能包系统，克隆项目后在 Claude Code 中对话启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个子 Agent 分工（规划/写作/审查/润色），主 Agent 协调
- 十维度审查评分体系（满分 50 分，通过线 35 分）
- 文件即记忆：bible 与技能包持久化，支持中断恢复
- 五个暂停等待人类确认的人机协同节点

## 适用场景

- 在人类作家把控方向下完成长篇小说的逐章创作
- 对 AI 生成的章节做多维度质量审查与去 AI 味润色
- 跨多个会话持续维护人物、世界观、悬念与伏笔设定

## 场景标签

`多智能体` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L3: 基于Claude Code的多Agent协作小说创作框架。通过四个专业子Agent分工协作，在人类作家的创意指导下完成长篇小说的规划、写作、审查和润色。
> L199: - 依赖Claude Code的Task工具实现多Agent协作

## 星数曲线

```mermaid
xychart-beta
    title "Ddhjx-code/writeAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c201628550c6` · [字段定义](../../DATASET.md)*
