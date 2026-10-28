# gelatinousdevelopment/buildermark

⭐ 24 · Go · MIT · 推送 2026-04-24 · [GitHub](https://github.com/gelatinousdevelopment/buildermark) · [官网](https://buildermark.dev) · 个人维护

**本地统计代码提交中由 AI 编程代理编写比例的工具**

面向使用编码代理的开发者的本地分析工具：导入 Claude Code、Codex、Gemini、Cursor 等代理的对话历史与本地 git 提交记录，将对话 diff 与提交 diff 做格式无关的匹配，计算各提交的代理编写占比；同时归档代理对话、支持手动或技能评分、发送带归属信息的系统通知。后台由本地 Go 服务器与 sqlite 数据库驱动，数据不出机器。提供 macOS/Windows 应用与 Linux CLI，另配浏览器扩展从云端代理服务导入对话。

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

- 对话 diff 与提交 diff 的格式无关匹配，计算代理编写比例
- 归档 Claude Code/Codex/Gemini/Cursor 等代理的对话历史
- 本地运行（localhost:55022 Go 服务 + sqlite），无账号无云端无分析
- Chrome/Firefox/Safari 扩展从 Claude Code Cloud 与 Codex Cloud 导入对话

## 适用场景

- 统计我的仓库里有多少代码由编码代理编写
- 归档并检索本机上的代理对话历史
- 在提交通知中查看每次提交的代理归属

## 场景标签

 · 领域:开发者工具/编码代理度量

## 证据(README 行号)

> L5: Buildermark matches your coding agent diffs with commits. It runs locally in the background archiving your agent con
> L9: - **Formatting-agnostic diff matching** - Buildermark matches agent output to your commits even when formatting diff

## 星数曲线

```mermaid
xychart-beta
    title "gelatinousdevelopment/buildermark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `833d7df8bac2` · [字段定义](../../DATASET.md)*
