# prabal-rje/latentscore

⭐ 44 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/prabal-rje/latentscore) · [官网](https://latentscore.com) · 个人维护

**从文本描述本地生成环境音乐的 Python 库，无需 GPU**

Python 库，把文字描述（如 'morning coffee shop'）经检索映射与程序化合成生成环境音乐，默认 CPU 运行、模型权重约 90 MB，提供一行代码渲染播放的 API。面向创作者与开发者：支持 Colab 免费运行、Docker 全套 demo 与 JupyterLab、macOS/Linux pip 安装（Python 3.11/3.12）。默认 fast 模型基于 LLM 蒸馏检索库；可选 extras 接入 LiteLLM 托管 LLM（Anthropic/Gemini/OpenAI）或 CLAP 音频检索。原生 Windows pip 不支持。有 SIGGRAPH Talks '26 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 文本→环境音乐的一行代码渲染（render().play()）
- CPU-only 运行，无需 GPU，模型约 90 MB
- MusicConfig 参数直接控制合成与流式/异步 API
- bring-your-own-LLM：经 LiteLLM 接入 Anthropic/Gemini/OpenAI 等托管模型

## 适用场景

- 为游戏或影像生成环境音景配乐
- 在脚本或 Notebook 中按文字描述即时生成氛围音乐
- 本地无 GPU 环境下做程序化音频创作

## 场景标签

 · 领域:生成式音频/创意工具

## 证据(README 行号)

> L7: **Generate ambient music from text. Locally. No GPU required.** - Read more about how it works.
> L23: ls.render("morning coffee shop").play()

## 星数曲线

```mermaid
xychart-beta
    title "prabal-rje/latentscore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-27 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `20a5c2341017` · [字段定义](../../DATASET.md)*
