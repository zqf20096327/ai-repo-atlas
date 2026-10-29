# niksbanna/medidiet-app

⭐ 20 · TypeScript · Apache-2.0 · 推送 2026-05-28 · [GitHub](https://github.com/niksbanna/medidiet-app) · 个人维护

**面向糖尿病/高血压等病患的 AI 营养管理移动应用**

基于 React Native、Expo 与 TypeScript 的跨平台（iOS/Android）移动应用，面向需要按疾病条件管理饮食的个人用户：通过 Google Gemini API 按糖尿病、高血压等状况生成 7 天个性化餐计划与营养分析，并提供餐食记录、依从度自评、BMI 计算与进度仪表盘。支持离线时的本地餐食生成回退；Gemini API key 可在应用内配置，未配置时跳过。数据经 AsyncStorage 本地存储；生产构建需 EAS CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini API 生成按疾病条件的 7 天个性化餐计划
- 餐食记录、依从度自评与每周趋势可视化
- 离线回退：无网络时本地生成餐计划
- AsyncStorage 本地数据持久化与 BMI 计算

## 适用场景

- 糖尿病或高血压患者获取符合自身状况的每周餐计划
- 记录每餐饮食并跟踪热量与依从度
- 通过仪表盘查看营养摄入趋势与健康洞察

## 场景标签

 · 领域:健康/医疗应用

## 证据(README 行号)

> L21: **MediDiet AI** is a cutting-edge mobile application designed to help individuals manage their nutrition in relatio
> L34: - **Gemini API Integration**: Utilizes Google's advanced AI for intelligent meal suggestions

## 星数曲线

```mermaid
xychart-beta
    title "niksbanna/medidiet-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `578faa11d809` · [字段定义](../../DATASET.md)*
