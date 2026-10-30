# androiddevnotes/android-modern-movie-app

⭐ 38 · Kotlin · 推送 2026-08-01 · [GitHub](https://github.com/androiddevnotes/android-modern-movie-app) · [官网](https://x.com/androiddevnotes/status/1835145851976454461) · 个人维护

**AI 生成代码的 Android 电影浏览应用（Jetpack Compose）**

基于 Kotlin 与 Jetpack Compose 的 Android 电影应用，对接 TMDB API，按 MVVM 架构组织：ViewModel 通过 Repository 与 ApiService 获取数据，StateFlow 驱动 Compose UI 重组。功能含分类浏览、搜索、收藏、自定义片单（需认证）、网格/列表切换、筛选与明暗主题。README 声明全部代码由大语言模型生成或建议，AI 参与的是开发过程而非应用内功能。需自行申请 TMDB API Key 并写入 gradle.properties。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 代码由大语言模型生成或建议，随 AI 持续演进
- MVVM 架构：ViewModel/Repository/StateFlow 数据流
- 支持分类浏览、搜索、收藏、自定义片单与筛选
- TMDB 请求令牌→会话 ID 的认证流程

## 适用场景

- 作为 Jetpack Compose + MVVM 的示例工程学习
- 观察 AI 生成代码在真实 Android 项目中的形态
- 二次开发个人电影浏览与片单应用

## 场景标签

 · 领域:移动开发/示例工程

## 证据(README 行号)

> L5: This Android app interacts with The Movie Database (TMDB) API. Every line of code has been generated
> L9: Beta = OpenAI

## 星数曲线

```mermaid
xychart-beta
    title "androiddevnotes/android-modern-movie-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `da6e39973f39` · [字段定义](../../DATASET.md)*
