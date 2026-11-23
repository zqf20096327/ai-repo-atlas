# strands-labs/strands-decider

⭐ 1,253 · Python · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/strands-labs/strands-decider) · [官网](https://strandsagents.com/docs/labs/) · 组织维护

**给 agentic 工作流的快速决策模型：选项判定与打分**

Strands Decider 是一个决策模型（自称 system one 模型）：在预训练 LLM 主干上丢弃语言建模头，换成约百万参数的指针头，单次前向即可从选项中挑选或按量表打分，不做文本生成。提供三种问题类型（noul 是/否、choice 多选一、score 有序评分），每次决策附带校准置信度。以 CLI 和 HTTP 服务器形式提供，基于 Qwen3.5 与 Gemma 4 基座，支持 CPU、CUDA、MPS、MLX 设备，模型权重发布在 Hugging Face。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单次前向输出的指针头架构，不做生成与解码循环
- 三种问题类型：choice/noul/score，附带校准置信度
- 以 CLI 与 HTTP 服务器形式提供，支持 --vision 图像输入
- 提供 2B 至 26B-A4B 多个尺寸，全部可在 CPU 运行

## 适用场景

- 在 agent 工作流中做路由决策（如按工单内容选择处理团队）
- 对文本做快速情感/紧急度打分
- 对文档图像做是/否判断（如签名栏是否填写）

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L20: Strands decider is one of a new class of **decision models**, or "system one" models. Unlike an
> L23: and traditional classification models: it is a general-purpose classification and scoring
> L26: agentic workflows built with the Strands Agents SDK.

## 星数曲线

```mermaid
xychart-beta
    title "strands-labs/strands-decider 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 617 --> 1310
    line [674, 686, 692, 699, 703, 708, 712, 720, 730, 741, 743, 744, 745, 703, 768, 977, 1099, 1154, 1172, 1183, 1197, 1207, 1218, 1225, 1233, 1239, 1243, 1253]
```

2026-10-21 674 → 2026-11-23 1,253（+579）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `cb86d5d3f95c` · [字段定义](../../DATASET.md)*
