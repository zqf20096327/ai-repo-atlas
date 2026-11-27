# zucchini-chat/personal-agent-scaffold

⭐ 4 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/zucchini-chat/personal-agent-scaffold) · [官网](https://zucchini.chat) · 个人维护

**个人 AI 助理模板：在 Claude Code/Codex 中管理日程与事务**

以纯 git 仓库加 Markdown 文件形式提供的个人 AI agent 起点模板：agent 将文件作为记忆、git log 作为活动记录，首次启动时通过约 15 分钟的设置访谈写入用户目标与偏好，并迁移到私有远端。内置 8 种后台 agent（晨间简报、日历审计、新闻监控、周度回顾、仓库清理、邮件台、聊天阅读等），默认全部关闭需逐一开启。代码仅为 Python 3 与 git 依赖的小脚本，含事实去重钩子、隐私数据拦截等 Claude Code hook 机制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown 文件为记忆、git log 为活动日志的持久化机制
- 8 种后台 agent playbook，默认关闭、逐一开启
- one-fact-one-place 钩子在提交前拦截重复事实与死链
- data-guard 钩子拦截携带隐私值的网络操作

## 适用场景

- 按优先级目标自动规划每日日程并做晚间复盘
- 夜间审计未来 7 天日历与目标的一致性
- 筛选邮件与群聊消息，只推送需要本人处理的内容
- 记录 agent 出错场景并在新模型上回放对比

## 场景标签

`AI 助手` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: A starting point for a personal AI agent: a chief of staff and coach that runs in Claude Code or Codex, keeps your s
> L5: It is a plain git repo of markdown files. The agent reads them, keeps them current and commits every change, so the 
> L12: There is no installer. The code is a few small scripts that need nothing beyond Python 3 and git, plus the memory h

## 星数曲线

```mermaid
xychart-beta
    title "zucchini-chat/personal-agent-scaffold 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-26 4 → 2026-11-27 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `6aebc378065e` · [字段定义](../../DATASET.md)*
