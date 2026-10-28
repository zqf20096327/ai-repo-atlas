# Yunado/dsh-qwen38-local-qol

⭐ 21 · JavaScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/Yunado/dsh-qwen38-local-qol) · 个人维护 · 中文 README

**本地运行 Qwen3.8 系列的 DeepSeek Harness QoL 插件**

面向 DeepSeek Harness（DSH）的插件，用于本地运行 Qwen3.8-27B 与 Qwen3.8-Flash-Next，不改核心补丁。功能包括逐请求 thinking 预算（按 low/medium/xhigh 分档下发）、压缩后端（摘要预填充裁剪、图片降级为文本占位、工具结果截断，压缩调用关闭 thinking 以免烧尽输出帽）、工具结果中图像块的多模态透传，以及实时设置 tab。支持 llama.cpp、NInfer、TabbyAPI、oMLX 四种服务后端，通过 dsh plugin 命令安装，附带与各 DSH 宿主版本的兼容矩阵。

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

- 逐请求 thinking 预算，兼容 llama.cpp/TabbyAPI/oMLX/NInfer 四种后端
- 压缩后端：thinking-off 压缩调用避免检查点被 token 上限截断
- 工具结果中嵌套图像以多模态 content array 透传，不可读时降级为文本占位
- 实时设置 tab，逐后端独立记忆配置并热持久化

## 适用场景

- 在 DSH 中本地运行 Qwen3.8 并按请求控制推理预算
- 长会话场景下调整压缩触发点与裁剪策略以省出上下文
- 在不同本地推理后端（llama.cpp/MLX/ExLlamaV3/TensorRT-LLM）间切换并保留各自配置

## 场景标签

 · 领域:LLM 工具链/插件

## 证据(README 行号)

> L9: A QoL plugin for DeepSeek Harness (DSH) for running **Qwen3.8 locally**, with no core patches and no pi-ai patchfile
> L12: - **Serving engines**: llama.cpp `llama-server` · NInfer · TabbyAPI (ExLlamaV3) · oMLX (Apple Silicon MLX)
> L51: - **Per-request thinking budgets.** The llama.cpp line sends the selected per-effort budget on every request (`reas

## 星数曲线

```mermaid
xychart-beta
    title "Yunado/dsh-qwen38-local-qol 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ea5a4d418639` · [字段定义](../../DATASET.md)*
