# ray-project/multimodal-training

⭐ 34 · Python · Apache-2.0 · 推送 2026-01-24 · [GitHub](https://github.com/ray-project/multimodal-training) · 组织维护

**基于 Ray 的视觉-语言模型训练框架：组件级混合并行**

面向研究者的视觉-语言模型（VLM）分布式训练框架，实现解耦混合并行（DHP）：视觉编码器用序列并行（SP）+ZeRO1，文本解码器用张量并行（TP），各组件独立选择并行策略。基于 Ray 的多 SPMD ActorGroup 编排，支持 GPU 共置与 ObjectRefs 跨组件数据传输。提供 LLaVA 风格数据格式、YAML 配置与检查点保存，附 Qwen2.5-VL 32B 在 8×H100 上的吞吐对比实验。已验证环境为 Python 3.12、CUDA 12.6、A100/H100。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视觉编码器 SP+ZeRO1、文本解码器 TP 的组件级独立并行
- Ray ActorGroup 支持多个独立 SPMD 组与 GPU 共置
- LLaVA 风格标注数据格式，支持 JSON/JSONL
- YAML 配置驱动，按 epoch 保存检查点

## 适用场景

- 在多 GPU 上训练 Qwen2.5-VL 等视觉-语言模型
- 长序列（最高 65k tokens）高分辨率图像训练避免 OOM
- 研究异构组件采用不同并行策略的分布式训练

## 场景标签

`模型训练` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: A framework for training vision-language models using disaggregated hybrid parallelism, where each model component a
> L41: This repository implements **disaggregated hybrid parallelism (DHP)** using Ray, allowing each model component to a

## 星数曲线

```mermaid
xychart-beta
    title "ray-project/multimodal-training 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-31 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `cef6297ce682` · [字段定义](../../DATASET.md)*
