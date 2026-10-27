# ViryaZheng/promptly-prompt

⭐ 38 · Python · MIT · 推送 2026-07-04 · [GitHub](https://github.com/ViryaZheng/promptly-prompt) · [官网](https://www.promptly-prompt.com/) · 个人维护 · 中文 README

**Claude Code 钩子：拦截模糊 prompt 并注入对齐纪律**

面向 Claude Code 用户的插件，通过 UserPromptSubmit 钩子在提交时对 prompt 做'清晰度'规则打分（模糊动词、含糊措辞、悬空指代等加分，代码锚点、结构、明确成功标准减分），分数≥3 时注入两条纪律：复述请求对齐理解、先诊断根因并检索领域成熟做法再执行。注入语言随 prompt 语言切换（中/英）。无 API 调用，仅依赖 Python 标准库，运行耗时声明 <50ms。通过 claude plugin 市场命令安装，聊天界面需手动粘贴自定义指令替代。

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

- UserPromptSubmit 钩子按规则信号对 prompt 清晰度打分，≥3 触发注入
- 注入两条纪律：复述对齐 + 先诊断并检索领域成熟做法
- 注入内容跟随 prompt 语言（中/英文协议）
- 无 API 调用，仅依赖 Python 标准库

## 适用场景

- 在 Claude Code 中自动拦截模糊 prompt，先对齐再执行
- 避免 AI 误解需求就开工导致的返工
- 无钩子的聊天界面用两句话自定义指令获得同类效果

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: A `UserPromptSubmit` hook that acts as a **clarity gate**: it intercepts unclear prompts — vague verbs with no succe
> L61: The hook scores every prompt's **unclarity** — not complexity, not length — using rule-based signals:

## 星数曲线

```mermaid
xychart-beta
    title "ViryaZheng/promptly-prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-27 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7d9ccb45e3f9` · [字段定义](../../DATASET.md)*
