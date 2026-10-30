# roy-reshef/socratic-ai-prompt-skill

⭐ 16 · 推送 2026-02-24 · [GitHub](https://github.com/roy-reshef/socratic-ai-prompt-skill) · 个人维护

**将 AI agent 从直接答题者转为苏格拉底式提问者的提示技能**

一个面向 AI agent 的提示工程技能（prompt skill）：拦截用户请求后，先做领域检索，再将请求改写为苏格拉底对话框架，经用户确认后执行。核心原则包括先提问后执行、显式化隐含假设、迭代精炼与角色反转（AI 作为引导者而非答案提供者）。以技能文件形式添加到 Agent 配置中使用，未给出具体安装命令。README 列明了适用与不适用场景（事务性任务、语法查询、紧急修复等不适用）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拦截请求→领域检索→改写为苏格拉底对话框架→用户批准后执行的流程
- 四项核心原则：先提问后执行、假设显式化、迭代精炼、角色反转
- 明确列出适用场景（架构设计、调试思路、学习概念、战略规划）与跳过场景（事务性任务、快速查询）

## 适用场景

- 做技术选型或架构设计时让 AI 通过追问帮我暴露忽略的权衡
- 学习新库或语言时让 AI 引导我自己得出答案而非直接给代码
- 感到思路陷入套路时把 AI 当作陪练推动出原创角度

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: This skill intercepts a standard request, performs domain research (if necessary), transforms the request into a ri
> L14: Once the skill is added to your Agent configuration:

## 星数曲线

```mermaid
xychart-beta
    title "roy-reshef/socratic-ai-prompt-skill 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-29", "2026-10-30"]
    y-axis "stars" 11 --> 17
    line [12, 13, 15, 16, 16]
```

2026-10-18 12 → 2026-10-30 16（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `ec821c691144` · [字段定义](../../DATASET.md)*
