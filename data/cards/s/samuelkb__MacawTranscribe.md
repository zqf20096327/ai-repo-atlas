# samuelkb/MacawTranscribe

⭐ 22 · Python · AGPL-3.0 · 推送 2026-06-05 · [GitHub](https://github.com/samuelkb/MacawTranscribe) · [官网](https://samuelkb.github.io/Macaw-transcribe-site/) · 个人维护

**本地优先的长期录音转写系统：渐进式分块转录加说话人分离**

面向访谈、播客、科研录音等长音频的自托管转写应用：上传后自动做音频归一化、全录音说话人分离、分块并由本地模型转录，结果逐块渐进显示，边处理边校对。后端为 Django 编排，支持 MLX Whisper（Apple Silicon 优化），音频不出本机、无需外部 API。部分功能（实时编辑、分块重试、候选对比、更多导出格式）标注 Coming Soon，项目声明处于活跃开发期。安装通过 setup.sh 脚本，需在宿主机安装 ffmpeg，PostgreSQL 与 Redis 经 docker-compose 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 分块渐进式转录，处理中即可查看与校对
- 全录音说话人分离，说话人可重命名并全文同步
- 本地运行，模型本地加载、无需外部 API
- MLX Whisper 后端，针对 Apple Silicon 优化

## 适用场景

- 转写 1–2 小时的访谈或播客并按说话人整理文稿
- 敏感录音不出本机的私密转写
- 边转写边校对并导出 txt/md 文稿

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L10: A local-first transcription system designed to help you turn **long interviews, podcasts, research calls, and spoke
> L12: This project is optimized for **Apple Silicon Macs** and runs entirely on your machine using open-source speech mod
> L172: All processing runs locally on your machine.

## 星数曲线

```mermaid
xychart-beta
    title "samuelkb/MacawTranscribe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0c0b94feffc7` · [字段定义](../../DATASET.md)*
