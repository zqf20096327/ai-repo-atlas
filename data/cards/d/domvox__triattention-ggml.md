# domvox/triattention-ggml

⭐ 16 · Python · Apache-2.0 · 推送 2026-04-18 · [GitHub](https://github.com/domvox/triattention-ggml) · 个人维护

**面向 llama.cpp 的 KV cache 频率剪枝实现（HIP/ROCm GPU 内核）**

基于 TriAttention 论文（Mao et al., 2026）的独立 C/HIP 实现，用于 llama.cpp：以三角函数频率预测对 KV 行打分，在解码阶段逐出低分行并在 GPU 上物理压实缓存。工作流为离线校准生成统计文件、运行期每 128 个解码 token 打分一次，采用解码-only 设计（prefill 保持稠密）。提供环境变量配置预算与渐进逐出比例。README 报告 65k 上下文下 +121% 解码加速、MATH500 精度 -12.0pp；限制包括多 slot 服务近似、需任务型评测衡量质量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解码阶段按频率打分逐出 KV 行并在 GPU 物理压实
- 离线校准 + 运行期每 128 token 打分的两阶段流程
- 指数渐进逐出（10→100%）防止语义冲击
- 集成于 TurboQuant HIP fork 的分支

## 适用场景

- 长上下文推理时降低 KV cache 显存占用并加速解码
- RDNA2/3/4 显卡的 llama.cpp 用户做 cache 预算控制
- 复现/对比 TriAttention 论文在 ggml 运行时的效果

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: Decode-only KV cache eviction with GPU scoring kernel. Scores KV rows by trigonometric frequency prediction, evicts 
> L5: Based on TriAttention (Mao et al., 2026) — independent C/HIP implementation for llama.cpp.

## 星数曲线

```mermaid
xychart-beta
    title "domvox/triattention-ggml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `82d932769c76` · [字段定义](../../DATASET.md)*
