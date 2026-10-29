# eren23/open_geo_spy

⭐ 28 · Python · 推送 2026-10-25 · [GitHub](https://github.com/eren23/open_geo_spy) · 个人维护

**GeoSpy 的开源实现：从图片推断拍摄地理位置**

GeoSpy 平台的开源替代实现：输入图像，借助视觉模型与 LLM（主题标签含 Gemini、OpenRouter）进行地理位置推断，面向 OSINT 与地理空间分析用户。作者在 README 中声明代码质量为初版：多数代码未经性能优化、结果时好时坏，并列出待办目标（去除偏置、重审 AI 生成代码、实验不同 LLM、增加地点样本）。运行方式为通过 docker compose 构建启动，凭据放入 .env 文件。

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

- 从图像推断地理位置（GeoSpy 的开源替代实现）
- 依赖 .env 配置凭据，docker compose 一键构建运行
- README 列出作者后续实验计划（不同 LLM、更多地点样本）

## 适用场景

- 对照片进行地理位置推断的 OSINT 调查
- 研究视觉 LLM 在地理定位任务上的表现
- 作为 GeoSpy 平台的开源自托管替代试用

## 场景标签

 · 领域:计算机视觉/OSINT 地理定位

## 证据(README 行号)

> L3: A very basic alternative open source implementation of the GeoSpy platform.

## 星数曲线

```mermaid
xychart-beta
    title "eren23/open_geo_spy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-29 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `238c2163b048` · [字段定义](../../DATASET.md)*
