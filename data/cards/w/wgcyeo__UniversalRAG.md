# wgcyeo/UniversalRAG

⭐ 177 · Python · Apache-2.0 · 推送 2026-06-24 · [GitHub](https://github.com/wgcyeo/UniversalRAG) · [官网](https://universalrag.github.io) · 组织维护

**跨模态多粒度检索的 any-to-any RAG 研究框架**

ACL 2026 论文配套的开源 RAG 框架：通过模态感知路由机制，为每个查询动态选择最合适的模态专用语料库进行检索，处理多模态与固定粒度检索的限制。提供数据集下载预处理、语料嵌入提取、路由器训练（Qwen3-VL-2B、InternVL3.5-1B、T5Gemma 270M）与免训练路由（GPT-5）、评测脚本四阶段流程。使用 uv 管理依赖，需要 Python 3.12+，嵌入提取与评测依赖 GPU（CUDA）。面向科研复现与多模态 RAG 实验场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模态感知路由：按查询动态选择模态专用语料库
- 支持训练式路由器（Qwen3-VL-2B/InternVL3.5-1B/T5Gemma-270M）与免训练路由（GPT-5）
- 提供数据预处理、嵌入提取、路由、评测的完整脚本流程
- 多 GPU 嵌入提取支持（CUDA_DEVICES 配置）

## 适用场景

- 复现论文中的多模态 RAG 实验
- 在多模态语料上做跨模态检索增强生成评测
- 训练或比较不同路由器模型

## 场景标签

 · 领域:多模态 RAG/研究

## 证据(README 行号)

> L7: **UniversalRAG** is a novel any-to-any RAG framework that retrieves across multiple modalities and granularities by 
> L64: To generate results for routed queries, run the following script:

## 星数曲线

```mermaid
xychart-beta
    title "wgcyeo/UniversalRAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 176 --> 178
    line [177, 177]
```

2026-10-18 177 → 2026-10-24 177（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6c0a49a3a956` · [字段定义](../../DATASET.md)*
