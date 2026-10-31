# facex-engine/facex

⭐ 349 · C · Apache-2.0 · 推送 2026-05-14 · [GitHub](https://github.com/facex-engine/facex) · [官网](https://facex-engine.github.io/facex/demo/) · 组织维护

**纯 WebAssembly/C99 浏览器端人脸全流程库：检测、3D 网格、识别、防伪**

面向在浏览器或边缘设备上本地运行人脸识别的开发者：提供 FCOS 人脸检测、98 点 landmark、576 点 3D 网格、MobileFaceNet+ArcFace 四档识别模型与 MiniFASNet 被动防伪，权重以 AES-256-GCM 密文分发并在浏览器内经 WebCrypto 解密。原生为纯 C99 零依赖实现（148 KB，AVX2/AVX-512），要求 GCC with AVX2 编译，浏览器端经 onnxruntime-web 运行、约 17 MB 权重。提供 C/Go/CLI 三种接口与在线 demo；识别需 112×112 ArcFace 对齐输入，否则准确率下降约 25 点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 检测→landmark→3D 网格→识别→防伪全流程模型自研，权重加密分发
- 纯 C99 零依赖原生实现，148 KB 库体积，声称单脸 3 ms
- 四种识别模型档位，LFW 十折均值 95.62%–99.07%
- 支持浏览器、x86-64、Apple Silicon（PR 中）、ARM/嵌入式等多目标

## 适用场景

- 浏览器端 KYC/人脸登录，人脸数据不出设备
- 边缘硬件上的门禁与无 GPU 摄像头识别
- 考试监考等本地身份核验场景

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L12: **Full face stack that runs entirely in the browser.** Detection, 98-point landmarks, dense 3D mesh, recognition, a
> L3:  Full face pipeline — detect, mesh, recognize, anti-spoof — in pure WebAssembly. Trained from scratch. No cloud, no 
> L122: 4. **Recognize** — MobileFaceNet + ArcFace, four size variants

## 星数曲线

```mermaid
xychart-beta
    title "facex-engine/facex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 347 --> 350
    line [348, 349, 349]
```

2026-10-18 348 → 2026-10-31 349（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b056cf6b22bc` · [字段定义](../../DATASET.md)*
