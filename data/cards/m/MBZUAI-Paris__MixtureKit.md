# MBZUAI-Paris/MixtureKit

⭐ 39 · Python · BSD-3-Clause · 推送 2026-10-15 · [GitHub](https://github.com/MBZUAI-Paris/MixtureKit) · [官网](https://mbzuai-paris.github.io/MixtureKit/) · 组织维护

**把多个微调模型组合成 MoE 模型并训练路由的框架**

面向已有基座模型及其多个微调版本的 PyTorch 框架：通过 BTX、Mixtral 式 MoE、BTS 三种方法把微调检查点合并为单一 Mixture-of-Experts 模型，训练逐 token 选择专家的路由（含负载均衡损失、可选专家 LoRA），并提供逐层逐 token 的路由可视化、基于 lm-evaluation-harness 的基准测试、Hugging Face Hub 上传与导出为原生 Mixtral/Qwen3-MoE 格式（可用于 GGUF/llama.cpp/vLLM/MLX）。合并可在笔记本上运行，路由训练需 GPU。ACL 2026 系统演示论文，BSD-3-Clause 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种合并方法（BTX/Traditional/BTS）统一于一份 YAML 配置
- 合并逐张量读写，笔记本内存即可完成
- 路由训练含负载均衡损失，可选专家 LoRA，支持单卡或多卡
- 逐层逐 token 的路由可视化（应用/HTML 页/Notebook 内嵌）

## 适用场景

- 把数学、代码、语言等多个微调模型合并成一个 MoE 模型
- 训练并观察路由器如何为每个 token 选择专家
- 导出为原生 MoE 格式后在 llama.cpp/vLLM 等运行时使用

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L17: language. MixtureKit composes them into a single Mixture-of-Experts model whose routers
> L49: * **Router training included**: `mixturekit train` trains the routers (or the BTS stitch

## 星数曲线

```mermaid
xychart-beta
    title "MBZUAI-Paris/MixtureKit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-28 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e81142897fe1` · [字段定义](../../DATASET.md)*
