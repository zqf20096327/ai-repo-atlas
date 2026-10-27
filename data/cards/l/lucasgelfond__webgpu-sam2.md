# lucasgelfond/webgpu-sam2

⭐ 184 · TypeScript · 推送 2026-01-10 · [GitHub](https://github.com/lucasgelfond/webgpu-sam2) · [官网](http://webgpu-sam2.lucasgelfond.online/) · 个人维护

**在浏览器中用 WebGPU 运行 Segment Anything 2 图像分割**

Facebook Research Segment Anything 2 的浏览器端 WebGPU 实现，基于 ONNX Runtime 与 Svelte 构建，完全在客户端运行推理，不上传数据。用户拖入图片后 encoder 生成图像嵌入，点击点位由 decoder 生成 256x256 掩膜并缩放绘制到画布。模型（encoder 超过 100MB）不打包进构建，首次下载后缓存于浏览器 origin private file system。输入限定 1024x1024。需安装 onnxruntime 开发版，构建用 Webpack；README 另给出用 samexporter 将模型转 ONNX/.ORT 的流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100% 客户端推理，数据不发送到服务器
- 点击交互式分割：encoder 生成嵌入，decoder 按点击点生成掩膜
- 模型首次下载后缓存于浏览器 origin private file system
- 提供将 SAM 2 模型转为 ONNX/.ORT 格式的流程说明

## 适用场景

- 在浏览器中对图片做交互式点击分割，无需上传数据
- 研究 WebGPU 运行 ONNX 模型的工程实践
- 参考模型导出与浏览器缓存大模型的方案

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repo includes a WebGPU implementation of Facebook Research's model, Segment Anything 2, using WebGPU. It runs c
> L25: Every time a user clicks a point, we pass the point of their mouse and the results of encoding to our decoder. It w

## 星数曲线

```mermaid
xychart-beta
    title "lucasgelfond/webgpu-sam2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 183 --> 185
    line [184, 184]
```

2026-10-18 184 → 2026-10-27 184（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `26e090b83b6d` · [字段定义](../../DATASET.md)*
