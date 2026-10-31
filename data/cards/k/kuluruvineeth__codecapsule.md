# kuluruvineeth/codecapsule

⭐ 21 · TypeScript · 推送 2026-07-30 · [GitHub](https://github.com/kuluruvineeth/codecapsule) · 个人维护

**描述即出应用：AI 生成代码并在 E2B 沙箱中实时运行预览**

用户输入自然语言描述，模型流式生成代码写入编辑器，随后在 E2B 沙箱容器（依赖预装）中真实执行，运行中的应用通过 iframe 回传到浏览器代码旁展示。支持 8 家提供商共 19 个模型，包括 OpenAI、Anthropic、Google、Mistral、Groq、Fireworks、Together AI 及 Ollama 本地模型。提供 Next.js、Vue/Nuxt、Streamlit、Gradio 四种沙箱模板（默认启用 Next.js），基于 Next.js App Router 与 Vercel AI SDK 构建，含 Vercel KV 限流与可选 Supabase 认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 个模型、8 家提供商，含 Ollama 本地模型
- 生成代码在 E2B 沙箱真实执行并回传 iframe 预览
- 四种预构建沙箱模板：Next.js/Vue/Streamlit/Gradio
- 自定义沙箱模板通过 Dockerfile + e2b.toml 构建注册

## 适用场景

- 用自然语言快速生成并即时预览前端/数据应用
- 对比不同模型生成同一应用的效果
- 在沙箱中安全运行 AI 生成的代码

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L16: You type what you want. A model writes the code, streaming it into the editor as it goes. The result is
> L17: then **executed in a real E2B sandbox** — a fresh container with the dependencies already installed — and
> L22: **19 models across 8 providers.** OpenAI (`o1-preview`, `o1-mini`, `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`),

## 星数曲线

```mermaid
xychart-beta
    title "kuluruvineeth/codecapsule 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a19cbaef1538` · [字段定义](../../DATASET.md)*
