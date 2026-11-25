# alexsergivan/kwant

⭐ 701 · Rust · AGPL-3.0 · 推送 2026-11-24 · [GitHub](https://github.com/alexsergivan/kwant) · [官网](https://kwant.si) · 个人维护

**自托管的 AI 机器人团队应用：分工协作与人工审批**

以单个二进制形式自托管的 AI 机器人团队应用：用户把消息发到共享频道，按 @mention 在机器人之间转交工作，任务以卡片形式呈现在 Mission board 上，只有系统自身运行检查通过后才标记为 Verified。支持按空间隔离不同用途的机器人与账号、定时例程、Inbox 审批（通过/退回/回滚）、由另一模型在干净副本上做二次检查，并内置团队浏览器（每任务独立页面、登录共享）。技术栈为 Rust（Tokio/Axum/SQLite）加内嵌 React 网页，提供 macOS、Linux（.deb/AppImage）、Docker 部署方式，接入用户已有的 Claude、Codex 或 Grok CLI 或自己的 API key。

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

- @mention 机器人间转交工作，消息自动路由到合适的机器人
- 任务需系统自身运行检查通过才标记 Verified，Inbox 提供审批与回滚
- 另一模型在文件干净副本上执行二次检查，高风险任务做变异测试
- 内置团队浏览器：每任务独立页面、共享登录、CAPTCHA 弹窗处理

## 适用场景

- 让一组机器人互相检查并完成自动化任务
- 为机器人的每项支出设置月度预算与告警
- 在浏览器自动化流程中保留人工审批节点

## 场景标签

`多智能体` `浏览器自动化` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Your own team of AI bots that check each other’s work before saying “done”.
> L27: kwant gives you a team of bots that share chats, hand work to each other with an @mention and get it done on their 
> L29: It's written in Rust (Tokio, Axum, SQLite) with a React web app embedded in the binary.

## 星数曲线

```mermaid
xychart-beta
    title "alexsergivan/kwant 星数(近 19 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 0 --> 769
    line [13, 14, 15, 16, 361, 454, 494, 540, 522, 556, 594, 652, 692, 699, 682, 681, 683, 691, 701]
```

2026-10-26 13 → 2026-11-25 701（+688）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `4e00a0fe4533` · [字段定义](../../DATASET.md)*
