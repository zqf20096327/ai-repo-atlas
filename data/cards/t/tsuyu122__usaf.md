# tsuyu122/usaf

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-04 · [GitHub](https://github.com/tsuyu122/usaf) · 个人维护

**消费级显卡上微调 MoE 大模型的稀疏训练工具**

面向无高端 GPU 用户的 MoE 模型微调框架：以梯度幅值选取 0.5% 专家参数做稀疏训练，同时用 SGD 协同训练路由器，配合 RigL 动态重选、4-bit 量化权重与 fp16 常驻缓存降低资源占用。参考运行在 AMD RX 6750 XT 12GB（DirectML）上完成 Qwen3-30B-A3B 的 180 步训练（7.64h，峰值 RAM 19GB）；CUDA 路径代码完成但未测。支持 Qwen3-MoE/Mixtral/OLMoE/DeepSeek-MoE 布局，通过 pip 源码安装，环境变量配置，提供通用 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 0.5% 专家参数稀疏训练 + 路由器协同训练，12GB GPU 可跑 Qwen3-30B-A3B
- RigL 每 50 步动态重选活跃权重
- 4-bit 量化权重 + fp16 常驻缓存 + 五个 Vulkan 核（对 PyTorch 数值验证）
- 无配置文件，全部通过环境变量与 31 参数通用 CLI 控制

## 适用场景

- 在 12GB 消费级/AMD 显卡上微调 MoE 模型（如 Qwen3-30B-A3B）
- 训练 LoRA/QLoRA 无法触及的专家权重与路由器
- 用 --resume/--export 完成断点续训与量化导出

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: Fine-tune MoE models on hardware that can barely run inference.
> L7: Qwen3-30B-A3B (used in all benchmarks on this page) needs 60GB in fp16. Full fine-tuning needs 120GB+. USAF trains 2
> L175: |DirectML (AMD)|Production - the configuration behind every number on this page|

## 星数曲线

```mermaid
xychart-beta
    title "tsuyu122/usaf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `189dfb21b980` · [字段定义](../../DATASET.md)*
