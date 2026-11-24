# MacHatter1/bb-plugin-followups

⭐ — · [GitHub]() · 个人维护

**BB 插件：线程结束后在其输入框上方生成可点击的追问建议**

面向 BB（bb ≥ 0.45）的 TypeScript 插件：当 agent 线程结束时，以隐藏 worker 线程调用所选模型，从最后一条回答（保留其结尾提议）与用户最近三条消息中抽取 2–5 条追问建议，连同理由显示在输入框上方的横幅中；点击即填入完整草稿，但不代替用户发送。支持逐线程开关、compact/detailed 两种提示模式、耗时与 token 展示、最多四个并发 worker 及其用后归档清理。安装需 BB Plugin SDK ≥ 0.6.15，仓库为私有，安装机器需有访问权限的 GitHub 凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从线程最后回答生成带理由的追问建议，一键填入草稿但不自动发送
- 最多四个 suggestion worker 并发，输出用后或失效即归档清理
- CLI（bb followups show/off/model/regenerate/draft 等）支持查询与手动触发
- 页脚显示每次运行的耗时与 token 拆分（输入/缓存/输出/推理）

## 适用场景

- agent 回答后快速选择下一步追问而无需手动打字
- 按线程控制是否启用追问建议
- 查看每条建议生成的时间与 token 成本
- 清理或回填遗留的 Codex worker 聊天记录

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L43: When a thread finishes, a model drafts follow-ups from its last answer,
> L92: - bb **0.45+** (Plugin SDK 0.6.15+)
> L95: - A provider BB can run models on. Every suggestion and draft is a short run

## 星数曲线

```mermaid
xychart-beta
    title "MacHatter1/bb-plugin-followups 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-22 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `7b6e364084ce` · [字段定义](../../DATASET.md)*
