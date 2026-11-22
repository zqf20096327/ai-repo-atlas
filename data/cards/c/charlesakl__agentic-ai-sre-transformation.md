# charlesakl/agentic-ai-sre-transformation

⭐ 4 · Python · 推送 2026-11-02 · [GitHub](https://github.com/charlesakl/agentic-ai-sre-transformation) · [官网](https://agentic-ai-sre-transformation.streamlit.app/) · 个人维护

**面向 SRE 的 Agentic AI 运维转型演示应用**

基于 Streamlit 的演示应用，用 LangGraph 工作流串联 LangChain 与 OpenAI 推理、Chroma 向量检索，展示 AIOps 异常检测、RAG 事件调查、根因分析与带审批门的治理式修复提案。所有事件数据、运行手册与生产集成为合成模拟，不连接真实可观测性系统，不执行生产变更；LLM 输出仅为假设而非经验证的 RCA。面向 SRE 与决策者作转型演示，含 ROI 模型页。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 六阶段工作流：Observe/Detect/Retrieve/Reason/Govern 等可逐步查看执行轨迹
- RAG 检索：OpenAI embeddings + Chroma 本地向量索引检索八份合成知识文档并附引用
- 治理式修复演示：合成变更单、策略评估与需勾选的审批门，不调用外部 API
- P95 统计异常检测器基于 90 天合成 OpenShift 数据，独立于 LangGraph 规则

## 适用场景

- 向管理层演示 agentic AI 在事件响应中的转型路径
- 展示 RAG + LangGraph 在 SRE 根因分析中的工作方式
- 讲解治理式自动化修复的审批与安全门设计

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: Complete Streamlit application with **LangGraph workflow**, **LangChain model and retriever**, **Chroma vector datab
> L23: In **Agent Investigation**, choose **Payment API latency**, enable live OpenAI, and run. The **Retrieve** stage cal

## 星数曲线

```mermaid
xychart-beta
    title "charlesakl/agentic-ai-sre-transformation 星数(近 2 点)"
    x-axis ["2026-11-11", "2026-11-22"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-11 4 → 2026-11-22 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9a761e87ae8d` · [字段定义](../../DATASET.md)*
