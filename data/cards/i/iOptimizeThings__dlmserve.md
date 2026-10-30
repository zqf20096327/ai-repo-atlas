# iOptimizeThings/dlmserve

⭐ 16 · Python · MIT · 推送 2026-05-26 · [GitHub](https://github.com/iOptimizeThings/dlmserve) · 个人维护

**为扩散语言模型提供 OpenAI 兼容的 HTTP 推理服务**

面向扩散语言模型（LLaDA-8B-Instruct、LLaDA-1.5 等）的推理服务引擎：按扩散解码契约（双向注意力、固定画布、逐步去噪）设计，提供去噪步级别的自动连续批处理与可选 LocalLeap 逐行加速，暴露 OpenAI 兼容的 /v1/chat/completions 端点及扩散特有参数（num_denoising_steps、block_length 等）。供需要在 GPU 服务器上部署扩散 LLM 的开发者使用。限制：仅 Linux x86_64、单 GPU；Docker 镜像不支持 Blackwell 架构；SSE 逐 token 流式未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 去噪步级自动连续批处理（DLMSERVE_MAX_BATCH，默认 8）
- OpenAI 兼容 /v1/chat/completions，附扩散特有参数
- 可选 LocalLeap 加速（arXiv:2510.07081），可与批处理叠加
- Prometheus 指标与 Swagger/ReDoc 交互式 API 文档

## 适用场景

- 在自有 GPU 服务器上部署扩散语言模型并通过 OpenAI 兼容 API 调用
- 并发多客户端请求下获得批处理吞吐收益
- 对照 HuggingFace generate() 基线复现与测试批处理加速效果

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: OpenAI-compatible HTTP serving for diffusion language models.
> L10: Diffusion LLMs use bidirectional attention, a fixed-length canvas, and confidence-ranked parallel commit — not the 
> L66: OpenAI-compatible `/v1/chat/completions` with documented deviations

## 星数曲线

```mermaid
xychart-beta
    title "iOptimizeThings/dlmserve 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b045eedcb833` · [字段定义](../../DATASET.md)*
