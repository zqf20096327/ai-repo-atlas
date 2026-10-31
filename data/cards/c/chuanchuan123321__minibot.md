# chuanchuan123321/minibot

⭐ 14 · Python · 推送 2026-03-20 · [GitHub](https://github.com/chuanchuan123321/minibot) · 个人维护 · 中文 README

**终端 AI 自动化助手：自然语言操控系统与文件，可接飞书**

Python 实现的轻量级 AI 自动化工具，自称采用 SuperAgent 架构：通过循环推理-规划-执行完成多步任务，内置 shell、文件读写、PDF/Word 解析、Tavily 网络搜索、定时器等 20+ 工具。提供 CLI、桌面 UI、飞书网关三种交互模式，支持 OpenAI/Anthropic 及 OpenAI 兼容 API。三层记忆系统通过压缩（约 30,000→1,000 tokens）维持长任务上下文，历史以指针归档。从源码安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 循环决策执行多步任务，内置 20+ 工具（shell/文件/搜索/定时器）
- CLI、桌面 UI、飞书网关三种交互模式
- 三层记忆压缩系统，压缩摘要+指针归档维持长上下文
- 技能系统：SKILL.md 格式的模块化知识扩展，内置 web/github/python/pdf 技能

## 适用场景

- 用自然语言让 AI 在服务器上执行命令和管理文件
- 通过飞书远程下发任务并接收实时进度
- 长时间运行的后台自动化任务处理

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L15: Minibot is an ultra-lightweight AI automation tool with original SuperAgent architecture that executes tasks throug
> L40: - **Tool Executor**: Executes 20+ built-in tools

## 星数曲线

```mermaid
xychart-beta
    title "chuanchuan123321/minibot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1f3421168b7e` · [字段定义](../../DATASET.md)*
