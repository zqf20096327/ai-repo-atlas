# slauger/suno-cli

⭐ 14 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/slauger/suno-cli) · 个人维护

**调用 Suno AI 生成音乐的命令行工具**

Python 编写的 CLI 工具，通过 Suno API 从歌词与风格提示词生成歌曲并输出 MP3。支持单首生成与基于 YAML 的批量生成（可并行，面向专辑场景），自动写入带封面图的 ID3 标签，可选多种 AI 模型（V5、V4.5-All 等），并提供配置文件管理默认值与任务状态查询、下载命令。安装方式为 git clone 源码，需 Python 3.8+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从歌词+风格提示词生成歌曲，输出 MP3
- 基于 YAML 的批量生成，支持并行（专辑场景）
- 自动写入带封面图的 ID3 标签
- 支持多模型选择（V5、V4.5-All 等）

## 适用场景

- 通过命令行用 Suno AI 快速生成单曲
- 按 YAML 清单批量生成整张专辑
- 在脚本或工作流中集成音乐生成

## 场景标签

 · 领域:AI 音乐生成/命令行工具

## 证据(README 行号)

> L3: > CLI tool for generating music with Suno AI
> L10: - 🎵 Generate songs from lyrics + style prompts

## 星数曲线

```mermaid
xychart-beta
    title "slauger/suno-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [15, 14, 14]
```

2026-10-18 15 → 2026-10-31 14（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `89c2dca19064` · [字段定义](../../DATASET.md)*
