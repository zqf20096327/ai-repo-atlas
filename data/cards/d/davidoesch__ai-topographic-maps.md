# davidoesch/ai-topographic-maps

⭐ — · [GitHub]() · 个人维护

**用 Gemini AI 将瑞士航拍图自动生成为瑞士风格地形图**

Python 脚本工具：从 swisstopo SWISSIMAGE WMTS 下载指定区域的 256×256 航拍瓦片（LV95 坐标系，zoom 26），逐块送入 Google Gemini（Nano Banana）图像模型，按基于 swisstopo Basemap Style 的提示词生成瑞士制图风格的地形图瓦片。用 SSIM 结构相似度检测生成失败（输出过接近原图）并自动重试至少 3 次。面向制图/GIS 从业者与研究者，需 Google API key（有免费额度，需配置账单）。README 声明结果存在瓦片间风格不一致、临时地物残留等限制，尚非生产就绪。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- WMTS 瓦片切分使任意大区域处理受限于 Gemini 1024×1024 像素输入限制
- SSIM 阈值（>0.35）检测失败生成并自动重跑至少 3 次
- prompt.txt 可自定义颜色、符号、要素与抽象程度
- 区域通过 map.geo.admin.ch 绘制多边形获取 KML 链接定义

## 适用场景

- 把瑞士航拍影像批量转为瑞士风格地形图瓦片
- 研究生成式 AI 制图的一致性与可扩展性
- 用 SSIM 指标筛除未发生风格转换的失败瓦片

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Automated generation of Swiss-style topographic maps from aerial imagery using Google’s Gemini AI (NanoBanana).
> L91: - **AI Model**: Google Gemini (Nano Banana) - available in free tier
> L100: 3. **AI Processing**: Each tile is processed through Gemini with a custom cartographic prompt based on swisstopo's

## 星数曲线

```mermaid
xychart-beta
    title "davidoesch/ai-topographic-maps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-28 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `64f8ac624c50` · [字段定义](../../DATASET.md)*
