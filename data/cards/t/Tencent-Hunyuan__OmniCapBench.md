# Tencent-Hunyuan/OmniCapBench

⭐ 10 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/Tencent-Hunyuan/OmniCapBench) · [官网](https://01yzzyu.github.io/OmniCapBench/) · 组织维护 · 中文 README

**音视频细粒度描述评测基准与配套标注/评分工具包**

将音视频描述（captioning）评测重构为深度结构化诊断任务：把评分目标拆解为实体引用、视觉镜头、音频事件三类原子可验证单元，先由规则做确定性校验与时间对齐，再由 LLM judge 只做单字段局部语义比对，各分数可追溯到具体单元。仓库提供生成标注的流水线（generate→evaluate→refine→select）与评分工具包，数据为 786 段视频、5,818 条引用、11,419 个镜头与 6,537 个音频事件，已在 NeurIPS 2026 Evaluations & Datasets Track 发表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三轨评测单元（references/shots/events）+ 双向 recall/precision 打分
- 规则校验与 LLM 局部比对分离，分数不随 judge 强度波动
- 标注流水线支持断点续跑、分层采样与多机分片
- 支持 OpenAI 兼容端点作为 judge（OpenRouter/DashScope/自托管 vLLM）

## 适用场景

- 在自有视频集上按同一协议复现结构化标注与评分
- 评测 omnimodal MLLM 的音视频描述输出并定位具体失败类型
- 离线验证安装：运行样例指标检查环境

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L18: **OmniCapBench** reframes audio–visual caption evaluation as a *deep-structured diagnostic* task. Instead of scorin
> L29: The paper applies this framework to 786 densely annotated videos (12.8 hours, 20 level-1 and 125 level-2 categories
> L11: - **[2026/09]** 🎉 **OmniCapBench** was accepted to **NeurIPS 2026** (Evaluations & Datasets Track).

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/OmniCapBench 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-08 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `946607830482` · [字段定义](../../DATASET.md)*
