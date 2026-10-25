# pedrol2b/react-native-vision-camera-mlkit

⭐ 58 · TypeScript · MIT · 推送 2026-08-20 · [GitHub](https://github.com/pedrol2b/react-native-vision-camera-mlkit) · [官网](https://www.npmjs.com/package/react-native-vision-camera-mlkit) · 个人维护

**React Native 相机插件：接入 Google ML Kit 做 OCR 与条码识别**

基于 Nitro 的 react-native-vision-camera v5 插件，向 React Native 应用暴露 Google ML Kit 的文字识别（OCR）与条码扫描能力。提供两种使用方式：摄像头实时帧钩子（useTextRecognition / useBarcodeScanning，运行于 frame worklet 内）与静态图像 API（processImageTextRecognition / processImageBarcodeScanning）。文本识别与条码扫描在编译期可各自独立启用/禁用，禁用即从构建中移除对应原生 SDK；并提供 Expo config plugin 自动写入原生配置。限制：要求 React Native 0.86+、iOS 15.1+/Android SDK 24+、VisionCamera v5（Nitro）；静态图仅支持本地文件（≤25MB），远程 URL 与 ph:// 不支持。

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

- 实时帧与静态图像两种 OCR/条码识别 API
- OCR 与条码功能编译期可选，可从原生构建中整体移除以减小体积
- 支持 5 种 OCR 语言（拉丁/中文/梵文/日文/韩文）与 14 种条码格式
- 提供 Expo config plugin、ROI 感兴趣区域裁剪与功能可用性查询工具

## 适用场景

- 在 React Native 应用中实时识别摄像头画面中的文字或条码
- 对相册选取的本地图片做 OCR 或条码解析（含 WiFi/URL/联系人等载荷）
- Expo prebuild 工程中按需引入 ML Kit 功能并控制包体积

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L19: A Nitro-based React Native Vision Camera v5 plugin that exposes high-performance Google ML Kit frame output feature
> L79: v2 implements two feature families: text recognition and barcode scanning.

## 星数曲线

```mermaid
xychart-beta
    title "pedrol2b/react-native-vision-camera-mlkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-25 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3e7ef6bf80d9` · [字段定义](../../DATASET.md)*
