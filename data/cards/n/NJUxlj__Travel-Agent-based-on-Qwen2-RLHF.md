# NJUxlj/Travel-Agent-based-on-Qwen2-RLHF

⭐ 83 · Python · 推送 2026-07-06 · [GitHub](https://github.com/NJUxlj/Travel-Agent-based-on-Qwen2-RLHF) · 个人维护 · 中文 README

**基于Qwen2.5微调+RLHF+RAG的旅游路径规划智能体项目**

以Qwen2.5（1.5B已测试）为本体，结合LoRA进行SFT微调，并支持PPO/DPO/GRPO三种RLHF训练路径，使用旅游问答数据集训练，产出旅行路线规划并生成思维导图。RAG部分基于LangChain与Chroma向量库，实现MemWalker、Self-RAG与传统BM25三种检索模式，可经RAG Dispatcher切换；工具调用系统接入Google搜索、天气、酒店、机票与最短路径API，前端用Gradio。需自备GPU环境与reward model权重，README自述仍有未修复bug。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Qwen2.5 + SFT + PPO/DPO/GRPO 多种RLHF训练路径
- 三种RAG模式（MemWalker/Self-RAG/传统BM25）可调度切换
- 工具调用系统含搜索/天气/酒店/机票/最短路径API与调度器
- 路线规划结果生成思维导图，Gradio Web Demo

## 适用场景

- 学习SFT+RLHF微调与RAG的完整实现流程
- 本地运行旅游路径规划智能体并生成行程思维导图
- 对比MemWalker、Self-RAG等RAG方法的效果

## 场景标签

`RAG` `微调` `强化学习` · 领域:知识与检索

## 证据(README 行号)

> L17: - 本项目希望借助轻量级大模型`Qwen2.5-0.5B~3B`帮助用户在本地更好地规划旅行路径，提高旅行体验。本项目是基于Qwen2.5+SFT微调+RLHF+RAG的旅游路径规划智能体。
> L29: - 工具调用系统 (Google Search + Weather API + Hotel Booking API + Plane Ticket API + Shortest Path API)

## 星数曲线

```mermaid
xychart-beta
    title "NJUxlj/Travel-Agent-based-on-Qwen2-RLHF 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-30 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e372091ae05f` · [字段定义](../../DATASET.md)*
