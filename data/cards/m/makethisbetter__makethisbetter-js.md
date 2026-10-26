# makethisbetter/makethisbetter-js

⭐ 93 · TypeScript · MIT · 推送 2026-09-10 · [GitHub](https://github.com/makethisbetter/makethisbetter-js) · [官网](https://makethisbetter.dev) · 组织维护

**带标注截图与 AI 分诊的用户反馈挂件 SDK**

面向 Web 应用的前端反馈组件（npm/CDN 引入）：用户两步提交带标注截图、控制台错误、DOM 状态与浏览器信息的反馈，SDK 自动捕获元素选择器、错误位置等上下文，支持最长 60 秒的 rrweb 交互回放（不录屏不录音，凭据类敏感数据强制过滤），并基于暴怒点击、死点击、表单失败等信号主动邀请反馈。提交前 AI 助手可追问一个问题澄清需求，云端 AI 分诊将反馈转为结构化任务供 Claude Code、Cursor、Codex 等编码 agent 接手；Widget 也支持自建后端（此路径不含 AI 分诊）。内置 7 种语言、三级身份验证（匿名/JWT/动态 JWT）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标注截图 + 控制台错误 + DOM 状态 + 元素选择器的两步反馈提交
- 最长 60 秒 rrweb 交互回放，凭据类敏感数据固定过滤且不可关闭
- 6 种挫败信号检测（暴怒点击/死点击/错误页等）主动邀请反馈
- AI 分诊输出结构化任务，供 Claude Code/Cursor/Codex 编码 agent 接手
- 支持自建后端（Self-Hosting API）与 7 种内置语言

## 适用场景

- 在 Web 应用中收集带标注截图与回放的用户反馈
- 让用户报障直接流转为编码 agent 可处理的任务
- 检测用户挫败信号并主动触发反馈收集
- 自托管反馈后端并接入自有看板流程

## 场景标签

 · 领域:开发者工具/用户反馈

## 证据(README 行号)

> L20: This widget gives your users a way to report exactly what went wrong — annotated screenshot, console errors, DOM st
> L326: The cloud platform at makethisbetter.dev adds AI triage, dashboard, GitHub/Linear sync, and email notifications on

## 星数曲线

```mermaid
xychart-beta
    title "makethisbetter/makethisbetter-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-26 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `dfbf9ec9ab28` · [字段定义](../../DATASET.md)*
