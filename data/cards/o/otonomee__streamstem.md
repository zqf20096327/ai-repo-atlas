# otonomee/streamstem

⭐ 40 · Python · 推送 2025-12-08 · [GitHub](https://github.com/otonomee/streamstem) · [官网](http://www.streamstem.com) · 个人维护

**网页应用：从 YouTube/Spotify 歌曲分离出人声、鼓等人声/伴奏分轨**

基于 Flask 的 Web 应用：用户输入 YouTube 或 Spotify 歌曲链接，经 yt-dlp 抽取音频后交给 Demucs 音乐源分离模型，生成 2/4/6 轨分轨（人声、鼓、贝斯、吉他、钢琴等），可选格式下载（MP3/WAV/FLAC）。Spotify 链接需配置 Spotify API 与 YouTube Data API 凭据用于 URL 转换；YouTube 链接无需 API key。安装方式为克隆仓库后 pip 安装依赖并运行 Python 脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Demucs 模型执行音乐源分离，生成 2/4/6 轨 stems
- 支持 YouTube 与 Spotify 链接输入，输出 MP3/WAV/FLAC
- Spotify URL 转换需 Spotify API 与 Google API 凭据，YouTube 链接无需

## 适用场景

- 把喜欢的歌曲分离出人声或伴奏用于练习
- 制作卡拉OK或混音用的分轨素材
- 从 YouTube 视频提取音频并按乐器拆分

## 场景标签

 · 领域:音频/音乐处理

## 证据(README 行号)

> L9: - Demucs ML model: Demucs is an music source separation model that creates the stems
> L3: ## Extract the "stems" (e.g. drums, vocals, bass) from any song on Spotify or Youtube into separate audio files

## 星数曲线

```mermaid
xychart-beta
    title "otonomee/streamstem 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-30 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e9f0f6dc4b03` · [字段定义](../../DATASET.md)*
