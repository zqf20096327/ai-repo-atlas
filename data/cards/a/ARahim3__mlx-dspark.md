# ARahim3/mlx-dspark

⭐ 792 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/ARahim3/mlx-dspark) · [官网](https://arahim.dev/mlx-dspark/) · 个人维护

**在 Apple Silicon 上无损加速本地 LLM 解码的推测推理引擎**

在 Apple Silicon 上以 MLX 原生运行 EAGLE 系推测解码方法的推理引擎，涵盖 DeepSeek 的 DSpark、z-lab 的 DFlash 及其后续 DFlash 2 与 DSpine；目标模型逐 token 校验草稿，输出与普通解码一致，仅改变速度。提供 CLI、Python 接口及单端口同时兼容 OpenAI 与 Anthropic API 的服务器，支持 tool calling、流式输出与基准测试；首次运行时自动测量本机成本曲线推导 draft 上限，并按 --model 自动解析配对 drafter。附独立 Mac 应用（聊天、模型管理、遥测、roofline 视图）。不含 DeepSeek-V4 本身的推理。

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

- 无损推测解码：目标模型逐 token 校验，输出与普通解码一致
- 自动按本机成本曲线推导 draft 上限，--model 自动解析配对 drafter
- 单端口同时提供 OpenAI 与 Anthropic 兼容 API，支持 tool calling 与流式
- 附原生 Mac 应用：模型管理、推测解码遥测与 roofline 视图

## 适用场景

- 在自己的 Mac 上更快地本地运行 Gemma-4、Qwen3 等消费级模型
- 为 Claude Code 或 Codex 提供本地模型后端
- 把本地模型接入 Open WebUI、SillyTavern、Continue/Cline 等前端
- 对多种推测解码方法做可复现的基准对比

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L16: mlx-dspark runs EAGLE-family speculative-decoding drafters natively on Apple Silicon: DeepSeek's
> L123: first use (none bundled). No server framework is pulled in — the API server is built on the standard
> L181: `--mode auto` picks the best available speculation for any target (a known DSpark drafter → else

## 星数曲线

```mermaid
xychart-beta
    title "ARahim3/mlx-dspark 星数(近 21 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-23", "2026-11-25"]
    y-axis "stars" 717 --> 798
    line [723, 724, 725, 726, 727, 728, 730, 732, 733, 725, 736, 738, 737, 738, 739, 740, 741, 742, 743, 741, 792]
```

2026-10-23 723 → 2026-11-25 792（+69）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `88e31f88a21a` · [字段定义](../../DATASET.md)*
