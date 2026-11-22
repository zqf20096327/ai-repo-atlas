# 47thtechcorner/RayCodes_Qwen3.8

⭐ 10 · Python · 推送 2026-08-10 · [GitHub](https://github.com/47thtechcorner/RayCodes_Qwen3.8) · [官网](https://youtu.be/XDGWObkZN0o) · 个人维护

**本地运行的提示词优化引擎：把简单提示重构为结构化系统提示**

基于序列蒸馏的 Qwen3.8 4B GGUF 模型，在本地通过 Ollama 运行的离线提示词优化工具：输入一句话的简单提示，自动重构为包含角色定义、技术约束和输出格式规则的结构化系统提示。通过自定义系统提示抑制内部 <think> 推理标签以加快输出速度。完全离线运行、无 API 计费，Python 3.10+ 环境下执行 main.py 即可运行；无 Web 界面，需手动复制输出结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将单行输入转化为含角色、约束、输出 schema 的系统提示
- 抑制 <think> 推理标签以加速输出
- 完全离线运行，数据不上传
- 覆盖软件工程、创意写作、正则生成等多领域提示

## 适用场景

- 把模糊的代码提示升级为编码助手可用的详细规格
- 为客户支持机器人和内部 AI 工具标准化系统提示
- 在离线或隔离网络的电脑上运行提示工程工具

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: An offline, zero-cost local prompt optimization engine powered by sequence-distilled Qwen3.8 4B AI reasoning. It aut
> L28: - **Model Engine:** `Ma7ee7/Qwen3.8_4B_Distilled_GGUF:Q4_K_M`
> L30: - **Local Server:** Ollama Native HuggingFace GGUF


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `d1388aca61aa` · [字段定义](../../DATASET.md)*
