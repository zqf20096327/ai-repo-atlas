# rayl15/Godwit

⭐ 25 · Swift · Apache-2.0 · 推送 2026-08-07 · [GitHub](https://github.com/rayl15/Godwit) · [官网](https://rayl15.github.io/Godwit/) · 个人维护

**在 16 GB Mac 上流式运行 GPT-OSS-120B 的 Swift+Metal 推理引擎**

面向 Apple Silicon 的本地 MoE 模型推理引擎：只将约 2.12 GiB 的共享主干常驻内存，专家权重按需从 SSD 流式读取，从而在 16 GB 内存机器上运行 59 GiB 的 GPT-OSS-120B，代价是约 1.4 tok/s 的吞吐。支持 GPT-OSS-120B/20B 与 Qwen3-30B-A3B，单一二进制运行时切换。提供 chat、serve 网页面板、range 专家特化探测、tokenize 等命令；无第三方依赖，需 macOS 26+、Swift 6.2+，源码编译安装，首装需 1-3 小时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主干常驻 2.12 GiB、专家权重按需从 SSD 流式加载
- 单一二进制支持 GPT-OSS-120B/20B 与 Qwen3-30B-A3B
- 无第三方依赖，Swift + Metal 实现，shader 运行时编译
- 内置 range 命令探测 4,608 个专家的主题特化分布

## 适用场景

- 在小内存 Mac 上本地运行超大参数量 MoE 模型
- 通过网页面板或命令行进行本地对话与脚本化生成
- 观测与分析 MoE 模型的专家路由行为

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L18: Godwit runs GPT-OSS-120B — 59 GiB
> L19: on disk — on an Apple Silicon Mac with 16 GB of memory, by keeping only the
> L124: - Apple Silicon Mac, macOS 26+, Swift 6.2+

## 星数曲线

```mermaid
xychart-beta
    title "rayl15/Godwit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-30 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `415b50c87d6f` · [字段定义](../../DATASET.md)*
