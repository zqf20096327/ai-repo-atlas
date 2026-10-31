# stdlogits/drowse

⭐ 14 · Python · AGPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/stdlogits/drowse) · [官网](https://drowse.ai) · 组织维护

**LLM 机制可解释性工作台：激活转向、概念探针与监控**

面向大语言模型机制可解释性的本地工作台，提供 WebUI 仪表盘、Python API 与 HTTP 服务器。通过基线提示提取隐状态并拟合概念流形/子空间，默认附带 17 对概念探针，支持激活转向表达式（可限定 token 阶段、探针门控）、token 级检查（几何/logits/SAE/J-lens）、SAE 训练或加载 SAELens 发布。服务器暴露 OpenAI 与 Ollama 兼容 API 及原生 API。需 Python 3.11+ 与 PyTorch，交互使用建议 CUDA 或 Apple Silicon MPS；定位为可信本机/实验室网络环境，非多租户推理服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 概念以流形/子空间形式提取，默认附带 17 对概念探针
- 统一转向表达式可用于 WebUI、Python、YAML、OpenAI/Ollama API
- 服务器同时暴露 OpenAI 兼容、Ollama 兼容与原生三类 API
- 支持 SAE 训练/加载与 Jacobian lens 拟合

## 适用场景

- 研究 LLM 内部表示并对特定概念做激活转向
- 在对话界面中逐 token 查看探针分数与 logprob
- 通过 OpenAI/Ollama 兼容接口做带转向参数的本地推理

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: Drowse is a local workbench for mechanistic interpretability on large language
> L8: models.
> L10: It comes with a local dashboard, along with a Python API, and a server compatible


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e42de0659087` · [字段定义](../../DATASET.md)*
