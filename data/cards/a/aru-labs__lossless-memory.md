# aru-labs/lossless-memory

⭐ 146 · Python · MIT · 推送 2026-09-23 · [GitHub](https://github.com/aru-labs/lossless-memory) · [官网](https://note.com/aru_log) · 个人维护

**个人 AI 的本地无损长期记忆层：全量留痕、全量打时间戳**

面向单用户单机的 AI 助手长期记忆层：原始对话以七字段记录逐条写入按日 JSONL，SQLite FTS5 做精确检索、sqlite-vec 做语义兜底。核心机制是以时间为主轴的 Temporal Backbone——查询解析器先识别英文/日文相对时间短语与绝对日期缩小范围，再做词序排序，结果按时间序原样返回；另有 LLL 主题索引每轮注入模型上下文。明确不做摘要、无基准测试；支持两种导入格式（含 claude_code 转录），CPU 可运行，GPU 可选。开发当前暂停。

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

- 原始对话全量保存，任何索引可从日志重建
- 时间短语先缩范围再排序，结果带时间戳按时间序返回
- LLL 当前话题索引每轮注入，上下文压缩后延续对话
- SQLite FTS5 精确检索 + sqlite-vec 语义兜底，本地无服务器

## 适用场景

- 让每日使用的个人 AI 助手记住原话与时间
- 查询『上周二晚上我们决定了什么』这类带时间的对话
- 在自有硬件上为长期陪伴型 AI 搭建记忆层

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L20: - A local, file-based long-term memory layer: JSONL logs + SQLite (FTS5 for exact search, sqlite-vec for semantic s
> L22: - A "current position" index (LLL) designed to be injected into the model's context on every turn.

## 星数曲线

```mermaid
xychart-beta
    title "aru-labs/lossless-memory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 143 --> 147
    line [144, 146, 146]
```

2026-10-18 144 → 2026-10-25 146（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3cf3a4d7d229` · [字段定义](../../DATASET.md)*
