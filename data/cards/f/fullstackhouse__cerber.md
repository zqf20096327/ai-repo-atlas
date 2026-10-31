# fullstackhouse/cerber

⭐ 14 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/fullstackhouse/cerber) · [官网](https://fullstack.house/blog/cerber) · 组织维护

**本地优先的 AI 代码评审驾驶舱：Claude 起草，人来决定发送**

面向开发者的人审环 AI 代码评审工具：调用已登录的 claude CLI 为 GitHub PR 生成摘要、分章变更走读、内联草稿评论与带置信度的裁决，产物为本地 JSON 文件，在本地 Web 驾驶舱中阅读、改写或丢弃。审阅过程 100% 本地只读，三种写回 GitHub 的途径均由人触发。硬性依赖 Claude Code 付费订阅、Node 22+、gh 与 git；仅支持 GitHub，通知仅 macOS/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 评审产物为 ~/.cerber/reviews/ 下的纯 JSON（摘要/章节/草稿评论/裁决与置信度）
- 审阅 100% 本地只读，发送需人工点击，无 API key 路径
- cerber serve 轮询 GitHub 自动起草待审 PR，配合桌面通知与键盘导航
- 支持就 diff 某一行向评审者追问并让其修订自身评论

## 适用场景

- 在本地驾驶舱中批量处理待审 PR，只发送自己认可的评论
- 用 Claude 起草 PR 评审后逐条取舍再发布到 GitHub
- 对自己的 PR 按 r 键发起自我评审

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: **AI code-review cockpit.** Claude reviews your pull requests into local
> L60: **Claude Code is a hard requirement, and a paid one.** Cerber drafts reviews by

## 星数曲线

```mermaid
xychart-beta
    title "fullstackhouse/cerber 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `88193734d550` · [字段定义](../../DATASET.md)*
