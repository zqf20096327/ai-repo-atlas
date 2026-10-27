# watadarkstar/react-native-nsfw-detector

⭐ 39 · JavaScript · NOASSERTION · 推送 2026-07-19 · [GitHub](https://github.com/watadarkstar/react-native-nsfw-detector) · [官网](https://www.npmjs.com/package/react-native-nsfw-detector) · 个人维护

**React Native/Expo 的 iOS 端本地 NSFW 图片检测库**

基于 CoreML 模型的 React Native / Expo 原生模块，在 iOS 设备本地推理检测图片中的裸露与不安全内容，无需网络调用，提供基于 Promise 的 checkNSFW API。模型经 CreateML 训练，需 Xcode 10+ 编译、iOS 13+，README 注明模拟器推理准确率显著下降，推荐真机测试。基于 LOVOO 的 NSFWDetector 工作，以 npm 包形式分发，附 /example 示例 Expo 应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CoreML 设备本地推理，检测 NSFW/SFW 内容
- 无需网络调用，提供基于 Promise 的 API
- 兼容 React Native 0.70+ 与 Expo 原生模块
- 附带可运行的 Expo 示例应用

## 适用场景

- 在 React Native 应用中上传前过滤不安全图片
- iOS 端离线内容审核
- 集成到 Expo 项目中做本地图像安全检测

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5:  A fast on device AI image safety detector for React Native / Expo using a CoreML model
> L31: - On device inference using CoreML
> L32: - Detects NSFW and safe for work content

## 星数曲线

```mermaid
xychart-beta
    title "watadarkstar/react-native-nsfw-detector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-27 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e5925f093e9e` · [字段定义](../../DATASET.md)*
