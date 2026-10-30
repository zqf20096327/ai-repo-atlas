# s-gryt/memory-mason

⭐ 17 · JavaScript · MIT · 推送 2026-07-11 · [GitHub](https://github.com/s-gryt/memory-mason) · 个人维护

**把 AI 编程会话自动捕获为 Obsidian 知识库的插件**

以插件/hook 形式接入 AI 编程 agent（Claude Code、Copilot、Codex 等），自动将对话写入 Obsidian vault 的日志文件，经六阶段过滤管道（去标签、ANSI 清理、事件分类、散文压缩、敏感信息拦截、去重）后落盘；用 /mmc 将原始日志编译为概念页、MOC、综合页与会话摘要，/mmq 基于已编译知识库回答并附 wikilink 引用。无需 API key，数据全部本地。Cursor/Windsurf 等仅支持技能命令、无捕获 hook，需 Node.js。

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

- hook 自动捕获会话，六阶段过滤管道拦截凭据等敏感内容
- /mmc 编译为概念页、MOC、综合页并 wikilink 互链
- /mmq 从知识库检索回答并附来源引用
- lite/full 两种捕获模式与可选无损压缩，token 节省指标可查

## 适用场景

- 我想把每天与 AI 编程助手的对话沉淀成可检索的知识库
- 跨会话回顾某个概念或决策的来龙去脉
- 用 /mmq 在对话中直接查询过往经验而不离开 agent

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L17: Memory Mason hooks into your AI coding agent and silently captures every conversation into daily Obsidian logs. Whe
> L82: |**Claude Code**|`/plugin marketplace add s-gryt/memory-mason` then `/plugin install memory-mason@s-gryt`|

## 星数曲线

```mermaid
xychart-beta
    title "s-gryt/memory-mason 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `cf1dd351b762` · [字段定义](../../DATASET.md)*
