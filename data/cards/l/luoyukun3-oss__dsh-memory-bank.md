# luoyukun3-oss/dsh-memory-bank

⭐ 3 · JavaScript · MIT · 推送 2026-11-09 · [GitHub](https://github.com/luoyukun3-oss/dsh-memory-bank) · 个人维护 · 中文 README

**给 Agent 用的零依赖按仓库隔离长期记忆系统**

以纯 Node 标准库实现的 Agent 记忆系统，通过 SessionStart、UserPromptSubmit、PreToolUse 等 hook 在会话开场注入 13 段摘要、每轮按提问召回条目并触发关键词联想，后台增量摄入对话流水。提供 bank/cli.mjs 的 31 个子命令覆盖事件库、情绪权重、做梦联想、LLM 结构化抽取、索引治理与召回诊断。每个仓库一套银行（repos/<slug>/）互不污染；注入总预算 8000 字按段配额，超出部分只能手动 recall/page 查询。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SessionStart 开场注入 13 段摘要，总预算 8000 字按段配额
- 31 个 CLI 子命令覆盖事件库/做梦/LLM 抽取/索引治理
- 纯 Node 标准库零外部依赖，38 个测试文件 719 条断言
- 检索含 IDF、按召回时间衰减的软遗忘与触发词联想

## 适用场景

- 让编码 Agent 跨会话保留待办、决策与教训
- 多个项目仓库各自维护互不污染的记忆库
- 定期备份并翻查 Agent 会话日志原文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: 给 Agent 用的**零依赖长期记忆系统**。核心主张一句话：**不靠助手"记得去读文件"，靠 hook 把该出现的东西自动送到模型眼前。**
> L9: |形态|纯 Node 标准库，**零外部依赖**|
> L19: |会话开场|`SessionStart`|注入 13 段摘要（全局偏好 / 待办索引 / 近期事件 / 决策 / 故障速查 / 程序记忆 / 教训索引 …），**总预算 8000 字**、按段配额|

## 星数曲线

```mermaid
xychart-beta
    title "luoyukun3-oss/dsh-memory-bank 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `3a9b799b28ad` · [字段定义](../../DATASET.md)*
