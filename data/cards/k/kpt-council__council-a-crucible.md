# kpt-council/council-a-crucible

⭐ 15 · NOASSERTION · 推送 2026-07-18 · [GitHub](https://github.com/kpt-council/council-a-crucible) · 个人维护

**在 Claude 会话内运行的结构化对话提示框架（四模式）**

Council — A Crucible 是一套结构化提示/对话框架，以文档（Runtime Directive）形式加载进 Claude 会话运行。通过 persona 描述与寄存器指令，将同一模型分解为多个受约束的"透镜"进行多角度推理：council（分析/命题检验）、forge（行动方向压力测试）、marrow（经验与情感议题）、yohaku（未成形的直觉）。支持模块扩展（Wanjiru、Handoff）与模块准入接口；共五份文档，仅 RT 为运行必需。README 声明其非多独立 agent，也不作为模型内部经验的证据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四种对话模式：council/forge/marrow/yohaku，分别对应分析、行动、体验与直觉
- 将单一模型分解为多个受约束透镜，多角度推理并允许分歧存在
- 模块系统开放，公开两个模块（Wanjiru 会话引导、Handoff 会话交接文档）
- 五份配套文档（RT/DS/MA/PM/MCG），仅运行时指令为必需

## 适用场景

- 在 Claude 会话中对重要决策或命题做多角度压力测试
- 检验单一回答可能遗漏的前提与过度声明
- 以不同认知/情感寄存器处理分析框架外的议题

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L25: Council — A Crucible is a structured dialogue framework that runs inside a Claude context window. It uses persona f
> L30: Council is a structured prompting framework that decomposes a single language model's reasoning into multiple const

## 星数曲线

```mermaid
xychart-beta
    title "kpt-council/council-a-crucible 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6f8d8b4d9584` · [字段定义](../../DATASET.md)*
