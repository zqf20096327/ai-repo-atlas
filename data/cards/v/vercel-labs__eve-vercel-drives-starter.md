# vercel-labs/eve-vercel-drives-starter

⭐ 4 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/vercel-labs/eve-vercel-drives-starter) · [官网](https://vercel.com/templates/eve/eve-vercel-drives-starter) · 组织维护

**基于 eve 与 Vercel Drives 的文件管理 agent 起始模板**

一个 starter 模板：部署一个 eve agent，通过 Slack 或终端对话读取和保存团队在 Vercel Drive 上的文件。每个会话在 Vercel Sandbox 中获得 Drive 的只读快照，用 shell 命令与 read_file 检索；save_to_drive 工具以短暂读写挂载写回文件，读写挂载互斥时返回 drive_busy。沙箱无网络访问，模板关闭 web_fetch/web_search。需 Node.js 24 与 pnpm，经 Vercel 项目流程部署并经 Vercel Connect 安装 Slack 应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 会话沙箱挂载 Drive 只读快照，用 ls/find/grep/read_file 检索
- save_to_drive 以短时读写挂载写回文件，busy 时提供重试
- 沙箱禁用网络与 web_fetch/web_search，限制文件外传
- 支持经 Vercel 项目流程部署与 Slack 接入

## 适用场景

- 团队文件上传 Drive 后在 Slack 中 @agent 问答检索
- 让 agent 把讨论摘要保存为 Drive 上的笔记文档
- 本地终端与部署实例共用同一 Drive 进行开发调试

## 场景标签

`文档问答` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: An eve agent that reads and saves your team's files on a Vercel Drive. Each session gets a read-only snapshot of the
> L19: |Agent framework|eve|
> L26: A session is one Slack thread, or one chat started with `pnpm dev`. When a session first uses its sandbox, the sand

## 星数曲线

```mermaid
xychart-beta
    title "vercel-labs/eve-vercel-drives-starter 星数(近 3 点)"
    x-axis ["2026-10-24", "2026-11-14", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-24 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `959bcbb00007` · [字段定义](../../DATASET.md)*
