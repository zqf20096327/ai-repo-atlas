# yassinsolim/soundalike

⭐ — · [GitHub]() · 个人维护

**基于音频相似度的开源音乐发现工具：找听起来像你喜欢的歌**

围绕音频相似度构建的开源音乐推荐系统，索引约 110 万首歌。比较预计算的音频表示（EfficientNet 与 CLAP 两种表征）及节奏、动态、低频等特征，不使用听歌历史作为排序信号。提供四种使用形态：Spicetify 扩展（Spotify 桌面端右键找相似）、网页应用（免登录搜索任意 Deezer 歌曲）、iOS/Android 原生伴生应用，以及本地应用与命令行工具。搜索无结果数量限制，语言过滤与版本折叠等排序保护策略可见于 README。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 基于音频相似度的推荐：EfficientNet 与 CLAP 两种音频表征组合排序
- 多种使用形态：Spicetify 扩展、Web 应用、iOS/Android 应用、CLI 与本地应用
- 索引约 110 万首歌，可对任意有 Deezer 预览的歌曲生成匹配
- 提供研究代码、基准测试与工程记录（案例研究、V3 研究日志）

## 适用场景

- 在 Spotify 桌面端右键一首歌找听感相似的歌曲
- 在浏览器搜索任意 Deezer 歌曲并按声音排序相似曲目
- 通过手机伴生应用对正在播放的歌曲找相似
- 本地部署 CLI/服务用于自己的音乐发现实验

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L5: **Find songs that sound like a track you already enjoy.**
> L29: recommender built around audio similarity. It compares precomputed audio
> L34: covers, samples, and shared melodies first, then the songs a small model ranks


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `ab10b79d5ecf` · [字段定义](../../DATASET.md)*
