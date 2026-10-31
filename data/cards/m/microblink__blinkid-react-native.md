# microblink/blinkid-react-native

⭐ 188 · TypeScript · 推送 2026-09-09 · [GitHub](https://github.com/microblink/blinkid-react-native) · 组织维护

**React Native 证件扫描插件：封装 BlinkID SDK 做 ID 识别**

Microblink 官方的 React Native 插件，封装原生 BlinkID SDK 与 BlinkID UX 模块，为跨平台 App 提供证件扫描：摄像头扫描（performScan）与静态图片 Base64 识别（performDirectApiScan），支持条码、MRZ、VIZ、文档拍摄四个可配置模块，以及按国家/地区/证件类型的过滤与结果脱敏（redaction，四种模式）。初始化需有效 license key，可在 Developer Hub 免费申请试用。要求 iOS 16.0+、Android API 24+，在 React Native 0.82.x 构建测试。

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

- 摄像头扫描与 DirectAPI 静态图片识别两种扫描方式
- 条码/MRZ/VIZ/文档拍摄四个可配置扫描模块
- 按国家、地区、证件类型的 class 过滤与四种 redaction 脱敏模式
- SDK 预加载（loadBlinkIdSdk）与自动卸载、资源缓存管理

## 适用场景

- 在 React Native App 中加入证件扫描完成 KYC/实名流程
- 从相册图片提取证件信息（单面/双面识别）
- 对扫描结果做字段级脱敏以满足隐私合规

## 场景标签

`OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5: The BlinkID SDK is a comprehensive solution for implementing secure document scanning in React Native cross-platform
> L43: 2. **Multiside DirectAPI scanning** — extracting document information from two static images (from the gallery).

## 星数曲线

```mermaid
xychart-beta
    title "microblink/blinkid-react-native 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 187 --> 189
    line [188, 188]
```

2026-10-18 188 → 2026-10-31 188（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `bb45c897be67` · [字段定义](../../DATASET.md)*
