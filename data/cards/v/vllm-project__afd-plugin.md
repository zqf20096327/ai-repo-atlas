# vllm-project/afd-plugin

⭐ 240 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/vllm-project/afd-plugin) · 组织维护 · 中文 README

**vLLM 注意力-FFN 分离部署插件（GPU 与昇腾 NPU）**

vLLM 官方生态的外部插件，实现 Attention-FFN Disaggregation（AFD）：提供插件自有的 worker 类、model runner、模型包装器、连接器、配置校验与兼容垫片，通过 vllm.general_plugins 入口点与 --additional-config 生效，不修改 vLLM 源码。面向在 CUDA GPU 与昇腾 NPU 上分离部署 DeepSeek、Qwen3 MoE 系列模型的推理工程师。目标运行时锁定 vLLM v0.30.0；README 自述仍处实验阶段，需更多大规模硬件测试。安装依赖 uv 与 Python 3.10-3.13。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 vLLM 插件入口点注入 AFD 行为，不修改 vLLM 源码
- 支持 CUDA GPU 与昇腾 NPU（三种连接器：NCCL P2P / CAMP2P / CAMAsync）
- 支持 DeepSeekV2/V3/V3.2 与 Qwen3/Qwen3.5/3.6 MoE 家族
- Eager 与 FULL_DECODE_ONLY 图执行，Native DBO 限两个 ubatch

## 适用场景

- 在 vLLM 0.30.0 上以分离的 Attention/FFN 角色部署 DeepSeek MoE 模型
- 在昇腾 910C/Atlas A3 上运行 AFD 推理部署
- 对照 recipe 与 E2E 测试复现已记录的 GPU/NPU 验证场景

## 场景标签

 · 领域:LLM 推理基础设施

## 证据(README 行号)

> L7: **afd-plugin** is a vLLM
> L19: source tree. AFD behavior is installed through the `vllm.general_plugins` entry
> L31: - vLLM plugin registration, AFD configuration, and runtime validation.

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/afd-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 239 --> 241
    line [240, 240]
```

2026-10-18 240 → 2026-10-22 240（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8b9b6e7cf808` · [字段定义](../../DATASET.md)*
