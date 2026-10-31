# awesomo913/Claude-Token-Saver

⭐ 16 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/awesomo913/Claude-Token-Saver) · 个人维护

**本地代码搜索 CLI：只取所需函数片段喂给 Claude 省 token**

面向 Claude Code 用户的命令行工具：在本地为项目中的函数和类建立索引，用自然语言或名称（含拼写容错）检索，输出可直接粘贴的代码块及 token 计数，避免 Claude 整文件读取消耗上下文。另提供 bootstrap/prep 命令生成并维护 CLAUDE.md 项目概览与记忆文件，标记内生成、不覆盖用户笔记。支持 Python 与 JavaScript/TypeScript，单一依赖 tiktoken，全部本地运行。附 Windows 可选桌面应用。基准显示按名称检索效果较好，纯英文描述与拼写错误模式为弱项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言/名称检索函数与类，输出粘贴就绪代码块及 token 计数
- bootstrap 生成 CLAUDE.md 概览与记忆文件，标记内管理不覆盖用户内容
- 全部本地运行，代码不出本机；单一依赖 tiktoken
- requests/flask/rich 上的可复现基准，明示各模式命中率与弱项

## 适用场景

- 让 Claude Code 只读取需要的函数而非整个文件，节省 token 与上下文
- 为项目生成并自动刷新 CLAUDE.md 项目概览供 Claude Code 会话加载
- 在脚本中调用 search 定位代码块（无匹配时退出码 1）

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L25: - `token-saver search . "what you need" --source` returns just the matching
> L79: **1. Tell Claude to search before it opens files.** Add this to your

## 星数曲线

```mermaid
xychart-beta
    title "awesomo913/Claude-Token-Saver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `415225b6a76a` · [字段定义](../../DATASET.md)*
