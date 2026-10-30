# hgsanyang/SoulTuner-Agent

⭐ 25 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/hgsanyang/SoulTuner-Agent) · 个人维护 · 中文 README

**自然语言音乐推荐 Agent：用一句话获得有解释的歌单**

开源的音乐推荐 agent（Python/FastAPI + LangGraph + Neo4j + Next.js）。用户以普通句子描述心情、场景或想避开的歌，Planner 大模型将请求拆为硬性要求与软偏好，图检索（Neo4j）与声学向量检索（MuQ/OMAR 或 CPU 用 M2D-CLAP）结果融合重排，并为每首歌给出推荐理由；点赞/收藏/跳过等反馈写入长期记忆影响后续排序。默认接入 DashScope/Qwen3.7 Plus，可换 SiliconFlow、Google、Volcengine 或本地 SGLang/vLLM/Ollama；另有项目自训 35B Planner（500 请求评估中 95.6% 选对意图与检索路径）。Docker Compose 部署，含音频审核入库管线与开发者模式隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 大模型规划检索 + 确定性代码校验，模型不直接编造歌单
- 知识图谱 + 双模型声学向量的混合检索与多源融合重排
- 点赞/收藏/跳过等反馈进入长期记忆（SQLite + Neo4j）
- 项目自训 35B Planner 可选，支持自托管 OpenAI 兼容端点

## 适用场景

- 用一句话描述心情或场景直接拿到带解释的歌曲推荐
- 在自有音乐库上建立可搜索、可个性化推荐的音乐系统
- 通过合法入库管线持续扩充可检索曲库

## 场景标签

`推荐系统` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L25: SoulTuner is an open-source music recommendation agent. Describe a mood, scene, sound, artist, or a song you want t
> L52: 1. **Understand the request** — the Planner separates hard requirements (for example, artist or language) from soft
> L93: To use another provider (SiliconFlow, Google, Volcengine, or local SGLang / vLLM / Ollama), change `MAIN_LLM_PROVID

## 星数曲线

```mermaid
xychart-beta
    title "hgsanyang/SoulTuner-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a622bd60e00c` · [字段定义](../../DATASET.md)*
