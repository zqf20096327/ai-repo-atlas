# anantbhandarkar/make-it-right

⭐ 15 · Python · Apache-2.0 · 推送 2026-08-29 · [GitHub](https://github.com/anantbhandarkar/make-it-right) · 个人维护

**给 AI 编码 agent 的约束先行后端可靠性技能库**

面向 Claude Code、Codex CLI、Antigravity、Cursor 四类编码 agent 宿主的可复用技能库：52 个技能按 7 大领域→运行时→框架三级组织，在任务开始前让 agent 先提问、确认假设、确认计划再写代码；提供 Bash 安装器以符号链接方式安装技能，`mir init` 命令为单个仓库生成栈专属指引与可选写保护（guard.py 检查文件写入路径）。README 明确声明结果不保证每次变更安全，写保护效果依赖宿主是否调用 hook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 52 个技能按 7 领域/9 运行时/框架三级路由（约 17400 token 简短描述常驻）
- 八步工作流，其中 3 步暂停等待用户输入
- `mir init` 生成项目栈指引与写保护检查器（guard.py/probe.py）
- Bash 安装器支持 4 种 agent 宿主，符号链接方式安装

## 适用场景

- 让 AI 编码 agent 在改数据库表、支付重试等后端变更前先确认关键约束
- 限制 agent 只能写入批准的项目路径，保护密钥与配置
- 为特定技术栈（如 Python+FastAPI）加载对应的工程指引

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L15: Make It Right helps an AI coding agent pause before a risky change. It asks for missing context, confirms the plan,
> L17: It is a small library of reusable skills, reviewer checklists, and a per-project setup command called `mir init`.
> L89: ## Supported hosts

## 星数曲线

```mermaid
xychart-beta
    title "anantbhandarkar/make-it-right 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3e3fd63433ed` · [字段定义](../../DATASET.md)*
