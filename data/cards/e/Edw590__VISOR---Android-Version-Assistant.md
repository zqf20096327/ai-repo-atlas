# Edw590/VISOR---Android-Version-Assistant

⭐ 40 · Java · Apache-2.0 · 推送 2025-11-20 · [GitHub](https://github.com/Edw590/VISOR---Android-Version-Assistant) · 个人维护

**Android 离线语音助手：语音命令操控手机功能**

个人开发的 Android 语音助手应用，含命令识别、语音朗读、通话/短信处理、录音、相机/手电筒控制、系统状态检查等模块。命令识别支持句中同义词与否定/指代理解，非精确匹配；计划完全离线运行。设计初衷是供屏幕损坏或无法触屏的用户使用，可配合 root、特权系统应用与设备管理员获得全部功能。以 Releases 中的 debug APK 分发，最低支持 Android 4.1（API 16），主要在 8.1 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持句中插入词、同义词与否定/指代的命令识别（非精确匹配）
- PocketSphinx 热词唤醒 + 设备默认语音识别的两级识别
- 以 debug APK 分发，最低支持 Android 4.1
- 可装为特权系统应用并配合 root/设备管理员获得全部功能

## 适用场景

- 屏幕或触控不可用时仅靠按键与语音操控手机
- 通过语音开关 Wi-Fi、手电筒、查询时间日期等
- 来电与短信到达的语音播报提醒

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L40: Its command recognition submodule is not a simple recognition (have a look on the Advanced Commands Detection modul
> L72: |**Speech Recognition**|This is a module which contains 2 different speech recognizers: the commands one and Pocket

## 星数曲线

```mermaid
xychart-beta
    title "Edw590/VISOR---Android-Version-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-30 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `993c373d052e` · [字段定义](../../DATASET.md)*
