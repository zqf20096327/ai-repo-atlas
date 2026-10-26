# RicherTunes/Brainarr

⭐ 46 · C# · MIT · 推送 2026-09-14 · [GitHub](https://github.com/RicherTunes/Brainarr) · 个人维护

**Lidarr 的本地优先 AI 音乐推荐导入清单插件**

Brainarr 是嵌入 Lidarr 导入清单工作流的插件，用 AI 生成专辑/艺人推荐：对曲库做指纹、选取代表性风格、采样后渲染提示词，经 LLM 产出建议，再经 MusicBrainz 富化、幻觉过滤、置信度门槛与人工复核队列后入库。支持 14 个 AI 提供方，其中 Ollama 与 LM Studio 可完全本地离线运行，云提供方（OpenAI/Anthropic/Gemini 等）为可选。附带只读的 Library Healer 曲库诊断、Prometheus 指标与成本可见性。要求 Lidarr 3.1.2.4913+ 且处于 plugins/nightly 分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性推荐管线：曲库指纹→风格选择→采样→提示词渲染，结果可复现
- 14 个提供方：2 本地（Ollama/LM Studio）+ 8 云 + 3 订阅 + 1 CLI，默认纯本地
- 幻觉过滤、置信度门槛、复核队列与 MusicBrainz MBID 校验
- 只读 Library Healer 诊断与 Prometheus 指标/成本可见性

## 适用场景

- 在 Lidarr 内获得不离开本地网络的 AI 音乐推荐
- 对推荐结果做置信度过滤与人工复核后再导入
- 诊断 Lidarr 曲库中的缺失文件与元数据问题

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L17: - **14 AI providers** — 2 local (Ollama, LM Studio), 8 cloud (OpenAI, Anthropic, Gemini, Perplexity, Groq, DeepSeek
> L190: Brainarr is an import list plugin that enriches Lidarr with AI-assisted album discovery while staying inside Lidar
> L204: Out of the box Brainarr stays purely local through Ollama/LM Studio, including iterative refinement defaults that 

## 星数曲线

```mermaid
xychart-beta
    title "RicherTunes/Brainarr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3a62278926a4` · [字段定义](../../DATASET.md)*
