# NVIDIA/logits-processor-zoo

⭐ 391 · Python · Apache-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/NVIDIA/logits-processor-zoo) · 组织维护

**NVIDIA 出品的 LLM logits 处理器集合，定制生成行为**

面向 LLM 开发者的 LogitsProcessor 工具库：提供调节回答长度、强制引用提示词内容、强制收尾短语、多选题作答、触发短语、幻觉回退、生成限时等处理器，通过干预 logits 实现对输出的细粒度控制。支持 transformers、vLLM、TensorRT-LLM（>=0.20.0）三种框架，vLLM HTTP API 场景下 tokenizer 仅从本地文件加载并需环境变量白名单许可。以 PyPI 包形式分发，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 类 LogitsProcessor 覆盖长度控制、引用增强、幻觉缓解、限时等任务
- 支持 transformers、vLLM、TensorRT-LLM 三种推理框架
- vLLM serve 场景提供 tokenizer 白名单安全机制

## 适用场景

- 强制模型以固定短语收尾或输出引用信息
- 限制模型生成时长或回答长度
- 降低幻觉输出，置信度低时回退到预设短语

## 场景标签

 · 领域:LLM 基础设施/推理控制

## 证据(README 行号)

> L14: ## Supported Frameworks
> L16: * vLLM

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/logits-processor-zoo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 389 --> 392
    line [390, 391, 391]
```

2026-10-18 390 → 2026-10-27 391（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4e4004e52ca2` · [字段定义](../../DATASET.md)*
