# justADeni/intel-npu-llm

⭐ 52 · Python · MIT · 推送 2026-07-04 · [GitHub](https://github.com/justADeni/intel-npu-llm) · 个人维护

**在 Intel NPU 上运行、量化并服务 LLM 的 Python CLI 工具**

基于 OpenVINO GenAI 的命令行工具：从 HuggingFace 拉取模型，量化为 symmetric int4，编译为 NPU 可用的 .blob（缓存以加速重载），随后可在终端聊天、暴露 OpenAI 兼容 API（/v1/chat/completions 等）、并显示 NPU 利用率实时面板。面向拥有 Intel Core Ultra（Meteor Lake/Arrow Lake/Lunar Lake）NPU 的用户，需 Python≥3.10 与 Intel NPU 驱动。限制：7B 模型接近约 13 TOPS NPU 上限；NPU 一次处理一个生成任务，API 请求排队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令完成拉取、int4 量化与 NPU 编译，blob 缓存加速重载
- OpenAI 兼容 API（流式+非流式 /v1/chat/completions、/v1/completions、/v1/models）
- 终端实时 NPU 利用率面板：tokens/s、TTFT、滚动曲线
- 长对话自动摘要压缩（--compact），避免上下文溢出重置

## 适用场景

- 在带 NPU 的 Intel 笔记本上本地运行和对话小规模 LLM
- 把 NPU 上的模型以 OpenAI 兼容 API 形式提供给本地客户端
- 监控 NPU 利用率与推理性能

## 场景标签

`模型量化` `推理引擎` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Run, quantize and serve large language models on your **Intel NPU** — from a single, modern CLI.
> L133: 3. **Run / Serve / Display** — a single `openvino_genai.LLMPipeline` on the `NPU` device drives chat, the
> L36: - An **Intel Core Ultra** CPU with an NPU (Meteor Lake / Arrow Lake / Lunar Lake).

## 星数曲线

```mermaid
xychart-beta
    title "justADeni/intel-npu-llm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-31 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `21221f97ca33` · [字段定义](../../DATASET.md)*
