# aymenhmaidiwastaken/GeoSnap

⭐ 16 · JavaScript · 推送 2026-05-25 · [GitHub](https://github.com/aymenhmaidiwastaken/GeoSnap) · 个人维护

**AI 照片地理定位 Web 应用：分析视觉线索在地图标出拍摄地**

基于 Node.js/Express 与 Vanilla JS 的照片地理定位应用：上传照片后经 Sharp 压缩为 JPEG，由视觉 AI（Google Gemini 或本地 Ollama LLaMA 3.2 Vision）分析街道标志、建筑、文字、植被等 15+ 类视觉线索，返回坐标与置信度的结构化 JSON，经多策略修复解析后在 Leaflet 地图上以动画标记与置信半径圈展示。支持 Street View 一键访问与拖拽上传。README 提示本地模型精度低于 Gemini，推荐 Gemini 免费层。面向终端用户，git clone 源码运行，需 Node.js 18+ 与 Gemini API key 或本地 Ollama。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15+ 类视觉线索的 AI 地理定位分析
- 双 AI 后端：Google Gemini（云端）与 Ollama（本地离线）
- 结构化 JSON 输出 + 多策略畸形输出修复引擎
- Leaflet 交互地图：置信半径圈、多图层切换、Street View 访问

## 适用场景

- 上传照片推测拍摄地点并在地图上查看
- 离线环境下用 Ollama 本地模型做照片地理定位
- 通过 API 集成照片地理定位分析

## 场景标签

 · 领域:计算机视觉/地理定位

## 证据(README 行号)

> L3: **Upload any photo. AI pinpoints the exact location on the map.**
> L62: Photo Upload ──> Image Optimization ──> AI Vision Analysis ──> JSON Parsing ──> Map Rendering

## 星数曲线

```mermaid
xychart-beta
    title "aymenhmaidiwastaken/GeoSnap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `35d6ebd1eee2` · [字段定义](../../DATASET.md)*
