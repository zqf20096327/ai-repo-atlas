# xi029/Qwen3-VL-MoeLORA

⭐ 60 · Python · Apache-2.0 · 推送 2025-12-14 · [GitHub](https://github.com/xi029/Qwen3-VL-MoeLORA) · 个人维护 · 中文 README

**Qwen3-VL 多模态模型 LoRA/MoeLoRA 微调与多智能体部署工程**

面向 Qwen3-VL-4B-Instruct 的微调与部署全链路工程：提供 COCO Caption 数据下载与格式转换脚本、LoRA/MoeLoRA/MoTLoRA/IA3 多种微调实现、test.py 推理验证，以及基于 LangChain + RAG + PyQt5 的多智能体桌面助手（Planner/Manager/Knowledge/Responder/Reviewer 五角色）。训练默认 4-bit NF4 量化，README 记录单卡 8G 可完成微调，训练全程用 SwanLab 可视化。仓库不含基座权重与数据集，需自行下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LoRA / MoeLoRA / MoTLoRA / IA3 多种微调方法实现与训练对比记录
- BM25 + FAISS 混合召回 + Cross-Encoder 重排序的 Advanced RAG
- 五角色多智能体（Planner/Manager/Knowledge/Responder/Reviewer）+ Reviewer 自检重写
- 默认 4-bit NF4 量化，单卡 8G 显存可跑完微调流程

## 适用场景

- 对 Qwen3-VL 多模态模型做参数高效微调并对比不同 LoRA 变体效果
- 搭建本地知识库图文问答桌面助手
- 用 COCO Caption 数据复现数据→训练→推理→部署流程

## 场景标签

`微调` `RAG` `多智能体` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L3: > 在千问最新的多模态 image-text 模型 **Qwen3-VL-4B-Instruct** 上改进设计 MOELoRA\MOTLoRA（混合专家\token LoRA）微调，同时打通 COCO 2014 数据处理、Swan
> L24: 1. **数据 → 训练 → 推理全链路脚本齐全**：`download_data2csv.py` 负责拉取 & 清洗 COCO Caption，`csv2json.py` 适配 Qwen3-VL 格式，`MoeLORA.py/ 
> L94: python test.py --model ./qwen3-vl-4b-instruct --image ./image/demo.jpg --prompt "描述这张图片"

## 星数曲线

```mermaid
xychart-beta
    title "xi029/Qwen3-VL-MoeLORA 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 59 --> 62
    line [61, 60, 60]
```

2026-10-18 61 → 2026-10-26 60（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `d00d3b17286d` · [字段定义](../../DATASET.md)*
