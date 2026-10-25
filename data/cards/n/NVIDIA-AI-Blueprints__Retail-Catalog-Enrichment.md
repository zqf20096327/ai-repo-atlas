# NVIDIA-AI-Blueprints/Retail-Catalog-Enrichment

⭐ 45 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/NVIDIA-AI-Blueprints/Retail-Catalog-Enrichment) · 组织维护

**面向零售商的商品图片目录自动富化系统（NVIDIA 蓝图）**

NVIDIA AI Blueprints 下的零售目录富化参考实现：以商品图片为输入，用 Nemotron 3 Nano Omni 做多模态商品理解、Nemotron 3.5 Lightning 做提示规划、FLUX 生成多语言文化背景商品图、TRELLIS 生成 3D GLB 模型，并支持 FAQ 生成、基于 RAG+Milvus 的政策合规检查、Exa 网络洞察与 ACP/UCP 协议导出。后端 FastAPI、前端 Next.js，以 Docker Compose 与 NVIDIA NIM 容器部署，本地自托管需 3×H100+1×L40S 级 GPU；无应用层鉴权，属参考蓝图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模态 VLM 商品分析与自动分类，10 个区域语言生成标题描述
- FLUX 生成文化适配商品背景图，TRELLIS 生成 3D GLB 模型
- RAG+Milvus 政策 PDF 合规检查与商品 FAQ 生成
- 导出 ACP/UCP 协议合规的商品数据 schema

## 适用场景

- 电商批量把基础商品图变成含标题、描述、FAQ 的完整目录条目
- 为不同地区市场生成文化适配的商品图与多语言文案
- 检查商品上架信息是否符合上传的政策文档

## 场景标签

`AI 写作` `图像生成` `文档问答` · 领域:内容生成

## 证据(README 行号)

> L5: A GenAI-powered catalog enrichment system that transforms basic product images into comprehensive, rich catalog entr
> L17: - **AI-Powered Analysis**: NVIDIA Nemotron 3 Nano Omni for intelligent omni-modal product understanding
> L24: - **Product FAQ Generation**: Automatically generate product FAQs from enriched catalog data, with optional product

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-AI-Blueprints/Retail-Catalog-Enrichment 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `93a58c801e62` · [字段定义](../../DATASET.md)*
