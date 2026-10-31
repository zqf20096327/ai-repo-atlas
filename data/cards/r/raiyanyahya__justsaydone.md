# raiyanyahya/justsaydone

⭐ 33 · Python · MIT · 推送 2026-07-06 · [GitHub](https://github.com/raiyanyahya/justsaydone) · 个人维护

**让 Claude Code 只回一个词的输出风格插件，省输出 token**

以 Claude Code 插件形式发布的单个输出风格（output style），通过 force-for-plugin: true 在安装后自动生效，使 Claude 在完成任务后仅回复 done 等极简内容，以减少回复文字与输出 token 消耗。Claude 的规划、编辑、运行与验证流程不变（keep-coding-instructions: true）。消息包含 explain/why/details 等关键词时该轮恢复完整回答；任务失败时以一行说明而非 done。附带回购基准测试脚本（需 claude CLI、jq、python3）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 安装后自动生效的 Claude Code 输出风格插件
- explain/why/summarize 等关键词触发单轮完整回答的逃生通道
- 任务失败或受阻时输出一行说明，不以 done 谎报成功
- 基准测试脚本可复现 A/B 对比结果并作回归检查

## 适用场景

- 希望 Claude Code 少说客套话、直接看 diff 的开发者
- 降低会话中的输出 token 花费
- 对回复简短化效果做可复现的基准验证

## 场景标签

 · 领域:开发者工具/LLM 客户端插件

## 证据(README 行号)

> L8: **A mode for Claude Code that does the work and replies with one word.**
> L133: A single output style shipped as a
> L134: plugin with `force-for-plugin: true`. That flag is what makes it apply automatically on

## 星数曲线

```mermaid
xychart-beta
    title "raiyanyahya/justsaydone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f6f766d6b621` · [字段定义](../../DATASET.md)*
