# rohitaryal/imageFX-api

⭐ 133 · TypeScript · MIT · 推送 2025-12-20 · [GitHub](https://github.com/rohitaryal/imageFX-api) · [官网](https://imagefx.rohitsharma.com.np/) · 个人维护

**非官方逆向的 Google ImageFX (Imagen) 图像生成 API 封装**

对 labs.google 的 ImageFX 服务做逆向封装的 npm 包，提供文生图（IMAGEN_4 等模型可选）、图片生成提示词/描述（caption）、按 media id 取回图片三类功能。以 CLI 命令 imagefx 和 TypeScript 模块两种方式调用，认证依赖从浏览器导出的 Google Cookie（GOOGLE_COOKIE 环境变量），并附 Cookie 提取与地区限制应对（VPN）指引。项目声明与 Google 无隶属关系，需自担风险使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文生图，支持选择模型与纵横比（IMAGEN_4/IMAGEN_3_5 等）
- 图生文 caption，支持 jpeg/png/webp/avif 等多种图片格式
- CLI 与 TypeScript 模块双调用方式
- 按 media id 取回已生成图片

## 适用场景

- 在命令行或脚本中调用 ImageFX 生成图片
- 用现有图片生成提示词或描述文本
- 国内等 ImageFX 不可用地区通过 Cookie 调用服务

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Unofficial free reverse engineered api for imageFX(imagen) service provided by labs.google
> L19: 1. Text to image using `IMAGEN_4`

## 星数曲线

```mermaid
xychart-beta
    title "rohitaryal/imageFX-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 132 --> 134
    line [133, 133]
```

2026-10-18 133 → 2026-10-25 133（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `cf2a8c43c935` · [字段定义](../../DATASET.md)*
