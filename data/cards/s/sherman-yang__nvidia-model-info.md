# sherman-yang/nvidia-model-info

⭐ 17 · JavaScript · MIT · 推送 2026-07-13 · [GitHub](https://github.com/sherman-yang/nvidia-model-info) · 个人维护

**浏览与实测 build.nvidia.com 模型的本地 Web 仪表盘**

面向反复进行 NVIDIA 托管模型对比工作的本地 Web 仪表盘：从 integrate.api.nvidia.com 的 /v1/models 与 NGC catalog 两个来源拉取模型目录和模型卡规格，生成可排序、可搜索的表格；通过实时探测（需 NVIDIA API key）检测可用性、延迟、实际部署的上下文窗口（解析 vLLM 校验错误或二分探测）、工具调用支持，以及推理/结构化输出/并行工具调用/视觉输入等能力，并提供可复制的 cURL 示例。探针调用经全局限速（默认 39 RPM，低于 NVIDIA 免费层 40 RPM 上限）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双来源数据：/v1/models 目录 + NGC 模型卡规格（model_specs.json 随仓库提交）
- 实时探测可用性、延迟、工具调用与部署上下文窗口（错误解析 + 二分/输入侧探测）
- 能力探测覆盖推理开关、结构化输出（json_schema / guided_json）、tool_choice required、并行工具调用、视觉输入
- 全局探针限速（默认 39 RPM）与 429 指数退避及延迟重试轮

## 适用场景

- 我在多个 NVIDIA 托管模型之间选型时做并排对比
- 我需要核验模型卡声称的上下文窗口与端点实际部署值是否一致
- 我需要确认某模型是否真的支持工具调用、结构化输出或视觉输入

## 场景标签

 · 领域:LLM 基础设施/模型评测

## 证据(README 行号)

> L5: A local web dashboard for browsing the free NVIDIA models listed on
> L9: The app is built for repeated model comparison work: dense table layout,

## 星数曲线

```mermaid
xychart-beta
    title "sherman-yang/nvidia-model-info 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [17, 16, 17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `beddcff628f3` · [字段定义](../../DATASET.md)*
