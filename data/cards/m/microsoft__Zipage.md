# microsoft/Zipage

⭐ 15 · Python · MIT · 推送 2026-03-13 · [GitHub](https://github.com/microsoft/Zipage) · 组织维护

**微软开源的高并发 LLM 离线推理引擎，基于 KV 缓存压缩**

基于 PagedAttention 并支持 KV cache 压缩与淘汰的 LLM 离线推理引擎：通过压缩使每请求显存占用保持恒定以支撑高并发，提供异步解码、前缀缓存、张量并行等功能。实验部分称在保持 vLLM 95% 以上性能的同时 TPS 翻倍。通过源码 pip install -e . 安装，支持从 HuggingFace 下载模型后以 Python API 生成文本；在线引擎、chunked prefilling 等功能仍在 TODO 列表，设计参考 Nano-vLLM 实现。

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

- KV cache 压缩使每请求显存占用保持恒定
- 异步解码与压缩、前缀缓存、张量并行
- 提供数学基准（AMC23/AIME24/GSM8K）与 LongBench 脚本

## 适用场景

- 高并发场景下运行 LLM 离线推理
- 压缩 KV cache 以在有限显存内提升吞吐
- 复现推理引擎的基准测试实验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: A high-concurrency LLM offline inference engine based on PagedAttention and KV cache compression.
> L7: * **High Concurrency** - This project builds on PagedAttention and supports KV cache compression. The memory require

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Zipage 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `f68bac48e169` · [字段定义](../../DATASET.md)*
