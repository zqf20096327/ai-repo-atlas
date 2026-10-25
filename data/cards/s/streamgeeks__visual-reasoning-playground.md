# streamgeeks/visual-reasoning-playground

⭐ 77 · JavaScript · MIT · 推送 2026-03-05 · [GitHub](https://github.com/streamgeeks/visual-reasoning-playground) · [官网](https://VisualReasoning.ai) · 组织维护

**面向广播/ProAV 的 17 个视觉语言模型演示工具集**

配套书籍《Visual Reasoning AI for Broadcast and ProAV》的 17 个即用型浏览器工具集合，通过 Moondream 云 API 的 caption/detect/query 能力实现场景描述、目标检测、手势控制 OBS、PTZ 摄像机自动跟踪、计数、区域告警、记分牌读取等功能；部分工具使用本地替代方案（Tesseract.js OCR、MediaPipe、浏览器内 Whisper）作对比。可在在线 Playground 直接试用（无需安装，自带示例视频），或克隆仓库后运行 python server.py 本地部署；需 Moondream API key（有免费额度），API 按调用计费，工具内置调用频率滑块控制成本。

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

- 17 个基于 Moondream VLM 的浏览器工具（检测/描述/问答/指向）
- PTZ 自动跟踪、OBS 手势控制与原生 OBS Python 脚本
- 部分工具提供本地替代对比：Tesseract.js OCR、MediaPipe、WebGPU/WASM 浏览器内 Whisper
- 支持 OBS WebSocket、vMix HTTP API、PTZOptics API 2.0、NDI、Webhooks、Home Assistant 集成

## 适用场景

- 直播活动中用 PTZ 摄像机自动跟踪演讲者
- 用手势或语音指令切换 OBS 场景
- 零售客流统计、仓库区域入侵告警等监控场景
- 多机位直播中做 AI 辅助构图与色彩匹配

## 场景标签

`目标检测` `多模态` `语音识别` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L8: **AI-powered visual reasoning tools for broadcast, live streaming, and ProAV professionals.**
> L10: 17 ready-to-use tools demonstrating real-world applications of Vision Language Models (VLMs) using Moondream. From 
> L261: 2. **Open Any Tool** - Visit the Visual Reasoning Playground

## 星数曲线

```mermaid
xychart-beta
    title "streamgeeks/visual-reasoning-playground 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 76 --> 78
    line [77, 77]
```

2026-10-18 77 → 2026-10-25 77（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6ec86e99c3b0` · [字段定义](../../DATASET.md)*
