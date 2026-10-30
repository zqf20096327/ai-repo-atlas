# UCSD-E4E/PyHa

⭐ 23 · Jupyter Notebook · NOASSERTION · 推送 2026-02-09 · [GitHub](https://github.com/UCSD-E4E/PyHa) · 组织维护

**将音频弱标签转为逐时刻强标签的生物声学标注工具**

由 UCSD Engineers for Exploration 声学物种识别团队与 San Diego Zoo Wildlife Alliance 合作维护的 Python 包，把音频片段的"弱"标签转换为逐时刻的"强"标签，并提供将自动标签与人工标签对比的流水线。标签隔离方法包括 DSP 前景-背景分离、互相关模板匹配，以及基于 BirdNET-Lite、Microfaune、TweetyNET 模型输出的 Simple/Stack/Steinberg/Chunk 等技术；通过 isolation_parameters 字典配置。概念验证基于鸟鸣音频，安装走 git clone + venv + poetry 流程。

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

- 支持 BirdNET-Lite、Microfaune、TweetyNET 三种模型的标签隔离
- 提供前景-背景 DSP 分离与互相关模板匹配等非模型方法
- 阈值判定支持 median/mean/average/standard deviation/pure 多种类型
- annotation_chunker 将标注转换为统一时长分块并可与人工标签对比

## 适用场景

- 将鸟类音频的整段弱标签细化为逐时刻出现标签
- 对比自动标注与人工标注的一致性
- 批量为声学监测数据生成带置信度的自动标注

## 场景标签

 · 领域:生物声学/生态监测

## 证据(README 行号)

> L5: A tool designed to convert audio-based "weak" labels to "strong" moment-to-moment labels. Provides a pipeline to com
> L41: The `isolation_parameters` dictionary definition depends on the model used. The currently supported models are Bird

## 星数曲线

```mermaid
xychart-beta
    title "UCSD-E4E/PyHa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4a2872791cce` · [字段定义](../../DATASET.md)*
