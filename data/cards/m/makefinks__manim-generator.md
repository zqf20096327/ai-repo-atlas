# makefinks/manim-generator

⭐ 119 · Python · MIT · 推送 2026-09-04 · [GitHub](https://github.com/makefinks/manim-generator) · 个人维护

**LLM 自动生成 Manim 数学动画视频的命令行工具**

基于 agentic LLM 流程自动生成 Manim 动画的 Python 命令行工具：Code Writer 负责起草 Manim 代码，Code Reviewer 负责审查，二者通过多轮迭代反馈与执行日志降低渲染失败率，并支持可选的视觉输入。经 LiteLLM 路由模型，OpenRouter 及 OpenAI/Anthropic 直连均可接入以对比不同模型。需配置 API key，另需安装 ffmpeg（LaTeX 为可选）。项目同时驱动公开排行榜 Manim Bench 展示各模型的生成效果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Code Writer / Code Reviewer 反馈循环，默认 5 轮审查
- LiteLLM 路由，支持 OpenRouter 前缀及 OpenAI/Anthropic 直连
- 场景渲染成功率阈值触发视觉审查模式，支持帧提取
- 提供 manim-generate CLI，支持流式输出与 reasoning token 配置

## 适用场景

- 用自然语言描述生成数学/概念解释动画
- 对比不同 LLM 在完整 Manim 视频生成任务上的表现
- 批量运行 bench_prompts 中的标准提示做基准测试

## 场景标签

`视频生成` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Automatic video generation using an agentic LLM flow in combination with the manim python library.
> L7: The project experiments with automated Manim video creation. An agent workflow delegates code drafting to a `Code Wr
> L13: The manim-generator harness now drives **Manim Bench**, a public leaderboard showcasing how latest AI models compar

## 星数曲线

```mermaid
xychart-beta
    title "makefinks/manim-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-26 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `bdf2f7a14b89` · [字段定义](../../DATASET.md)*
