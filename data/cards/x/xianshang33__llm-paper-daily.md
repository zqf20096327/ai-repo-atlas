# xianshang33/llm-paper-daily

⭐ 1,345 · Python · 推送 2026-11-23 · [GitHub](https://github.com/xianshang33/llm-paper-daily) · 个人维护 · 中文 README

**给 LLM/Agent 研究者的每日论文更新与分类订阅源**

该仓库每日收录 LLM、Agent 相关研究论文，按日期组织列表，每条附 arXiv 链接、相关 GitHub 仓库和中文摘要总结。订阅方式是通过仓库提供的 prompt 交给本地 Agent（OpenClaw/Codex/Claude Code），由其读取仓库根目录 SUBSCRIBE.md 完成本地配置，并只读取公开的 feed-papers.json，不在本机运行抓取或总结流程，同时安装定时任务实现每日推送。本体是论文精选与分类展示平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每日更新 LLM、Agent 论文并附 arXiv 地址与中文摘要
- 通过 paper-subscribe skill 的 Agent 配置完成本地订阅
- 订阅仅读取公开 feed-papers.json，不运行抓取流程
- 提供定时任务推送的 digest 配置流程

## 适用场景

- 每天追踪 LLM 与 Agent 领域最新论文
- 让本地 Agent 帮我配置论文日报订阅
- 按日期浏览论文并快速看中文总结

## 场景标签

`科研工具` `精选清单` · 领域:学习与行业

## 证据(README 行号)

> L5: 欢迎来到 **llm-paper-daily**! 这是一个获取 LLM、Agent 相关研究论文的每日更新和分类平台。
> L7: 📚 **每日更新:** 仓库每天会带来最新的 LLM、Agent 相关研究，并附有 arXiv 地址、相关 GitHub 仓库和文章的总结。
> L25: Agent 会使用仓库里的 `paper-subscribe` skill，只读取公开的 `feed-papers.json`，不会在你的机器上运行论文抓取或总结生产流程。

## 星数曲线

```mermaid
xychart-beta
    title "xianshang33/llm-paper-daily 星数(近 14 点)"
    x-axis ["2026-10-23", "2026-10-27", "2026-10-29", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-25"]
    y-axis "stars" 1336 --> 1347
    line [1337, 1338, 1337, 1339, 1340, 1337, 1340, 1341, 1342, 1343, 1345, 1346, 1345, 1345]
```

2026-10-23 1,337 → 2026-11-25 1,345（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `29a8336c08cc` · [字段定义](../../DATASET.md)*
