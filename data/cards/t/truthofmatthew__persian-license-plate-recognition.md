# truthofmatthew/persian-license-plate-recognition

⭐ 450 · Python · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/truthofmatthew/persian-license-plate-recognition) · 个人维护

**伊朗车牌识别工具：从照片/视频/摄像头读牌并判定放行**

基于 YOLOv5 与 ONNX Runtime 的伊朗车牌识别系统：检测车牌、逐字符识别、波斯车牌语法校验、跨帧投票使每车只记一次，并按居民名单判定允许/拒绝。以四种形态提供：浏览器内运行（WebGPU/WASM，离线可用）的 Web 应用、PySide6 桌面应用、FastAPI API 服务器与门禁边缘 agent（RTSP 读取、离线缓冲），另有 Docker 编排与训练/量化脚本。README 明确标注当前模型在模糊、夜间、特种车牌上识别较差，重训尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv5s 车牌检测 + 43 类字符检测 + 波斯语法校验 + 跨帧投票
- 同一模型在浏览器（WebGPU/WASM）、桌面、API 服务器、边缘 agent 四处运行
- 浏览器端数据存 IndexedDB，照片不上传；API 含 HMAC 签名 webhook 与角色 API key
- 提供 ONNX 导出、合成车牌生成、基准测试与 INT8 量化脚本

## 适用场景

- 小区/园区门禁自动识别车牌并按居民名单放行
- 从摄像头/视频/照片中读出伊朗车牌文本
- 将车牌读取接入自有系统（Python 库或 API 服务）

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Read Iranian license plates from a camera, a video or a photo, and decide whether the car may enter.
> L92: frame ─► plate detector (YOLOv5s, ONNX) ─► crop ─► character detector (43 classes)
> L95:       ─► one result per car, e.g. 34D31966 / ۳۴ د ۳۱۹ - ایران ۶۶

## 星数曲线

```mermaid
xychart-beta
    title "truthofmatthew/persian-license-plate-recognition 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-30"]
    y-axis "stars" 449 --> 451
    line [450, 450]
```

2026-10-28 450 → 2026-10-30 450（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3ed7325cbf57` · [字段定义](../../DATASET.md)*
