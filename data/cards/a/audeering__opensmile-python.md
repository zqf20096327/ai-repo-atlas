# audeering/opensmile-python

⭐ 336 · BitBake · NOASSERTION · 推送 2026-09-15 · [GitHub](https://github.com/audeering/opensmile-python) · [官网](https://audeering.github.io/opensmile-python/) · 组织维护

**openSMILE 音频特征提取工具的 Python 接口，面向语音研究**

对 openSMILE 音频特征提取器的 Python 封装，供研究者在 Python 中提取声学特征。支持 ComParE 2016、GeMAPS、eGeMAPS 三个标准特征集及其多个版本变体，特征可在低层描述子（LLD）与统计泛函（Functionals）两级提取，ComParE 2016 额外支持 LLD deltas，ComParE 2016 泛函层产出 6373 维特征。仅支持 64 位 Python，以 pip 安装。注意 openSMILE 采用双许可模式：开源许可仅限私人、研究与教育用途，商业产品需购买商业开发许可。

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

- 支持 ComParE 2016 / GeMAPS / eGeMAPS 标准特征集及多版本变体
- LLD 与 Functionals 两级特征提取，ComParE 2016 另支持 LLD deltas
- ComParE 2016 泛函层提取 6373 维声学特征
- 社区贡献的额外特征集可通过 opensmile.FeatureSet 文档查看

## 适用场景

- 语音情感识别研究中提取声学特征
- 音频机器学习流水线中生成 GeMAPS/eGeMAPS 特征
- 按 ComParE 2016 基准复现声学场景实验

## 场景标签

 · 领域:音频信号处理/语音研究

## 证据(README 行号)

> L5: Python interface for extracting openSMILE_ features.
> L107: Please cite openSMILE in your publications by citing the following paper:

## 星数曲线

```mermaid
xychart-beta
    title "audeering/opensmile-python 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 334 --> 337
    line [335, 336, 336]
```

2026-10-18 335 → 2026-10-27 336（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `40d1abaab1b2` · [字段定义](../../DATASET.md)*
