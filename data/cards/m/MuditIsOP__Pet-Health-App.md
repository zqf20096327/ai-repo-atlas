# MuditIsOP/Pet-Health-App

⭐ 29 · Kotlin · 推送 2026-05-21 · [GitHub](https://github.com/MuditIsOP/Pet-Health-App) · 个人维护

**宠物主人用的 Android 健康监测 App：蓝牙遥测+AI 解读**

面向宠物主人的 Jetpack Compose Android 应用，采用 MVVM 分层架构。通过蓝牙 RFCOMM/SPP 连接模拟器或智能项圈，解析 JSON 遥测包（生命体征、活动、GPS），结合本地 TensorFlow Lite 模型与规则引擎做健康评分和异常标记，再调用 xAI Grok 或 Groq 的远程 LLM 生成面向主人的解读文案。后端使用 Firebase Auth/Cloud Firestore，另含 OSM 地图、地理围栏、SOS、兽医查找、聊天预约与 PDF 报告导出。需自备 Firebase 配置，LLM API key 为可选。无自定义服务端，需在 Android Studio 中构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 蓝牙遥测解析 + Firestore 持久化
- 本地 TFLite 健康评分与异常标记，远程 LLM 生成解读
- 地理围栏、SOS、兽医发现与实时聊天/预约
- PDF 健康报告导出与分享

## 适用场景

- 给宠物佩戴智能项圈后持续查看生命体征与活动
- 宠物离开安全区域时收到地理围栏提醒
- 查看 AI 生成的健康解读并导出 PDF 报告给兽医
- 紧急情况触发 SOS 流程并联系附近兽医

## 场景标签

 · 领域:宠物健康/移动应用

## 证据(README 行号)

> L21: PetHealthApp is the production-facing Android application in this workspace. It combines wearable telemetry ingesti
> L30: - Uses a local TensorFlow Lite model plus remote LLM-based analysis to generate health insights.
> L211: - AI is hybrid: local TFLite for scoring, remote LLM for explanation.

## 星数曲线

```mermaid
xychart-beta
    title "MuditIsOP/Pet-Health-App 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-31 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `4f3ef4301336` · [字段定义](../../DATASET.md)*
