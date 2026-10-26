# stfurkan/bitgpu

⭐ 29 · TypeScript · MIT · 推送 2026-07-23 · [GitHub](https://github.com/stfurkan/bitgpu) · 个人维护

**浏览器端 1-bit LLM 的 WebGPU 推理运行时**

面向 Web 前端开发者的零依赖 ESM 库：在浏览器中通过 WebGPU 运行 1-bit（二值权重）LLM，参考适配 Bonsai 1.7B/4B/8B（Qwen3 架构）与 Bonsai-27B（Qwen3.5 混合线性注意力），权重从 Hugging Face Hub 流式加载，全程本地 GPU 推理。提供 GPU 驻留解码、跨轮 KV 缓存复用、f16/q8 缓存压缩、会话快照、attention-sink 滚动窗口的无限对话、promptLookup 投机解码、约束 JSON 输出与思考预算控制。在 Apple/NVIDIA/较新 AMD 走 subgroup 快速路径，其他 WebGPU 设备走回退路径；1-bit 架构外的模型不在当前范围。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器内 WebGPU 运行 1-bit LLM，零运行时依赖，权重从 Hugging Face Hub 流式加载
- 对参考模型做 bit-exact/贪心精确门控验证
- KV 缓存 f16/q8 压缩与 attention-sink 滚动窗口，实现固定显存下的长对话
- 逐 token 校验的约束 JSON/schema 解码与 thinkBudget 推理预算控制

## 适用场景

- 在网页中本地 GPU 运行 1-bit LLM 做流式对话
- 需要结构化保证 JSON 输出的前端 AI 功能
- 在有限显存下做长上下文/多轮会话推理

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: A fast, dependency-free WebGPU runtime for **low-bit LLMs** in the browser.
> L5: Today it runs **1-bit (binary-weight)** models.
> L162: The engine is deliberately ids-in/ids-out; `bitgpu/chat` is the batteries-included text layer on

## 星数曲线

```mermaid
xychart-beta
    title "stfurkan/bitgpu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2124d75b1135` · [字段定义](../../DATASET.md)*
