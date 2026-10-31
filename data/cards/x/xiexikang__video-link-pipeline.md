# xiexikang/video-link-pipeline

⭐ 23 · Python · MIT · 推送 2026-06-23 · [GitHub](https://github.com/xiexikang/video-link-pipeline) · 个人维护 · 中文 README

**视频链接到转录/摘要产物的本地处理流水线工具**

本地视频处理工具集：从 Bilibili、YouTube 等站点下载媒体、字幕和元数据，用 Whisper 生成转录文本和 srt/vtt 字幕，再调用大模型生成摘要与关键词，按任务目录持续写入 manifest.json 状态文件。以 `vlp` CLI 与本地 Web 工作台两种形式提供，支持 cookies 登录导出、多站点输出归类、环境自检（vlp doctor）。需 Python 3.10+，摘要依赖外部 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- vlp run 一键串联下载、Whisper 转录与 LLM 摘要
- manifest.json 机器可读的任务状态供自动化与 Web 展示复用
- CLI 与本地 Web 工作台双入口，可查看任务看板、日志与产物预览
- cookies-login 独立浏览器 profile 完成站点登录并复用 cookies.txt

## 适用场景

- 把 B 站 / YouTube 视频拉到本地转成 transcript、字幕和摘要
- 持续整理视频内容并保留稳定的任务目录与状态文件
- 对本地已有视频/音频文件做批量转录与关键词提取

## 场景标签

`语音识别` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L6: - 用 Whisper 生成转录文本和字幕
> L7: - 用大模型生成摘要和关键词
> L26: - `vlp summarize <transcript.txt>`：生成摘要和关键词

## 星数曲线

```mermaid
xychart-beta
    title "xiexikang/video-link-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5c07e2bdfbca` · [字段定义](../../DATASET.md)*
