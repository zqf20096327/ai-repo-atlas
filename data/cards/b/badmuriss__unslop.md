# badmuriss/unslop

⭐ 21 · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/badmuriss/unslop) · 个人维护

**模型无关的 LLM 写作技能：清除 AI 文风痕迹并检测评分**

以跨 agent 技能文件（SKILL.md）形式提供的写作系统，可在 Claude Code、Codex、OpenCode、Cursor 等遵循指令文件的 agent 中运行，任何 LLM 也可将其作为纯指令集执行。提供 write/edit/detect/score/clean 五种模式：起草并清洗文风、仅审计不改动、按 5 维度量表评分（35/50 截断线）、区分散文改写与水印元数据清理。检测基于两层：维基百科 Signs of AI writing 表面特征与 StoryScope 叙事结构特征，另含强制加载的巴西葡萄牙语层。限制：clean 模式不声称证明人类作者身份，改写不得添加原文没有的事实。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- write/edit/detect/score/clean 五模式，按请求选择最小流水线
- 表面层（Wikipedia Signs of AI writing）+ 叙事层（StoryScope）双层检测
- 5 维度量表评分（每维 1-10，总分 35/50 截断），附 20 项二元自检 eval
- 巴西葡萄牙语专属特征层与作者语音校准（从样本提取句长、语气、节奏）

## 适用场景

- 让我的 agent 在写完初稿后自动清除 AI 文风痕迹
- 检测一段文本是否带 AI 写作模式并逐行列出证据
- 按量表为文案或长文打分，低于阈值自动重写
- 清理巴西葡萄牙语文本中的本地化 AI 痕迹

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L18: Cross-agent skills format — works with Claude Code, Codex, OpenCode, Cursor, and any agent that can follow an instr
> L30: Then ask for a mode: "write a launch post about X", "unslop this", "is this text AI?", "score this", or "remove the
> L45: |Mode|You say|It does|

## 星数曲线

```mermaid
xychart-beta
    title "badmuriss/unslop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `984a66b25441` · [字段定义](../../DATASET.md)*
