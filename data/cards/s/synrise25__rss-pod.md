# synrise25/rss-pod

⭐ 33 · Go · MIT · 推送 2026-10-26 · [GitHub](https://github.com/synrise25/rss-pod) · [官网](https://rss-pod.ssyserver.com) · 个人维护 · 中文 README

**自托管应用：把 RSS 订阅转成对话式播客供通勤收听**

用 Go 编写的自托管 RSS 转播客应用：通过 OpenAI 兼容 LLM 把文章内容改写为多角色对话脚本，用 Edge TTS 或 Azure Speech 合成音频，并提供中英文网页播放器与播客 RSS 输出。内容来源支持直连 RSS、Jina 与 Crawl4AI 扩展，可选内容审查；PostgreSQL+River 存储进度支持断点续跑，S3/MinIO 存储音频与脚本。需自备数据库、对象存储与至少一个 LLM 服务，可单个 Go 二进制或 Docker 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 LLM 生成多角色对话脚本，有序 LLM 降级链
- Edge TTS / Azure Speech / Azure MultiTalker 语音合成，可自定义角色与音色
- PostgreSQL+River 持久化进度，失败自动重试与断点恢复
- 提供中英文网页播放器、管理页与播客 RSS 输出

## 适用场景

- 通勤、开车时用播客形式收听没时间读的 RSS 订阅
- 自建把信息源自动转为每日对话播客的流水线
- 在管理页审查与隐藏不合适的生成内容

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L18: rss-pod is a self-hosted RSS-to-podcast app. It uses an OpenAI-compatible LLM to
> L19: turn content into multi-speaker conversations, synthesizes audio with Edge TTS
> L20: or Azure Speech, and provides a web player and podcast RSS feeds. Listen to the

## 星数曲线

```mermaid
xychart-beta
    title "synrise25/rss-pod 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c32b8601d7cf` · [字段定义](../../DATASET.md)*
