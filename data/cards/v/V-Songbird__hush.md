# V-Songbird/hush

⭐ 54 · JavaScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/V-Songbird/hush) · [官网](https://github.com/V-Songbird/foundry) · 个人维护

**Claude Code 插件：减少过程解说、缩短工具输出**

面向 Claude Code 用户的插件，通过写作风格设定与会话控制减少助手的例行解说、裁剪冗长工具输出，并将最终回答聚焦于变更内容与后续步骤；大输出可暂存为临时文件并保留引用供查看。通过 /plugin 命令安装，要求 Claude Code 2.1.139+ 与 Node.js 22+。README 附带 36 会话测量数据：中位最终回答缩短约 27%，但 Opus 5.5 上平均账单高 9%；不提供 Codex 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 写作风格 + 会话控制减少例行解说与长工具输出
- /hush:config 提供答案布局配置（长度、结构、卡片/链接等）
- 大输出暂存临时文件并保留引用
- README 提供带测量条件的基准数据（36 会话）

## 适用场景

- 减少 Claude Code 会话中的过程性叙述，直接看结果
- 避免冗长命令输出挤占对话上下文
- 需要时通过引用回查被截断的完整输出

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L31: A writing style asks the assistant to stay quiet during routine work and finish with a short, useful answer. Sessio
> L52: /plugin install hush@foundry

## 星数曲线

```mermaid
xychart-beta
    title "V-Songbird/hush 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-25 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a664a5a08485` · [字段定义](../../DATASET.md)*
