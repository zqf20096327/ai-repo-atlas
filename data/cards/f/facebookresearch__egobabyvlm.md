# facebookresearch/egobabyvlm

⭐ 20 · Python · NOASSERTION · 推送 2026-06-23 · [GitHub](https://github.com/facebookresearch/egobabyvlm) · [官网](https://facebookresearch.github.io/egobabyvlm/) · 组织维护

**基于儿童第一视角视频的跨模态学习基准与训练评测基础设施**

Meta FAIR 等机构随论文发布的挑战赛基础设施：要求参赛者仅用 BabyView 2025.1（约 863 小时头戴相机儿童视频）训练 VLM，在视觉、语言、跨模态 grounding 三类任务上评测并与排行榜对比。仓库提供 DINOv2、BERT/GPT-2、CLIP+、LLaVA 四种参考基线训练器，数据预处理管线（抽帧+WhisperX 转写），以及可通过实现协议接入自定义模型的评测启动器。环境用 Pixi 锁定（Python 3.12、PyTorch 2.8 + CUDA 12.6），代码以 CC BY-NC 4.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三类评测任务族（视觉/语言/跨模态 grounding，含 Machine-DevBench）
- 四个参考基线训练器：DINOv2、BERT/GPT-2、CLIP+（四模式）、LLaVA 式生成 VLM
- 协议化的模型接入：实现 ImageFeatureExtractor 等协议即可被 eval_launcher 调度
- 视频→帧+WhisperX 转写→(帧,话语) manifest 的数据预处理管线

## 适用场景

- 参加仅用 BabyView 数据训练 VLM 的挑战赛并提交排行榜成绩
- 在自然第一视角视频上复现论文基线或开发自己的训练方法
- 为新的训练语料生成跨模态评测基准

## 场景标签

`模型评测` `多模态` `模型训练` · 领域:评测与运维

## 证据(README 行号)

> L16: Challenge infrastructure accompanying the paper
> L31: Submissions are scored on three families of tasks, each with subgroup
> L120: **Plugging in an alternative architecture.** The eval launcher

## 星数曲线

```mermaid
xychart-beta
    title "facebookresearch/egobabyvlm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ed54842ed396` · [字段定义](../../DATASET.md)*
