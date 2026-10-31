# Peter-SB/n8n-ai-instagram-scraper

⭐ 39 · Python · 推送 2026-01-10 · [GitHub](https://github.com/Peter-SB/n8n-ai-instagram-scraper) · 个人维护

**自托管的 n8n AI 工作流：抓取并转录 Instagram Reels，结构化存表**

基于 n8n 低代码工作流构建的自托管管道：通过 Google 表单提交 Reels 链接，轮询新条目后用 Instaloader 下载视频与描述，fast-whisper 在本地转录音频，再由 LLM（GPT-4.1-mini，也试验过自托管 Ollama 模型）提取可操作信息并归入四类，按类别写入 Google Sheets 各标签页。部署采用 Docker Compose 与 Nginx 反向代理。README 为教学性项目记录，作者自述分类准确性有局限且未做深入提示工程。

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

- Google 表单触发，n8n 每 5 分钟轮询新条目
- Instaloader 抓取视频与描述，fast-whisper 本地 CPU 转录
- LLM 提取信息项并归入四类，输出符合目标 schema 的 JSON
- Switch 节点按类别路由写入 Google Sheets 标签页

## 适用场景

- 旅行规划时自动整理 Reels 中的食宿与攻略信息
- 营销团队批量结构化短视频内容做调研
- 小规模内容监测与趋势数据积累

## 场景标签

`网页抓取` `工作流自动化` `语音识别` · 领域:效率与自动化

## 证据(README 行号)

> L6: Self hosted AI workflow for scraping Instagram Reels (audio and description). Extracting, summarising and categorisi
> L23: The workflow was built with a tool called n8n, a low code/no code agentic workflow builder. It allows simple workfl

## 星数曲线

```mermaid
xychart-beta
    title "Peter-SB/n8n-ai-instagram-scraper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 37 --> 40
    line [38, 39]
```

2026-10-18 38 → 2026-10-31 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6ddb8e1ec12b` · [字段定义](../../DATASET.md)*
