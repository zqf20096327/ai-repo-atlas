# marcoaureliojf/viralcutterweb

⭐ 11 · Python · 推送 2026-04-05 · [GitHub](https://github.com/marcoaureliojf/viralcutterweb) · 个人维护

**Web 平台：AI 自动剪切病毒视频并生成风格化字幕**

ViralCutterWeb 是一个网页应用，上传视频或提供 URL 后，用 AI 自动建议病毒式剪辑点，并通过 pycaps 包自动生成风格化字幕；用户在 Web 界面中调整剪辑建议、选择字幕模板，处理完成后下载成片。受 ViralCutter 项目启发。通过 Docker Compose 部署，Docker 镜像因包含 AI 与视频处理依赖而体积较大，建议至少 4GB 内存。版本 0.1，处于早期开发阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 自动建议病毒式视频剪辑点
- pycaps 自动生成风格化字幕
- 支持视频上传或 URL 下载输入
- Web 界面调整剪辑与字幕模板

## 适用场景

- 把长视频自动剪成带字幕的病毒式短视频
- 为社交媒体批量生成剪辑片段
- 在本地用 Docker 自托管视频剪辑流程

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L6: ViralCutterWeb é uma aplicação web para corte automático de vídeos virais, inspirada no projeto ViralCutter. Utiliza
> L10: - Sugestão automática de cortes virais
> L11: - Geração de legendas automáticas com PyCaps

## 星数曲线

```mermaid
xychart-beta
    title "marcoaureliojf/viralcutterweb 星数(近 3 点)"
    x-axis ["2026-11-18", "2026-11-20", "2026-11-21"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-18 10 → 2026-11-21 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `31c96497179a` · [字段定义](../../DATASET.md)*
