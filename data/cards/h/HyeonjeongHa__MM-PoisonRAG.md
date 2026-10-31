# HyeonjeongHa/MM-PoisonRAG

⭐ 20 · Python · 推送 2025-12-04 · [GitHub](https://github.com/HyeonjeongHa/MM-PoisonRAG) · 个人维护

**针对多模态 RAG 的知识投毒攻击框架官方实现**

论文 MM-PoisonRAG 的官方 PyTorch 实现，面向 AI 安全研究人员：提供局部投毒攻击 LPA（针对特定查询注入文本与图像误导信息）与全局投毒攻击 GPA（干扰 MLLM 生成使所有查询输出失效）两种策略，在 MultiModalQA 与 WebQA 基准上评估检索召回与投毒前后准确率。环境依赖 Python 3.10、requirements.txt 与 LLaVA 配置流程，GPA-RtRrGen 需至少 3 块 GPU，支持 llava/qwen 作为重排与生成模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LPA 与 GPA 两类投毒攻击策略（LPA-BB/LPA-Rt/GPA-Rt/GPA-RtRrGen）
- 在 MultiModalQA 与 WebQA 上评估检索召回与攻击前后准确率
- 支持 llava/qwen 重排与生成模型切换及跨检索器迁移性评估

## 适用场景

- 复现论文中的多模态 RAG 投毒攻击实验
- 研究 RAG 外部知识库的安全性与投毒防御
- 评估不同检索/重排设置下攻击的成功率

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: This is the official PyTorch implementation for the paper ***MM-PoisonRAG: Disrupting Multimodal RAG with Local and 
> L12: To expose such vulnerabilities in multimodal RAG, we propose MM-PoisonRAG, a novel knowledge poisoning attack frame

## 星数曲线

```mermaid
xychart-beta
    title "HyeonjeongHa/MM-PoisonRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3af0001b2b01` · [字段定义](../../DATASET.md)*
