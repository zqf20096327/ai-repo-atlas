# generativelabs/g-genlabs-skill-tldr

⭐ 5 · MIT · 推送 2026-10-21 · [GitHub](https://github.com/generativelabs/g-genlabs-skill-tldr) · [官网](https://www.generativelabs.com/?utm_source=github&utm_medium=referral&utm_campaign=skill_tldr) · 组织维护

**Claude Code 技能：将长回复压缩为不丢事实的分组短要点**

以 Claude Code skill 形式安装的斜杠命令工具：输入 /tldr 将上一条长回复改写为分组的短要点，声明保留全部事实、数字、路径、决策与未完成项，仅删去连接性文字；/tldr super 为更激进压缩档，可指定压缩对象（某条消息、只留决策/数字），支持会话级 on 模式持续生效。代码块、命令与错误文本不做压缩。通过 git clone 到 ~/.claude/skills 安装，MIT 许可，由 Generative Labs 维护。

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

- /tldr 一次压缩、/tldr on 会话内持续压缩，/tldr super 更紧凑档
- 声明保留每条事实、数字、路径、决策与开放项，仅删连接性文字
- 可指定压缩对象（早前消息、仅决策、仅数字）
- 代码块、命令、错误文本永不压缩

## 适用场景

- 阅读 Claude Code 的长篇排障回复时压缩为要点
- 保持会话所有回复为短要点形式
- 只提取一段回复中的决策或数字

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: A Claude Code skill that turns long replies into short grouped bullets without dropping any facts. Type `/tldr` afte
> L11: Start a new Claude Code session and `/tldr` is available. To install it for one project only, clone it into that pr

## 星数曲线

```mermaid
xychart-beta
    title "generativelabs/g-genlabs-skill-tldr 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-08", "2026-11-22"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-02 4 → 2026-11-22 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a07d6cb4f3a0` · [字段定义](../../DATASET.md)*
