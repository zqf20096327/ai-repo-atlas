# dwyl/image-classifier

⭐ 35 · Jupyter Notebook · GPL-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/dwyl/image-classifier) · 组织维护

**Elixir/Phoenix 图像描述与语义搜索的分步教程**

面向 Phoenix 初学者的教程仓库，逐步构建一个支持图片上传与 AI 图像描述（captioning）的 Phoenix LiveView 应用，并把描述编码为向量做 kNN 近似最近邻语义搜索，支持录制语音描述、转写为文本后再语义查询。使用 Bumblebee 集成 Hugging Face 预训练模型（BLIP 图像描述、whisper-small 语音识别、sentence-transformers 嵌入、ResNet-50 分类），依赖 Nx/EXLA 在 CPU 或 GPU 上运行。要求读者已安装 Elixir 与 Phoenix，并具备 AWS S3 的基础知识。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分步构建支持图片上传与 AI 描述的 Phoenix LiveView 应用
- BLIP 图像描述 + whisper-small 语音转写 + 嵌入模型语义搜索
- 通过 Nx.Serving 做请求批处理，模型可在 CPU/GPU 运行
- 全程离线，不依赖第三方 API/服务

## 适用场景

- 我想学习如何在 Elixir/Phoenix 中运行图像描述模型
- 我想给上传的图片自动生成可搜索的描述与元标签
- 我想学习用嵌入向量做图片的语义/语音搜索

## 场景标签

`教程课程` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L30: A step-by-step tutorial building a fully functional
> L55: This tutorial is aimed at `Phoenix` beginners
> L58: We propose to use pre-trained models from Hugging Face via `Bumblebee`

## 星数曲线

```mermaid
xychart-beta
    title "dwyl/image-classifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `396b8c78d279` · [字段定义](../../DATASET.md)*
