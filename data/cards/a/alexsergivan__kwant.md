# alexsergivan/kwant

⭐ 710 · Rust · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/alexsergivan/kwant) · [官网](https://kwant.si) · 个人维护

**自托管的多 AI bot 团队协作应用：bot 互相交接、互检工作**

以单个二进制形式自托管运行的应用（Rust + 内嵌 React），提供多 bot 团队：消息经 @mention 在 bot 间交接，任务以卡片呈现在 Mission board，任务标记为 Verified 需系统自身运行检查而非仅凭 bot 陈述；0.9 系列加入 Inbox 审核、第二模型复核、浏览器页面定点指认、每任务独立 worktree 与例程等机制。支持 macOS/Linux/Windows(beta) 与服务器部署，配合已有的 Claude/Codex/Grok CLI 或自有 API key 使用。许可为 AGPL-3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- bot 间 @mention 交接工作，任务需系统自检通过才标记 Verified
- 审核流：Inbox 逐项裁决（Approve/Send back/Roll back），复核在另一模型的干净副本上运行
- 支持 Claude、Codex、Grok CLI 或自有 API key 接入
- macOS/Linux/Windows(beta) 安装包与服务器 binary/Docker 部署

## 适用场景

- 搭建一支自托管、互相检查工作的 AI bot 团队
- 让 bot 代为执行浏览、开发、例程类任务并按需审批
- 按工作/生活等空间隔离各自的 bot 与账号

## 场景标签

`多智能体` `AI 助手` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Your own team of AI bots that check each other’s work before saying “done”.
> L27: kwant gives you a team of bots that share chats, hand work to each other with an @mention and get it done on their 

## 星数曲线

```mermaid
xychart-beta
    title "alexsergivan/kwant 星数(近 20 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 0 --> 779
    line [13, 14, 15, 16, 361, 454, 494, 540, 522, 556, 594, 652, 692, 699, 682, 681, 683, 691, 701, 710]
```

2026-10-26 13 → 2026-11-26 710（+697）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 low · 依据 README sha `bbfd0d20a042` · [字段定义](../../DATASET.md)*
