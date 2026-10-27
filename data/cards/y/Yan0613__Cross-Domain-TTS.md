# Yan0613/Cross-Domain-TTS

⭐ 30 · Python · 推送 2026-10-14 · [GitHub](https://github.com/Yan0613/Cross-Domain-TTS) · 个人维护

**论文官方代码：跨领域测试时扩展方法的评测框架**

IJCAI 2026 论文《Cross Domain Test Time Scaling》的官方代码库，实现 CR-TTS 方法，用于在跨领域任务上扩展知识与推理。安装需创建 Python 3.10 conda 环境，安装依赖及 vllm、transformers 用于推理；数据置于 data 文件夹（含 aime24 等基准）；提供评测脚本，支持 DeepSeek-R1-Distill-Qwen-1.5B/7B、Qwen3-8B、GURU、Huatuo-O1、M1 等模型的评测运行，建议以输出重定向方式后台运行并记录日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CR-TTS 跨领域测试时扩展方法的官方实现
- 提供 DeepSeek-R1-Distill 系列、Qwen3-8B、GURU、Huatuo-O1、M1 等模型的评测脚本
- 依赖 vllm 与 transformers 运行推理
- 含数学公式处理的 latex2sympy 组件（pip install -e 安装）

## 适用场景

- 复现论文的跨领域测试时扩展实验
- 在不同开源推理模型上运行 CR-TTS 评测
- 基于评测脚本开展测试时扩展方法研究

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # [IJCAI 2026]Cross Domain Test Time Scaling: Scale Knowledge and Reasoning on Cross Domains
> L44: ## 🎯 Testing

## 星数曲线

```mermaid
xychart-beta
    title "Yan0613/Cross-Domain-TTS 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 29 --> 32
    line [31, 30, 30]
```

2026-10-18 31 → 2026-10-27 30（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `03f83ddd2c3b` · [字段定义](../../DATASET.md)*
