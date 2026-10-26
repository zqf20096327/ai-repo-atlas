# loretoparisi/hf-experiments

⭐ 48 · Python · MIT · 推送 2026-04-18 · [GitHub](https://github.com/loretoparisi/hf-experiments) · 个人维护

**基于 Hugging Face 模型的机器学习实验合集，一键脚本运行**

个人维护的机器学习实验集合：封装 GPT-J/GPT-Neo、BERT、HuBERT、Whisper、ViT、ColBERT 等约 30 个基于 Hugging Face transformers 的模型实验，覆盖文本生成、问答、摘要、翻译、情感与情绪检测、语音识别、音频分割、图像分类、NER 等任务，另含若干不在 HF Hub 上的模型（YamNet、Projected GAN、AlphaTensor 等）。通过 build.sh/run.sh 脚本在容器环境构建与运行，支持 GPU/CPU 切换，模型文件缓存目录可由 cache_dir 环境变量指定，部分实验需手动下载额外模型文件。

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

- 约 30 个封装好的模型实验，覆盖 NLP/语音/视觉多任务
- build.sh/run.sh 脚本化构建与运行，支持 gpu|cpu 参数
- cache_dir 环境变量指定模型缓存目录
- 实验级依赖独立声明（如 src/asr/requirements.txt）

## 适用场景

- 快速试用 GPT-J、Whisper 等 HF 模型的各类推理任务
- 在 GPU 或 CPU 环境复现模型实验
- 参考不同任务（ASR、NER、语义检索）的模型调用代码

## 场景标签

`语音识别` `语义搜索` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L2: Machine Learning (cool) Experiments 🔬 🤗 with Hugging Face's (HF) transformers
> L10: The following experiments available through HF models are supported:
> L22: - asr - automatic speech recognition

## 星数曲线

```mermaid
xychart-beta
    title "loretoparisi/hf-experiments 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-26 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `fc2c192fc5c5` · [字段定义](../../DATASET.md)*
