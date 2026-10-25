# flashserve/RAGPulse

⭐ 40 · Python · MIT · 推送 2026-09-01 · [GitHub](https://github.com/flashserve/RAGPulse) · [官网](https://arxiv.org/abs/2511.12979) · 组织维护

**真实校园问答服务的 RAG 负载轨迹数据集（3.5 万条）**

来自一所大学全校问答服务（2024 年 4 月起服务 4 万+师生）的真实 RAG 工作负载数据集：完整数据 13.4 万条，当前发布六周采样共 34,987 条。文本内容以重映射 hash ID 替换以保护隐私，轨迹记录时间戳、输入/输出 token 长度、会话 ID 及系统提示、检索段落、聊天历史、网页搜索等各组件的 hash 标识。提供基于 vLLM 的回放脚本，输出 TTFT/TPOT 等指标，可用于 RAG 服务系统的调度、缓存与性能研究。后续将补充执行耗时、内部 LLM 请求日志与 agent 工作流轨迹。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 34,987 条来自真实校园问答服务的 RAG 请求轨迹（完整集 134K）
- 文本以重映射 hash ID 匿名化，保留各输入组件结构
- 提供 vLLM 回放脚本，记录 TTFT/TPOT 等服务指标
- 覆盖系统提示、检索段落、聊天历史、网页搜索等组件的 token 长度信息

## 适用场景

- 评估 RAG 服务系统的延迟分解与调度缓存策略
- 构建贴近真实部署的 RAG 负载模拟器或基准
- 研究检索深度与服务成本/质量的权衡

## 场景标签

 · 领域:LLM/RAG 系统研究

## 证据(README 行号)

> L7: RAGPulse is a real-world RAG workload trace collected from an university-wide Q&A service scenario. The system has b
> L17: - `0_trace.jsonl` contains the key information of our trace. Totally 34,987 lines.

## 星数曲线

```mermaid
xychart-beta
    title "flashserve/RAGPulse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c8af92366203` · [字段定义](../../DATASET.md)*
