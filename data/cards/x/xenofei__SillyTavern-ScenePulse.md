# xenofei/SillyTavern-ScenePulse

⭐ 23 · JavaScript · GPL-3.0 · 推送 2026-04-27 · [GitHub](https://github.com/xenofei/SillyTavern-ScenePulse) · [官网](https://github.com/xenofei/SillyTavern-ScenePulse#readme) · 个人维护

**SillyTavern 扩展：从 AI 回复实时提取并追踪角色/关系/任务/氛围**

SillyTavern 角色扮演前端的扩展：每次 AI 回复后自动解析 LLM 输出，抽取场景环境、角色档案（外观/内心想法/物品栏）、五维关系数值（好感/渴望/信任/压力/契合度，0-100）、任务日志与心情张力等结构化数据，在实时仪表盘展示；附带角色 Wiki、关系网图、时间线快照浏览、剧情点子生成与斜杠命令/自定义宏。内置 39 个模型预设（DeepSeek、Claude、GPT、Gemini、GLM 等），支持多套 Prompt+Schema 档案切换与导入导出。提供 Token 用量分析与崩溃日志面板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条 AI 消息自动生成快照，追踪角色/关系/任务/环境并在实时仪表盘展示
- 39 个内置模型预设（DeepSeek/Claude/GPT/Gemini/GLM/Kimi 等），可社区贡献调优
- Prompt+Schema 档案系统：按对话覆盖、导入导出、斜杠命令切换
- 时间线快照浏览、角色 Wiki、关系网 SVG 图、Token 用量分析、5 种主题

## 适用场景

- 长篇角色扮演中追踪多角色关系与任务进展，避免遗忘剧情细节
- 通过仪表盘和时间线回看任意历史时刻的场景状态
- 将场景状态以宏变量注入提示词，保持剧情一致性

## 场景标签

 · 领域:游戏/角色扮演工具

## 证据(README 行号)

> L13: ScenePulse is a SillyTavern extension that automatically extracts and tracks scene data from AI responses — charact
> L41: - **Real-time updates** every AI message

## 星数曲线

```mermaid
xychart-beta
    title "xenofei/SillyTavern-ScenePulse 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [23, 22, 23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7235024c50cd` · [字段定义](../../DATASET.md)*
