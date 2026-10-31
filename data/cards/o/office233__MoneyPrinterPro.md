# office233/MoneyPrinterPro

⭐ 19 · JavaScript · MIT · 推送 2026-05-28 · [GitHub](https://github.com/office233/MoneyPrinterPro) · [官网](https://github.com/office233/MoneyPrinterPro) · 个人维护

**本地优先的虚拟人像图文生成管线：身份保持与质量把关**

基于 Next.js 的内容生成管线：用户上传参考照片创建 persona，调用 Gemini 生成身份保持的图像，再用 VEO 3.1 生成 8 秒 9:16 视频；内置 7 个视觉引擎组合提示词、内容规划器（支柱选择/防重复场景/文案生成）、Autopilot 批量生成模式，以及可选的 Python FastAPI 质量评分服务（5 通道分析）和发布质量门。自带 API key 直付 Google，数据存本地。评分服务为实验性需手动部署，暂无生产级认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 参考照片实现跨输出的人脸身份保持
- Gemini 出图 + VEO 3.1 出 8 秒 9:16 视频
- 7 个视觉引擎（光照/阴影/运动/天气/服装等）组合提示词
- Autopilot 批量生成与发布质量门

## 适用场景

- 为 Reels/TikTok/Shorts 批量生成同一人设的图像与视频
- 保持一致身份的多风格图像创作
- 自动规划内容并按质量阈值过滤低质输出

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L5: **Local-first AI creative pipeline** for persona-based image and video generation with identity preservation, prompt
> L61: - ✅ **Image + Video generation** — Gemini for images, VEO 3.1 for cinematic 9:16 video

## 星数曲线

```mermaid
xychart-beta
    title "office233/MoneyPrinterPro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `e8d5b5dd04e3` · [字段定义](../../DATASET.md)*
