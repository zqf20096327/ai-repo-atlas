# evandempsey/podcast-llm

⭐ 153 · Python · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/evandempsey/podcast-llm) · [官网](https://evandempsey.github.io/podcast-llm/) · 个人维护

**仅凭标题自动生成 AI 播客对话的 CLI/Web 工具**

以 LLM 与文本转语音为引擎的播客生成系统：提供两种模式——研究模式用 Tavily 搜索自动收集内容，上下文模式从给定 URL/文件生成带章节与来源引用的脚本；经多轮问答式脚本写作后由 Google Cloud 或 ElevenLabs 合成多人语音。支持断点续跑、章节级预览/重录/校对（用转写比对脚本）、Gradio 网页编辑器。pip 安装，需配置多家 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 研究模式：用 Tavily 搜索自动选题取材，全程无需人工整理素材
- 上下文模式：从 URL/文件生成带章节和来源引用的脚本，可切换 Claude/Google/OpenAI 写作模型
- 章节级渲染流水线：预览、转写比对校对、单章重录、断点缓存复用音频
- Gradio 网页界面编辑对话并导出完整音频与文稿

## 适用场景

- 给一个主题标题，自动生成一期可下载的多人对话播客
- 把已有资料/链接转成带引用的播客脚本并配音
- 在网页界面逐章修改对话后重新合成音频

## 场景标签

`语音合成` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: An intelligent system that automatically generates engaging podcast conversations using LLMs and text-to-speech tec
> L17:  - Research mode: Automated research and content gathering using Tavily search

## 星数曲线

```mermaid
xychart-beta
    title "evandempsey/podcast-llm 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-28"]
    y-axis "stars" 152 --> 154
    line [153, 153]
```

2026-11-23 153 → 2026-11-28 153（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `80955eeb2555` · [字段定义](../../DATASET.md)*
