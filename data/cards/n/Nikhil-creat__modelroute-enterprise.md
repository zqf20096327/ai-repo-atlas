# Nikhil-creat/modelroute-enterprise

⭐ 4 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/Nikhil-creat/modelroute-enterprise) · [官网](https://nikhil-creat.github.io/modelroute-enterprise/) · 个人维护

**多模态工单路由平台：本地 LLM+CNN，低置信回退前沿模型**

面向客服工单的多模态路由项目：4-bit QLoRA 微调的本地 LLM 处理工单文本，PyTorch CNN 处理图片附件，结合混合 RAG（dense+BM25）与 agent 工作流（ReAct 循环、SLA 查询工具）；按文本/视觉/RAG 三路置信度加权判定，低于阈值时才回退到 GPT-4o/Claude/Groq。提供合成数据生成、训练、阈值校准、基准评测与 FastAPI 服务脚本，附 docker compose 部署（api/chroma/vllm 服务）。README 提示标签来自规则生成的合成数据，生产使用前需用真实工单重训。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 置信度路由：三路置信加权，低于阈值回退 GPT-4o/Claude 3.5 Sonnet/Groq
- QLoRA 微调 Llama-3/Qwen2.5，FP16 合并后由 vLLM 服务
- 确定性 ReAct agent：CNN→RAG→LLM→SLA 查询
- 基准评测脚本输出带实测数字的报告与成本对比

## 适用场景

- 客服工单的意图/优先级/部门自动分派
- 带图片附件的工单诊断与知识库检索
- 搭建本地优先、前沿模型兜底的降本路由管线

## 场景标签

`RAG` `多模态` `微调` `推理引擎` · 领域:知识与检索

## 证据(README 行号)

> L5: Multimodal support-ticket platform: a 4-bit **QLoRA** fine-tuned LLM, a PyTorch **CNN** for attachments, an **agenti
> L9:               -> C_total = w1*C_text + w2*C_vision + w3*C_rag -> C >= tau ? local : frontier

## 星数曲线

```mermaid
xychart-beta
    title "Nikhil-creat/modelroute-enterprise 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-10-24 4 → 2026-11-26 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f3d3c2b7bed4` · [字段定义](../../DATASET.md)*
