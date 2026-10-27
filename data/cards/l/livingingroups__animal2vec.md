# livingingroups/animal2vec

⭐ 34 · Python · MIT · 推送 2025-12-15 · [GitHub](https://github.com/livingingroups/animal2vec) · 组织维护

**面向稀有动物发声事件的自监督 transformer 模型与数据集**

动物叫声音频分析的自监督 transformer 模型实现：先在无标注音频上预训练，再用少量标注数据微调，可在稀疏不平衡的生物声学数据上做发声事件检测；配套发布 MeerKAT 猫鼬发声标注数据集（1068 小时、59 GB）。基于 fairseq 框架构建，提供预处理脚本、预训练/微调/推理命令与模型权重下载；限制为仅支持 Python 3.6–3.9（3.10 不可用），Docker 镜像与 HuggingFace Transformers 权重尚在准备中。面向生物声学与生态学研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对稀疏不平衡音频的自监督预训练+微调训练方案
- 发布 MeerKAT 数据集：1068 小时猫鼬发声音频，184 小时毫秒级标注
- 提供预处理、manifest 生成、预训练/微调/推理全流程脚本与模型权重
- 基于 fairseq 框架，可加载 .pt checkpoint 做自有数据推理

## 适用场景

- 对野外录制的动物发声音频做自动检测与分类
- 用自己的无标注/少量标注音频做声学预训练与微调
- 获取大规模非人哺乳动物标注声学数据集用于研究

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L13: Bioacoustic research, vital for understanding animal behavior, conservation, and ecology, faces a monumental challe
> L90: ```python animal2vec_inference.py --path=/path/to/audio_data --out-path=/path/to/desired/output_folder --model-path

## 星数曲线

```mermaid
xychart-beta
    title "livingingroups/animal2vec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fc16ff0806bd` · [字段定义](../../DATASET.md)*
