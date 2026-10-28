# konjoai/squish

⭐ 20 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/konjoai/squish) · [官网](https://squish.run) · 组织维护

**Apple Silicon 上的本地 LLM 推理守护进程，兼容 OpenAI/Ollama API**

基于 MLX/Metal 的 macOS 本地 LLM 服务守护进程：权重一次性转换为 Metal 原生 bf16 布局并 mmap 进统一内存，实现约 0.5 秒冷启动；采用块分页 KV 缓存与提示 KV 缓存跨请求复用 prefill；提供 INT4/INT3/INT8 量化（含家族级精度闸门）与贪心无损投机解码；单服务器同时暴露 OpenAI 与 Ollama 兼容端点。面向单开发者单机场景，声明不支持 Apple Silicon 以外 GPU、多用户服务与多模态。附菜单栏应用 SquishBar 与 dashboard，通过 Homebrew/PyPI 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层权重缓存 + mmap 实现 ≈0.5s 冷启动（较 mlx_lm 冷加载快 54×，README 数据）
- 双缓存架构（块分页 KV + 提示 KV）跨请求复用 prefill，缓存命中 TTFT 为个位数毫秒
- 同一守护进程提供 OpenAI(/v1/*) 与 Ollama(/api/*) 双兼容端点
- INT3/INT4/INT8 量化，家族感知精度闸门阻断会降质的量化配置

## 适用场景

- 在同一模型高频调用、上下文变动的场景（agent 循环、代码审查、多轮对话）本地跑 LLM
- Mac 上将现有 OpenAI/Ollama 客户端指向本地端点，离线无 API key 使用
- 登录时常驻加载模型，避免每次长提示重复 prefill

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L73: - **Drop-in compatible** — OpenAI (`/v1/*`) *and* Ollama (`/api/*`) endpoints on one server. Point your existing cl
> L80: Requires Python 3.11–3.14 and macOS 13 (Ventura) or later on Apple Silicon.
> L142: - **No multi-user serving.** One developer, one machine — not a production API.

## 星数曲线

```mermaid
xychart-beta
    title "konjoai/squish 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9d4f016d63e9` · [字段定义](../../DATASET.md)*
