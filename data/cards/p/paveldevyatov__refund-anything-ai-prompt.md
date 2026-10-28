# paveldevyatov/refund-anything-ai-prompt

⭐ 96 · MIT · 推送 2026-10-06 · [GitHub](https://github.com/paveldevyatov/refund-anything-ai-prompt) · 个人维护

**把 AI 变成个人退款助手的提示词/agent 技能**

一个单文件提示词（PROMPT.md），粘贴进 Claude、ChatGPT 等 AI 后，可让模型读取票据、调查公司退款政策并生成退款申请信；采用两阶段策略：先礼貌协商信，被拒后生成引用具体法条（45+ 司法辖区）与升级路径（监管投诉、拒付、小额诉讼）的信函；无真实理由时会如实告知。也可通过 npx skills 命令作为 get-refund 技能安装到 Claude Code、Codex、Cursor 等编码 agent。README 声明非法务建议，法条需自行核验。

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

- 两阶段策略：先礼貌协商信，后法律升级信
- 内置 45+ 司法辖区的消费者保护法条引用参考
- 读取票据/邮件/截图并调查公司退款政策
- 可作为技能安装到 Claude Code 等编码 agent

## 适用场景

- 订阅、数字购买、预订等场景向商家申请退款
- 退款被拒后获得引用法条的升级信函与投诉路径
- 判断自己的退款请求是否有实际依据

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: A single, self-contained prompt that turns Claude, ChatGPT, or any other capable AI into your personal refund assist
> L18: Using Claude Code, Codex, Cursor or another coding agent? Install it as a skill instead:

## 星数曲线

```mermaid
xychart-beta
    title "paveldevyatov/refund-anything-ai-prompt 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-28 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `263df5afb26c` · [字段定义](../../DATASET.md)*
