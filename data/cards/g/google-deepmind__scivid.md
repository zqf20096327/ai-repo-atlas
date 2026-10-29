# google-deepmind/scivid

⭐ 18 · Python · Apache-2.0 · 推送 2026-03-02 · [GitHub](https://github.com/google-deepmind/scivid) · 组织维护

**科研视频基础模型评测基准：五项跨领域视频任务**

Google DeepMind 发布的 ViFM（视频基础模型）评测基准：覆盖 FlyVsFly 果蝇行为分类、CalMS21 小鼠行为分类、WeatherBench 2 天气预报、Digital Typhoon 台风中心气压预测、STIR 手术组织点跟踪共五项任务。评测时在预训练 backbone 上附加任务专属 readout，支持冻结或微调 backbone；提供 Hugging Face VideoMAE-B 与 Scaling4D 等配置，并附 Colab 演示。安装基于 conda 环境与 JAX/kauldron 生态，测试环境为 CUDA 12.4 与 Python 3.10，数据从 Google Cloud Storage 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个科学视频任务（行为分类/天气预报/气压预测/点跟踪）
- 冻结或微调 backbone 的 readout 评测机制
- 支持 Hugging Face VideoMAE-B 与 Scaling4D 预训练模型
- 提供 Colab 演示 notebook

## 适用场景

- 评估视频基础模型在科学领域的迁移能力
- 在自己的视频 backbone 上跑跨领域基准测试
- 复现论文中各 ViFM 的基线结果

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L5: benchmark for evaluating Video Foundation Models (ViFMs) across multiple
> L12: * Instructions to evaluate pretrained video models on SciVid (eg. Hugging Face VideoMAE-B backbone), easily extensi
> L37: In our paper, we evaluate the capabilities

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/scivid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c6e3fd30f866` · [字段定义](../../DATASET.md)*
