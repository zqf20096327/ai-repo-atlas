# laipz8200/anime-librarian

⭐ 21 · Python · NOASSERTION · 推送 2026-07-28 · [GitHub](https://github.com/laipz8200/anime-librarian) · 个人维护

**调用 Dify 工作流自动重命名整理视频文件的命令行工具**

Python 3.13 命令行工具：把待整理目录中的文件名与媒体库现有目录发送给已发布的 Dify 工作流，获取移动计划后进行严格校验（来源精确匹配、扩展名保留、禁止越界与重复移动），经一次确认后执行移动。提供 Rich 表格、纯文本与 JSON Lines 三种输出格式，支持 true dry run。需自建或使用 Dify 部署并导入随附的 DSL 工作流文件，可选配置 TMDB API token 以获得更丰富元数据。支持视频与字幕共 16 种扩展名，扫描不递归。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将文件名与媒体库目录交给 Dify 工作流生成移动计划
- 对 AI 建议做严格校验：路径越界、重复移动、扩展名变更均被拒绝
- dry run 不提示不改动文件系统；输出 table/plain/JSON Lines 三种格式
- 附带回随仓库的 Dify DSL 工作流文件，可选 TMDB 元数据

## 适用场景

- 把下载目录中的动漫发布文件名整理为规范的媒体库路径
- 在执行前以 JSON 预览 AI 给出的重命名计划供脚本或人工审查
- 整理 mkv/mp4 等视频与 srt/ass 等字幕文件

## 场景标签

 · 领域:文件整理/媒体库工具

## 证据(README 行号)

> L9: AnimeLibrarian sends the filenames in an incoming folder and the existing folders
> L10: in a media library to a Dify workflow. It validates the returned move plan, shows

## 星数曲线

```mermaid
xychart-beta
    title "laipz8200/anime-librarian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `af456983ab7f` · [字段定义](../../DATASET.md)*
