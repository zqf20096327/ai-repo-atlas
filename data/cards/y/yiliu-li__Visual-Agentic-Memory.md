# yiliu-li/Visual-Agentic-Memory

⭐ 18 · Python · MIT · 推送 2026-08-07 · [GitHub](https://github.com/yiliu-li/Visual-Agentic-Memory) · 个人维护 · 中文 README

**长视频在线理解框架：流式索引构建层级记忆并支持代理式检索**

论文官方实现：将无约束视频流转式索引为持久化的层级视觉记忆（边界敏感切分、自适应去重），由 MLLM 作为检索代理进行多轮搜索、检视与总结，对远距离事件给出有据回答；整体训练无关，使用预训练多模态组件。面向长视频问答与事件定位场景的研究者/开发者。提供 TUI 终端界面与可选 FastAPI/WebSocket 服务，默认调用 SiliconFlow 的 Qwen3-VL 模型，可切换 OpenRouter；运行需 Python 3.10+ 与系统安装 FFmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在线索引+自适应去重的流式记忆构建
- 跨时间层级的记忆结构（moments/events）
- MLLM 多轮代理式检索与可审计推理，无需任务微调
- 提供 vam-tui 终端界面与 vam-server API 服务两种入口

## 适用场景

- 对长视频做事件定位与回顾式提问（如寻找某场景）
- 对已索引记忆生成指定时间段摘要
- 在证据稀疏且时间上远距的视频流中做有据问答

## 场景标签

`多模态` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Transforms unconstrained video streams into hierarchical visual memory, supports query-driven agentic retrieval, an
> L17: - **Agentic Retrieval for Grounded Reasoning**: A multi-turn retrieval loop in which an MLLM acts as a retrieval ag
> L18: - **Training-free End-to-end Framework**: An integrated system that supports streaming perception and long-horizon 

## 星数曲线

```mermaid
xychart-beta
    title "yiliu-li/Visual-Agentic-Memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `dc9e7c3b23be` · [字段定义](../../DATASET.md)*
