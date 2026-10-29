# SalesforceAIResearch/CoDA

⭐ 68 · Python · Apache-2.0 · 推送 2026-06-02 · [GitHub](https://github.com/SalesforceAIResearch/CoDA) · 组织维护

**Salesforce 开源扩散语言模型，面向代码生成全流程**

CoDA 是 Salesforce AI Research 开源的扩散（diffusion）语言模型仓库，覆盖 TPU 预训练、GPU 监督微调（基于 LLaMA-Factory 扩散训练器）、评测框架（HumanEval/MBPP/EvalPlus）与 FastAPI 推理服务后端。提供 CoDA-Base 与 CoDA-Instruct 检查点，支持 HuggingFace 模型类加载与转换，通过环境变量配置生成长度、温度、扩散步数等参数。仓库声明仅供研究用途，数据发布受内部规定约束。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预训练→微调→评测→服务的端到端训练管线
- TPU 预训练与 GPU 扩散微调（SFT）流水线
- FastAPI 服务后端与流式 CLI 交互
- HuggingFace 模型类与检查点转换工具

## 适用场景

- 研究扩散语言建模的预训练与后训练方法
- 复现代码生成基准（HumanEval/MBPP/EvalPlus）评测
- 本地部署 CoDA 模型提供代码生成 API 服务

## 场景标签

`代码生成` `模型训练` `微调` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L5: > End-to-end diffusion language modeling across TPU pre-training, GPU fine-tuning, evaluation, and serving.
> L12: CoDA is Salesforce AI Research's open diffusion language model. This repo contains a unified training pipeline from

## 星数曲线

```mermaid
xychart-beta
    title "SalesforceAIResearch/CoDA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-29 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b610d17ecfbb` · [字段定义](../../DATASET.md)*
